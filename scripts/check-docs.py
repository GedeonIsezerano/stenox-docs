#!/usr/bin/env python3
"""Check local routes/assets and the documented model catalog against committed app source."""
from pathlib import Path
from urllib.parse import urlsplit, unquote
import argparse, json, re, subprocess, sys

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--app-dir', type=Path, default=root.parent / 'app')
parser.add_argument('--allow-newer-main', action='store_true', help='Check the recorded snapshot without requiring current main to match.')
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
for _, name, old in models:
    if old == 'true': check(name in doc('providers/llm/mlx-local').split('## Older models')[1], f'Missing legacy model: {name}')
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
current = subprocess.check_output(['git','rev-parse','main'], cwd=args.app_dir, text=True).strip()
check(args.allow_newer_main or current == commit, f'App main advanced to {current}; review delta from {commit}')
print(f'Checked {len(files)} MDX files, {len(nav)} navigation pages, {checked} local links/assets, and current local model catalogs against {commit}.')
if errors:
    print('\n'.join('ERROR: ' + error for error in errors)); sys.exit(1)
print('PASS')
