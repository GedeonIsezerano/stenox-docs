# Stenox documentation

Mintlify documentation for Stenox dictation, local models, meeting capture, and notes. Public pages are MDX; navigation, appearance, redirects, and branding live in `docs.json`. `style.css` extends Mintlify with the current website's warm surfaces and typography.

## Preview and validate

Use Node.js and the reviewed Mintlify CLI version:

```sh
npx --yes mint@4.2.964 dev --no-open --port 3022 --telemetry false
npx --yes mint@4.2.964 validate --telemetry false
npx --yes mint@4.2.964 broken-links --telemetry false
npx --yes mint@4.2.964 a11y --telemetry false
python3 scripts/check-docs.py
```

The preview is at `http://127.0.0.1:3022`. Local search requires a separate Mintlify CLI login; a working preview does not establish search service readiness. No login is needed for the build, route, or catalog checks above.

## Source of truth

See [the source audit](maintenance/source-audit.md) and [recorded snapshot](maintenance/source-snapshot.json). App claims come from committed local `main`, not uncommitted experiments or synthetic UI demos. Website styling follows its working tree. Model download sizes are catalog estimates, not RAM guarantees.

`check-docs.py` checks the documented local model IDs against that exact app commit, navigation and local targets, and whether app `main` advanced. By default it expects the app repo at `../app`; use `--app-dir /path/to/app` elsewhere. If main advances, inspect the delta before updating the recorded snapshot. `--allow-newer-main` checks the old snapshot deliberately without accepting new behavior.

The [local consolidation report](maintenance/consolidation-2026-10-01.md) records the retained work and validation. Final V2 alignment awaits the coordinator's final app baseline; the recorded source snapshot has not been advanced during consolidation.

## Release boundary

The docs describe development capabilities. The banner and release page distinguish those from the public download and staged paid offer. Do not claim that a paid build or checkout is live based on source or a local preview. Committing, pushing, and publishing require their own authorization.

Maintenance evidence and scripts are excluded from public docs through `docs.json`. Historical image files remain in the repository, but the active guides do not use the old screenshots or animated mock UI. Replace them only with verified current imagery.
