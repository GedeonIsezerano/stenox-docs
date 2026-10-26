#!/usr/bin/env python3
"""Check local routes/assets and the documented model catalog against committed app source."""
from pathlib import Path
from urllib.parse import urlsplit, unquote
import argparse, hashlib, json, re, subprocess, sys

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--app-dir', type=Path, default=root.parent / 'app')
parser.add_argument('--keygen-dir', type=Path, default=root.parent / 'keygen')
parser.add_argument('--website-dir', type=Path, default=root.parent / 'website')
parser.add_argument('--allow-newer-main', action='store_true', help='Check the recorded snapshots without requiring repository mains to match.')
parser.add_argument('--candidate-inputs', type=Path, help='Audited exact source inputs for an unpublished release candidate.')
parser.add_argument('--candidate-manifest', type=Path, help='Prepared app manifest bound by the candidate inputs.')
args = parser.parse_args()
candidate_mode = args.candidate_inputs is not None
if candidate_mode != (args.candidate_manifest is not None):
    parser.error('--candidate-inputs and --candidate-manifest must be supplied together')
if candidate_mode and args.allow_newer_main:
    parser.error('Candidate validation requires exact inputs, not --allow-newer-main')
snapshot = json.loads((args.candidate_inputs if candidate_mode else root / 'maintenance/source-snapshot.json').read_text())
commit = snapshot['app_commit']
errors = []
def check(ok, message):
    if not ok: errors.append(message)
if candidate_mode:
    check(snapshot.get('schema_version') == 1 and snapshot.get('kind') == 'docs-candidate-inputs', 'Invalid candidate input record')
    check(snapshot.get('app_source_mode') == 'candidate', 'Candidate record must describe unpublished candidate source')
    manifest_bytes = args.candidate_manifest.read_bytes()
    check(hashlib.sha256(manifest_bytes).hexdigest() == snapshot.get('app_manifest_sha256'), 'Candidate app manifest changed')
    manifest = json.loads(manifest_bytes)
    check(manifest.get('status') == 'prepared' and manifest.get('publicationPolicy') == 'candidate-only' and manifest.get('published') is False,
          'Use a prepared unpublished app manifest; candidate validation does not authorize publication')
    check(manifest.get('sourceSHA') == commit == snapshot.get('app_build_commit'), 'Candidate app source differs from prepared build')
    check(manifest.get('releaseToolingSHA') == snapshot.get('release_tooling_commit'), 'Candidate release tooling differs')
    check(manifest.get('version') == snapshot.get('version'), 'Candidate version differs')
    check(manifest.get('notarization', {}).get('status') == 'Accepted', 'Candidate notarization is not accepted')
    check(manifest.get('bundleID') == 'com.gedeonapps.stenox' and manifest.get('feedURL') == 'https://stenox.app/updates/appcast.xml', 'Candidate is not the production release identity')
    for name, expected in manifest.get('artifacts', {}).items():
        artifact = args.candidate_manifest.parent / name
        check(artifact.resolve().is_relative_to(args.candidate_manifest.parent.resolve()), 'Candidate artifact escapes its directory')
        check(artifact.is_file() and hashlib.sha256(artifact.read_bytes()).hexdigest() == expected, 'Candidate artifact changed: ' + name)
    check(hashlib.sha256((root / 'changelog.mdx').read_bytes()).hexdigest() == snapshot.get('changelog_sha256'), 'Approved changelog changed')
    for label, directory, revision in [('app', args.app_dir, commit), ('keygen', args.keygen_dir, snapshot['keygen_commit']), ('website', args.website_dir, snapshot['website_commit'])]:
        check(bool(re.fullmatch('[0-9a-f]{40}', revision)), 'Use an exact candidate source commit: ' + label)
        pinned = subprocess.check_output(['git', 'rev-parse', revision + '^{commit}'], cwd=directory, text=True).strip()
        check(pinned == revision, 'Candidate source commit does not resolve exactly: ' + label)
        bindings = snapshot.get('source_files', {}).get(label, {})
        check(bool(bindings), 'Candidate input omits source bindings: ' + label)
        for name, expected in bindings.items():
            contents = subprocess.check_output(['git', 'show', revision + ':' + name], cwd=directory)
            check(hashlib.sha256(contents).hexdigest() == expected, 'Candidate source input changed: ' + label + '/' + name)
def source(path):
    return subprocess.check_output(['git', 'show', f'{commit}:{path}'], cwd=args.app_dir, text=True)
def doc(path):
    return (root / (path + '.mdx')).read_text()
def ids_in_table(path, section, next_section):
    text = doc(path).split(section, 1)[1].split(next_section, 1)[0]
    return set(re.findall(r'\|\s*`([^`]+)`\s*\|', text))

