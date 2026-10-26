# Stenox documentation

Mintlify documentation for Stenox dictation, local models, meeting capture, and notes. Public pages are MDX; navigation, appearance, redirects, and branding live in `docs.json`. `style.css` extends Mintlify with the current website's warm surfaces and typography.

Public docs use “Stenox” as the product name and cover the trial, license setup and access, and app functionality. Reserve exact version numbers for release history, compatibility, model names, and upgrade instructions. Keep prices, discounts, promotional offers, and sales copy on the marketing website; do not duplicate them in public documentation.

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

For the prepared 2.3.0 candidate, use the separate audited input record and exact app manifest:

```sh
python3 scripts/check-docs.py --candidate-inputs maintenance/release-2.3.0-source.json --candidate-manifest /absolute/candidate-overlay-fix-2/release-manifest.json --app-dir /absolute/app-checkout --keygen-dir /absolute/keygen-checkout --website-dir /absolute/website-checkout
```

This route checks exact committed inputs, source-file hashes, prepared artifact hashes, catalogs, license terms, current controls, subscription setup and the approved changelog. It does not compare a release branch with unrelated local `main` heads. The historical published snapshot remains unchanged. `--allow-newer-main` cannot be combined with candidate validation; its historical checks do not establish candidate acceptance. Source validation does not establish native interaction, rendered docs, hosted publication or website deployment.

## Source of truth

See [the V2 readiness audit](maintenance/v2-readiness-2026-10-01.md) and [recorded snapshot](maintenance/source-snapshot.json). The [original refresh audit](maintenance/source-audit.md) preserves the earlier claim map and rendering evidence. App claims come from the recorded committed source, not uncommitted experiments or synthetic UI demos. Licensing terms are checked against the recorded app, keygen, and website commits. Website styling retains the consolidated theme. Model download sizes are catalog estimates, not RAM guarantees.

The current snapshot pins the published 2.3.3 app and its release tooling. It excludes the separately prepared 2.3.4 candidate until publication. The previous snapshot is retained in [source-snapshot-2.0.0.json](maintenance/source-snapshot-2.0.0.json).

### Historical 2.0 acceptance

The original snapshot pinned the published 2.0.0 app and release tooling to `b73e8fd`, including Keychain recovery, Personal notes context and canonical changelog links. The three public V2 artifacts match their approved hashes. The user confirmed the live Sparkle update from 1.1, installation and relaunch into 2.0.0; installed signature and executable match the frozen candidate. A separate saved-provider exercise was not observed, and no general OS Keychain guarantee is claimed. The user directed moving on; no repeated relaunch handoff is required. Separate popup/recording WIP is excluded, and the app checkout is not claimed clean.

`check-docs.py` checks current and legacy model IDs, license terms and UI labels, navigation and local targets. With `app_source_mode: published`, the app pin must match the recorded build/tooling commits, have publication acceptance and remain an ancestor of app main; later app work is excluded. Keygen and website pins must match their current mains. It expects sibling `../app`, `../keygen`, and `../website` repos; use `--app-dir`, `--keygen-dir`, and `--website-dir` elsewhere. Inspect any main delta before updating the snapshots. `--allow-newer-main` checks the recorded snapshots deliberately without accepting newer behavior.

The [local consolidation report](maintenance/consolidation-2026-10-01.md) preserves earlier work. The [current V2 audit](maintenance/v2-readiness-2026-10-01.md) records the published source, exact artifact and deployment evidence, human update result, and anonymous-trial verification: 18 live backend checks, 15 isolated checks, and a shared native SwiftPM DEBUG-service runner bound to the published licensing inputs. The native runner used an in-memory identity/store and production configuration; it was not a fresh-profile UI or Release-executable test. Historical candidates and site-only release states remain historical evidence.

## Release boundary

The public docs describe Stenox without versioned branding or pending-release notices. Source, deployment, human observations and test limitations remain separate in maintenance evidence. The existing release authority covers the requested download guidance update through origin/main without force: optional email submission permits occasional product updates and team check-ins, while X continues the download without an email. Review the final website source, run the unflagged source check, and verify the exact Mintlify deployment. The installation and privacy guidance has focused build, desktop/narrow and keyboard-link evidence in `docs-email-submit-consent-review.json`; unchanged pages retain their earlier rendering/search evidence.

Maintenance evidence and scripts are excluded from public docs through `docs.json`. Historical image files remain in the repository, but the active guides do not use the old screenshots or animated mock UI. Replace them only with verified current imagery.

## Hosting

`docs.stenox.app` remains on Mintlify (`cname.mintlify-dns.com`); the website uses Cloudflare separately. The canonical `/changelog` route is linked in the sidebar and footer. Origin is `git@github.com:GedeonIsezerano/stenox-docs.git`, branch `main`. Public-content commit `5c1bc1c` has live route, redirect, desktop/mobile and hosted-search evidence. Subsequent maintenance-only deployments are bound to exact SHAs by successful Mintlify GitHub App checks. Dashboard project/root metadata remains unverified and is not required to establish those deployments.
