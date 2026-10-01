#!/usr/bin/env python3
"""Check local routes/assets and the documented model catalog against committed app source."""
from pathlib import Path
from urllib.parse import urlsplit, unquote
import argparse, json, re, subprocess, sys

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--app-dir', type=Path, default=root.parent / 'app')
parser.add_argument('--keygen-dir', type=Path, default=root.parent / 'keygen')
parser.add_argument('--website-dir', type=Path, default=root.parent / 'website')
parser.add_argument('--allow-newer-main', action='store_true', help='Check the recorded snapshots without requiring repository mains to match.')
args = parser.parse_args()
snapshot = json.loads((root / 'maintenance/source-snapshot.json').read_text())
commit = snapshot['app_commit']
errors = []
def check(ok, message):
    if not ok: errors.append(message)
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
for label in ['Start 7-day trial', 'Activate', 'Verify now', 'Deactivate this Mac', 'Manage purchase and devices']:
    check(f'"{label}"' in license_ui and label in doc('pricing/overview'), f'License guide/UI label mismatch: {label}')
for label, directory, revision in [('App', args.app_dir, commit), ('Keygen', args.keygen_dir, keygen_commit), ('Website', args.website_dir, website_commit)]:
    current = subprocess.check_output(['git','rev-parse','main'], cwd=directory, text=True).strip()
    check(args.allow_newer_main or current == revision, f'{label} main advanced to {current}; review delta from {revision}')
print(f'Checked {len(files)} MDX files, {len(nav)} navigation pages, {checked} local links/assets, and local model catalogs against app {commit}.')
print(f'Checked license terms and UI labels against keygen {keygen_commit} and website {website_commit}.')
if errors:
    print('\n'.join('ERROR: ' + error for error in errors)); sys.exit(1)
print('PASS')