config = json.loads((root / 'docs.json').read_text())
files = {str(p.relative_to(root)).removesuffix('.mdx'): p for p in root.rglob('*.mdx') if '.git' not in p.parts}
redirects = {r['source']: r['destination'] for r in config.get('redirects', [])}
routes = {'/' + path for path in files} | {'/'}
nav = []
def walk(node):
    if isinstance(node, dict):
        for key, value in node.items():
            if key == 'pages':
                for page in value:
                    if isinstance(page, str):
                        nav.append(page); check(page in files, f'Missing navigation page: {page}')
                    else: walk(page)
            else: walk(value)
    elif isinstance(node, list):
        for value in node: walk(value)
walk(config['navigation'])
check(len(nav) == len(set(nav)), 'Duplicate navigation page')
for old, new in redirects.items():
    check(old != new, f'Self redirect: {old}')
    check(new in routes, f'Redirect destination missing: {old} -> {new}')

checked = 0
def local_link(value, owner):
    global checked
    if not value.startswith('/') or value.startswith('//'): return
    path = unquote(urlsplit(value).path).rstrip('/') or '/'
    checked += 1
    check(path in routes or path in redirects or (root / path.lstrip('/')).is_file(), f'{owner}: missing local target {path}')
for name, file in files.items():
    text = file.read_text()
    if not name.startswith('snippets/'):
        check(text.startswith('---\n'), f'{name}: missing frontmatter')
        check(bool(re.search(r'^description: .+', text, re.M)), f'{name}: missing description')
    for href in re.findall(r'\]\((/[^\s)]+)\)|(?:href|src)="(/[^\"]+)"', text):
        local_link(href[0] or href[1], name)
def config_links(value):
    if isinstance(value, str): local_link(value, 'docs.json')
    elif isinstance(value, dict):
        for v in value.values(): config_links(v)
    elif isinstance(value, list):
        for v in value: config_links(v)
config_links(config)
for match in re.findall(r'url\([\'\"]?(/[^)\'\"]+)', (root/'style.css').read_text()):
    local_link(match, 'style.css')

mlx = source('Stenox/Services/LLM/Providers/MLXProvider.swift')
models = re.findall(r'LocalLLMModelConfiguration\(id: "([^"]+)", name: "([^"]+)".*?isDeprecated: (true|false)', mlx)
s1_id = re.search(r'static let modelID = "([^"]+)"', source('Stenox/Services/LLM/S1Correction.swift')).group(1)
active = {mid for mid, _, old in models if old == 'false'} | {s1_id}
check(active == ids_in_table('providers/llm/mlx-local', '## Current cleanup catalog', '## Load before polishing'), 'Cleanup table differs from runtime catalog')
legacy = {mid for mid, _, old in models if old == 'true'}
check(legacy == ids_in_table('providers/llm/mlx-local', '## Older models', '## Meetings are separate'), 'Legacy cleanup table differs from runtime catalog')
for provider, page in [('Parakeet', 'parakeet-local'), ('WhisperKit', 'whisperkit-local')]:
    swift = source(f'Stenox/Services/Transcription/Providers/{provider}Provider.swift')
    catalog = swift.split('static let availableModels',1)[1].split('// MARK:',1)[0]
    if provider == 'WhisperKit':
        # WhisperKit declares the catalog on StenoxTranscriptionModelInfo.
        catalog = swift.split('static let availableModels',1)[1].split('actor ',1)[0]
    ids = set(re.findall(r'\bid: "([^"]+)"', catalog))
    documented = set(re.findall(r'\|\s*`([^`]+)`\s*\|', doc('providers/transcription/'+page)))
    check(ids == documented, f'{provider} table differs from source: {ids ^ documented}')
cohere = source('Stenox/Services/Transcription/Providers/CohereTranscribeProvider.swift')
cohere_id = re.search(r'static let modelId = "([^"]+)"', cohere).group(1)
check(cohere_id in doc('providers/transcription/cohere-local'), 'Missing Cohere model ID')
brief = source('Stenox/Services/Notetaker/NotetakerBriefModel.swift')
brief_id = re.search(r'static let modelID = "([^"]+)"', brief).group(1)
check(brief_id in doc('meetings/processing'), 'Meeting model differs from source')
check('Nemotron-3-Diarization-8bit' in source('Stenox/Services/Notetaker/NemotronDiarizer.swift') and 'Nemotron-3-Diarization-8bit' in doc('meetings/processing'), 'Missing diarizer model')
check(not any('groq' in page for page in nav), 'Removed Groq provider is in active navigation')
def repository_source(directory, revision, path):
    return subprocess.check_output(['git', 'show', f'{revision}:{path}'], cwd=directory, text=True)
keygen_commit = snapshot['keygen_commit']
website_commit = snapshot['website_commit']
license_service = repository_source(args.keygen_dir, keygen_commit, 'src/service.ts')
commerce = repository_source(args.website_dir, website_commit, 'lib/commerce.ts')
terms = commerce.split('export const PURCHASE_TERMS = {', 1)[1].split('} as const', 1)[0]
for field, expected in [('devices', 2), ('verificationDays', 7), ('trialDays', 7), ('paidOfflineDays', 30)]:
    actual = re.search(rf'\b{field}:\s*(\d+)', terms)
    check(actual is not None and int(actual.group(1)) == expected, f'Review documented license term: {field}')
