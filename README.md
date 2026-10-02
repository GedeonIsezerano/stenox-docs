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

The snapshot records final intended app source `b73e8fd`, including explicit Keychain recovery at `8006345`, Personal notes context at `8de0e03`, and the canonical changelog links. The replacement signed candidate and actual macOS continuity acceptance remain separate internal gates. The older `bb165c2` and `8e46e4f` candidates are historical only. The V2 publication policy permits exactly the final V2 DMG, notes and appcast. An empty R2 bucket and a working site-only website do not establish V2 release acceptance.

`check-docs.py` checks current and legacy model IDs, license terms and UI labels, navigation, local targets, and whether a recorded repository main advanced. It expects sibling `../app`, `../keygen`, and `../website` repos; use `--app-dir`, `--keygen-dir`, and `--website-dir` elsewhere. Inspect any main delta before updating the snapshots. `--allow-newer-main` checks the recorded snapshots deliberately without accepting newer behavior.

The [local consolidation report](maintenance/consolidation-2026-10-01.md) records the retained work and validation. The [current V2 audit](maintenance/v2-readiness-2026-10-01.md) aligns Notetaker provider selection, Google access and per-operation payloads, explicit insight generation, provider switching, and onboarding preparation to app `b73e8fd`, including Personal notes and preparation questions in insight/refinement inputs. The earlier V1-to-V2 installation was user-confirmed through V1’s **Check for Updates**, establishing historical Sparkle migration success. The user denied the bb165c2 Keychain request and its UI subsequently worked; credential recovery remained incomplete. Replacement-candidate acceptance, actual GUI production trial/license and fresh Sparkle installation remain separate. Polar-originated delivery, paid fulfillment, and V2 publication remain pending. The Cloudflare site-only website is live with downloads unavailable and checkout closed; the coordinator also verified ordinary Chrome, macOS HTTPS and router DNS recovery.

## Release boundary

The public docs use release-ready V2 wording at the user's request, without pending-release notices. Actual source, candidate and deployment status remain in maintenance evidence. Do not infer that downloads or checkout are live from this copy or a local preview. The user has authorized production publication after the coordinator releases readiness gates; do not push or publish independently before that release.

Maintenance evidence and scripts are excluded from public docs through `docs.json`. Historical image files remain in the repository, but the active guides do not use the old screenshots or animated mock UI. Replace them only with verified current imagery.

## Hosting

`docs.stenox.app` remains on Mintlify (`cname.mintlify-dns.com`), verified October 1, 2026. The website's Vercel-to-Cloudflare migration does not move these docs. The canonical release-highlights route is `/changelog`, linked in the sidebar and footer. Git origin is `git@github.com:GedeonIsezerano/stenox-docs.git`, with default branch `main`. The remote was still at `32c5564` during publication inspection. Confirm the Mintlify production repository/branch and successful deployment in its dashboard before treating a push as published; that dashboard check currently needs sign-in. See the current readiness audit for the exact publication prerequisites.
