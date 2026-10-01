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

See [the V2 readiness audit](maintenance/v2-readiness-2026-10-01.md) and [recorded snapshot](maintenance/source-snapshot.json). The [original refresh audit](maintenance/source-audit.md) preserves the earlier claim map and rendering evidence. App claims come from the recorded committed source, not uncommitted experiments or synthetic UI demos. Licensing terms are checked against the recorded app, keygen, and website commits. Website styling retains the consolidated theme. Model download sizes are catalog estimates, not RAM guarantees.

`check-docs.py` checks current and legacy model IDs, license terms and UI labels, navigation, local targets, and whether a recorded repository main advanced. It expects sibling `../app`, `../keygen`, and `../website` repos; use `--app-dir`, `--keygen-dir`, and `--website-dir` elsewhere. Inspect any main delta before updating the snapshots. `--allow-newer-main` checks the recorded snapshots deliberately without accepting newer behavior.

The [local consolidation report](maintenance/consolidation-2026-10-01.md) records the retained work and validation. The [V2 readiness audit](maintenance/v2-readiness-2026-10-01.md) updates the source baseline after reviewing consolidation. A final release/config delta and publication acceptance remain pending.

## Release boundary

The docs describe development capabilities. The banner and release page distinguish those from the public download and staged paid offer. Do not claim that a paid build or checkout is live based on source or a local preview. Committing, pushing, and publishing require their own authorization.

Maintenance evidence and scripts are excluded from public docs through `docs.json`. Historical image files remain in the repository, but the active guides do not use the old screenshots or animated mock UI. Replace them only with verified current imagery.

## Hosting

`docs.stenox.app` remains on Mintlify (`cname.mintlify-dns.com`), verified October 1, 2026. The website's Vercel-to-Cloudflare migration does not move these docs. Push and Mintlify publication remain separate authorized release actions.