check('now+7*DAY' in license_service and 'refreshAfter:Math.min(now+7*DAY,exp)' in license_service,
      'Review documented trial and weekly refresh against licensing service')
check('Math.min(now+30*DAY,l.expires??Infinity)' in license_service,
      'Review documented paid offline window and underlying license expiry')
check('deviceLimit:l.limit' in license_service, 'Review original device allowance preservation')
license_ui = source('Stenox/Views/Settings/LicensingSettingsContent.swift')
license_labels = ['Start 7-day trial', 'Activate', 'Manage purchase and devices']
license_labels += ['Remove license'] if '"Remove license"' in license_ui else ['Verify now', 'Deactivate this Mac']
for label in license_labels:
    check(f'"{label}"' in license_ui and label in doc('pricing/overview'), f'License guide/UI label mismatch: {label}')
if candidate_mode:
    license_manager = source('Stenox/Managers/LicensingManager.swift')
    check('await manager.refreshIfDue()' in license_ui and 'func refreshIfDue()' in license_manager,
          'Review documented automatic license verification against candidate UI/manager')
    check('automatically when verification is due' in doc('pricing/overview'), 'License guide omits automatic due verification')
    check('Verify now' not in doc('pricing/overview') + doc('guides/troubleshooting') and 'Deactivate this Mac' not in doc('pricing/overview'), 'Candidate docs retain obsolete licensing controls')
    metadata = source('Stenox/Core/Models/ProviderMetadata.swift')
    subscriptions = source('Stenox/Services/Notetaker/NotetakerInsightProvider.swift')
    check('NotetakerInsightProvider.subscriptions.map' in metadata and '[.codex, .claude, .antigravity]' in subscriptions,
          'Review candidate subscription Polish provider choices')
    polish_row = next((line for line in doc('providers/overview').splitlines() if line.startswith('| Dictation Polish |')), '')
    check(all(name in polish_row for name in ['Gemini', 'Codex', 'Claude Code', 'Google Antigravity']), 'Polish provider table omits a candidate choice')
    runtime = source('Tools/MeetingAgentBridge/runtime-paths.mjs')
    check('codexAppExecutables' in runtime and 'runtime_missing' in runtime, 'Review installed runtime discovery against candidate source')
    check('bundled runtimes' not in doc('meetings/processing') and 'installed Codex CLI' in doc('meetings/processing'), 'Subscription docs misstate runtime installation')
    check('Subscription Polish' in doc('providers/local-privacy'), 'Privacy guide omits subscription Polish data flow')
    notes_bytes = subprocess.check_output(['git', 'show', commit + ':Installer/release-notes/' + snapshot['version'] + '.json'], cwd=args.app_dir)
    check(hashlib.sha256(notes_bytes).hexdigest() == snapshot.get('release_notes_sha256') == manifest.get('artifacts', {}).get('release-notes.json'), 'Approved release notes differ from candidate source/artifact')
    notes = json.loads(notes_bytes)
    section = doc('changelog').split('## ' + snapshot['version'] + '\n', 1)[1].split('\n## ', 1)[0]
    check(notes['summary'] in section and [line[2:] for line in section.splitlines() if line.startswith('- ')] == [item for group in notes['sections'] for item in group['highlights']], 'Changelog differs from approved canonical notes')
    refund = re.search(r'\brefundDays:\s*(\d+)', terms)
    check(refund is not None and int(refund.group(1)) == 7, 'Review refund term against candidate commerce source')
app_source_mode = snapshot.get('app_source_mode', 'main')
check(app_source_mode in {'main', 'published', 'candidate'}, f'Unknown app source mode: {app_source_mode}')
for label, directory, revision in [('App', args.app_dir, commit), ('Keygen', args.keygen_dir, keygen_commit), ('Website', args.website_dir, website_commit)]:
    if candidate_mode:
        print(f'{label} source is pinned to exact candidate input {revision}; no deployment or native acceptance is inferred.')
        continue
    current = subprocess.check_output(['git','rev-parse','main'], cwd=directory, text=True).strip()
    if label == 'App' and app_source_mode == 'published':
        check(revision == snapshot.get('app_build_commit') == snapshot.get('release_tooling_commit'),
              'Published app source must match the recorded build and release-tooling commits')
        check(snapshot.get('release_acceptance', {}).get('published') is True,
              'Published app source requires recorded publication acceptance')
        check(subprocess.run(['git', 'merge-base', '--is-ancestor', revision, current], cwd=directory).returncode == 0,
              f'Published app source {revision} is not an ancestor of app main {current}')
        print(f'App source is pinned to published {revision}; current main {current} is not included.')
        continue
    check(args.allow_newer_main or current == revision, f'{label} main advanced to {current}; review delta from {revision}')
print(f'Checked {len(files)} MDX files, {len(nav)} navigation pages, {checked} local links/assets, and local model catalogs against app {commit}.')
print(f'Checked license terms and UI labels against keygen {keygen_commit} and website {website_commit}.')
if errors:
    print('\n'.join('ERROR: ' + error for error in errors)); sys.exit(1)
print('PASS')
