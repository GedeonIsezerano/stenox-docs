# V2 documentation readiness — October 1, 2026

The docs record the reviewed source and evidence below. V2 remains unpublished; the existing Vercel website still offers free V1.1. The user's revised release policy permits only the accepted V2 installer, notes and appcast in public release storage. Current owner evidence verifies candidate signing and production licensing smoke checks. Notarization, native trial/license acceptance, actual V1-to-V2 migration, Polar-originated webhook delivery, paid fulfillment and website hosting cutover remain incomplete.

## Reviewed baselines

| Repository | Commit | Review |
| --- | --- | --- |
| App / release tooling | `58583d57a7892ae1856e7ecfb45f9137e0517e64` | Publication-tooling-only delta from `8e46e4f`; native app/build inputs are unchanged. The signed candidate's original build source remains `8e46e4f400855354e07c2c1d848f77150fb86528`. |
| Keygen | `12c5f8f901782bd79f84dc01a17f6d83ab9c4bc2` | Documentation-only delta from `6d5b243` records verified `license.stenox.app` attachment and dedicated webhook URL change. Runtime source and API contract are unchanged. |
| Website | `c5e0b5dddbab661bf3f483da23c60eeb1264617c` | Delta from `93b8b61`: V2-only manifest, upload/acceptance guards, empty closed staging and reviewed historical-object cleanup. Commerce terms, the live Vercel version and local release originals are unchanged. |

All three local mains were clean and matched these commits at review. The combined snapshot is aligned after reviewing the final V2-only website implementation and exact cleanup evidence. It records `app_build_commit` separately from current `app_commit` and `release_tooling_commit`; the signed candidate has not been rebuilt. No source dependency remains at these revisions. `check-docs.py` detects later source drift; `--allow-newer-main` deliberately validates recorded commits only. Source alignment does not complete the release acceptance gates below.

## Delta and claim review

- `77577b9` restored full-app trial and paid access. `LicensingManager`, `LicensingService`, `LicensingSettingsContent`, onboarding, and new-work guards establish the trial/activation/verification flow. New dictation, file transcription, Polish, and meeting work are gated; saved history/export and ongoing work remain available.
- `5f756df` removed Gemma 3n 2B/4B, normalized unsupported local selections, and repaired local runtime/checkpoint lifecycle handling. Current active model IDs are unchanged. The legacy table now contains only Qwen 2.5 1.5B, Phi-3 Mini, and Qwen 3 4B. The documentation checker compares the entire legacy ID set, so removed entries cannot silently remain documented as supported.
- `9f16e2e` fixes provider ownership when activating a completed local-model download and removes obsolete audit files. Existing download/select/readiness guidance remains applicable.
- `f7d017f` preserves isolated demo data and research. Demo controls are not documented as customer features or release acceptance.
- App `8e46e4f` sets version 2.0.0, describes the optional paid upgrade, and requires the production licensing issuer/audience in release configuration. Packaging retains the bundle ID, Sparkle feed and public key and marks V2 as a major upgrade. Its original policy of retaining V1 feed entries is superseded by `58583d5`, which emits only the accepted V2 item. Candidate signing is verified separately below; notarization remains pending. Synthetic V1 history compatibility tests do not establish actual migration.
- App tooling `58583d5` changes only the release script, its tests and release notes for operators. The feed title is **Stenox 2.0.0 — optional major upgrade**, with existing paid-key rights preserved. Resume accepts only descendant changes in the explicit release-metadata allowlist; changes to native code, resources, version or build inputs require a new candidate. The completed manifest retains the original app `sourceSHA`, adds the exact `releaseToolingSHA`, and records `publicationPolicy: candidate-only`. The app owner reports 16 focused release-tool tests passing; the signed candidate was not rebuilt.
- Keygen `9c78121` adds isolated staging/production configuration, guarded cloud preparation and deployment, and read-only legacy eligibility verification. `API_CONTRACT.md` and `src/` have no delta from the prior reviewed baseline, so the documented trial, refresh, offline window and allowance behavior remain applicable.
- Website `85a0708` adds V2 offer names/campaign metadata without changing prices or purchase terms. The Cloudflare build accepts `--offer=standard` for the manual standard-price transition; deployment derives the offer and flags from the verified build marker and selects the matching checkout-link secret. Defaults keep paid visibility and checkout closed. `lib/constants.ts` and `public/updates/` are unchanged. Cloudflare privacy/hosting wording belongs to the prepared website source and is not evidence of public cutover; the docs hosting guidance remains Mintlify.
- Keygen `6d5b243` adds a narrowly guarded custom-domain configuration: only `license.stenox.app` in the `stenox.app` zone, with no wildcard/path/extra host or staging route. It preserves the working `workers.dev` endpoint used by the signed candidate. Documentation-only commit `12c5f8f` records the subsequent deployment, custom-host acceptance and dedicated webhook URL change. No runtime or customer-contract change requires a public guide edit.
- Website `93b8b61` added full-download verification for the former historical-release migration plan; the 119-file publication requirement is now superseded by the V2-only decision below. Its exact `www.stenox.app` redirect preserves existing 307 behavior to the HTTPS apex, with paths and queries retained except private checkout-return queries. Worker-first routing covers static assets, and the deployment guard permits only the apex and explicit `www` custom domains.
- Website `c5e0b5d` replaces the historical manifest with schema 2, `pending`, no current version and zero files. The Worker removes the Vercel download bridge and serves no release assets until an accepted V2 manifest exists. Accepted manifests require exactly DMG, notes and appcast; upload and production deployment require matching final app provenance, artifact/evidence hashes and release acceptance. The uploader validates the final Sparkle signature and macOS signing/stapling/Gatekeeper evidence before uploading, with the feed last. These controls remain closed for the current unnotarized candidate.

| Customer guidance | Source or authority |
| --- | --- |
| Seven-day full-app trial, explicit online start, no account/card, fixed deadline | App licensing models/manager and onboarding; keygen `API_CONTRACT.md` and `src/service.ts` trial issuance. |
| New two-Mac licenses; valid earlier paid licenses cover V2 without repurchase and retain original rights/allowance | User's explicit V2 entitlement decision, relayed by the coordinator; website/app allowance wording; Worker preserves the provider's actual `l.limit` and rejects inactive/revoked/expired grants. This does not promise access from refunded licenses. |
| Weekly paid refresh and up to 30 days offline | Worker `paid()` sets refresh at seven days and expiry at 30 days, capped by any underlying grant expiry. Native signed-credential checks enforce the deadline. |
| Temporary failures preserve the existing deadline; authoritative invalidity can block new work | Native `LicensingManager.perform`, `LicensingFailure.revokesExistingActivation`, and Worker/provider error handling. |
| Device change or lost Keychain identity | Native deactivation clears paid access after server success; Worker operations document new-key activation and releasing the old slot. No Keychain deletion is prescribed. |
| Provider credential recovery | App `KeychainService` scopes credentials to the app and preserves existing values on unsuccessful updates; API Keys and Notetaker settings own re-entry/reconnection. |
| Publisher | GKI Software Inc., formerly Sophosia Software Inc.; candidate bundle/archive verification records Developer ID Application: Sophosia Software Inc., Team VWXR46VR26. The candidate is signed but unnotarized and unpublished. |
| Permission and Keychain reauthorization | Existing app permission flow and Apple's current support guidance linked in the upgrade guide. No live user permissions or credentials were modified. |

The Worker admits entitlements through explicit organization/benefit allowlists, including the reviewed Lifetime, Lifetime Plus and current granted Plus benefits. The licensing owner's evidence reports that both existing production Lifetime records passed the actual provider normalization and eligibility functions, first using redacted read-only records and then the production Polar GET API. Each retains three Macs and no expiry. Before/after reads reported unchanged keys, rights, usage, activation lists and validation metadata; zero customer activations occurred. This establishes reviewed mapping and code compatibility for those records, not live customer activation acceptance.

The licensing evidence records 11 successful staging checks, seven production `workers.dev` checks, and seven custom-host checks after deployment of Worker version `30024785-dfe5-487b-814f-d708557f046f` from `6d5b243`. `licensing-custom-domain-cloudflare-readback.json` confirms the exact attached hostname, retained `workers.dev`, D1 and secret bindings. `licensing-custom-domain-cloud-results.json` covers health, signed trial/deadline behavior, proof/replay rejection, unavailable local controls, invalid-license handling and forged-webhook rejection.

The dedicated Polar webhook now uses `https://license.stenox.app/webhooks/polar`; its enabled state, secret, API version and event subscriptions were preserved. `licensing-custom-domain-webhook-acceptance.json` records operator-signed synthetic reconciliation for both existing licenses; original and duplicate deliveries returned 200 without changing provider rights or activations. Zero customer activations occurred. These events were not sent by Polar: Polar-originated delivery remains unverified.

Custom-host acceptance initially used addresses from Google DNS-over-HTTPS with the original Host/SNI and normal certificate/hostname verification while the Mac's ordinary resolver still returned a stale Vercel 404. The later `website-pre-origin-cutover-dns.json` records ordinary-Mac HTTPS health returning 200 with `{ "ok": true }`, resolving that observed local-cache limitation. It also records the Cloudflare nameserver pair and preserved mail, Mintlify docs and API routing. This is endpoint health and DNS evidence, not native license activation or Polar-originated delivery acceptance.

The coordinator's `coordinator-production-license-readback.json` confirms healthy backend response and equality of all six bundled licensing fields: base URL, issuer, audience, signing key ID, signing public key and verification keys. The subsequent custom-domain readback preserves that configuration and signing identity. This verifies the signed candidate's public configuration against the deployed backend, not a native trial or license activation. The candidate has not been launched or activated and still uses the retained `workers.dev` base URL.

## In-app upgrade path clarification

The intended normal V1-to-V2 path is the existing Sparkle updater; manual download is a fallback. App `UpdateManager.swift` owns the Sparkle controller, and `MenuBarView.swift` exposes **Check for Updates...**, replaced by **Restart to Update** when a pending update is ready. The customer guide describes the update prompt and menu actions without requiring every user to download a DMG again.

The coordinator's `sparkle-continuity.json`, read from `/Users/home/.codex/qa-artifacts/stenox/v2-readiness-20261001/`, reports successful Ed25519 verification of the published V1.1 archive and a retained-key signing challenge against the retained public key. It records V1.1 DMG SHA-256 `03fa5529db5924c6a1a77793f7a92a808e7c9db4fabd8aca433d860e1005d002`, with no private-key export. This establishes signing-key continuity evidence, not successful end-to-end delivery/install of V2 or data, permission, and Keychain migration. Those acceptance gates remain open until release evidence arrives.

The app owner's `candidate-bundle-verification.json` and `candidate-archive-verification.json` now record complete Developer ID signing, including nested code, hardened runtime and Team `VWXR46VR26`. The signed upload DMG is 279,396,987 bytes, SHA-256 `354c36fa9c5012dd9c9eb17ba60bd5be3e3c9cfbf7568bbeb9668baf3260e989`; `candidate-sparkle-proof.json` verifies its Ed25519 signature against the retained public key. This is the unnotarized upload, not a final public artifact. `app-readiness.json` reports that the `stenox-v2-notary` profile is absent, no submission or stapling occurred, and the actual V1-to-V2 installation remains untested. A final stapled DMG requires its own verification and Sparkle signature.

The coordinator independently rehashed the signed upload after the policy change. `coordinator-v2-only-signed-checkpoint.json` confirms the same SHA-256, original app source `8e46e4f`, release-tooling source `58583d5`, checkpoint phase `signed`, and no final release manifest. Publication-tooling changes did not alter the signed candidate.

## V2-only publication plan

The authorized storage policy is exactly three public release assets for the accepted V2 candidate:

| Public path | Required artifact |
| --- | --- |
| `/updates/Stenox-2.0.0.dmg` | Final notarized, stapled and verified V2 installer, with its final Sparkle signature. |
| `/updates/Stenox-2.0.0.html` | Approved V2 release notes. |
| `/updates/appcast.xml` | Signed-enclosure feed containing only the accepted V2 item, titled **Stenox 2.0.0 — optional major upgrade**. |

There is no public historical-installer or V1 fallback requirement. The existing Sparkle feed URL and trusted key remain unchanged so an installed V1 can discover V2. An installed V1 remains usable, but this policy does not promise continued public V1 downloads. Preserve the manual **V2** download route if the updater cannot offer or complete the upgrade, and keep the V1.1 installer locally as the isolated upgrade-test fixture.

Keep `base-appcast.xml`, licensing configuration, signed preparation upload, manifests and test fixtures as local release evidence; they are not additional public release assets. The final manifest must distinguish the unchanged app build SHA `8e46e4f400855354e07c2c1d848f77150fb86528` from release-tooling SHA `58583d57a7892ae1856e7ecfb45f9137e0517e64`, with `publicationPolicy: candidate-only`. Do not publish the unnotarized upload or infer final acceptance from the 16 passing tooling tests.

The website owner's `website/r2-historical-cleanup-verification.json` confirms deletion of the 119 exact task-created historical objects, with zero historical keys and zero objects remaining. The bucket, local originals and Vercel were preserved. Cleanup is complete; this docs task performed no storage deletion. The deployed V2-only staging manifest is empty, so no V2 assets have been uploaded. After release acceptance and publication authority, verify the three final objects against the approved manifest and verify that historical paths remain unavailable. The public website remains on Vercel until a separately accepted origin cutover.

## Public availability and hosting

Read-only checks on October 1 found:

- `https://stenox.app/download` offers free V1.1 and says that build does not require a license.
- `docs.stenox.app` resolves through CNAME `cname.mintlify-dns.com` and returns HTTP 200 with Mintlify proxy/client headers. Its rendered footer identifies Mintlify hosting.
- Response headers also mention Vercel, which is part of the observed serving path; this does not make the docs a website-project deployment to migrate. The docs domain stays on Mintlify. This docs task changed no DNS or hosting settings.

The docs banner, home, installation, release/access, and new upgrade guide retain the V2-unpublished boundary. Website Cloudflare migration status is not represented as complete.

The prior historical-download staging plan is superseded. The website owner's current handoff records staging commit `c5e0b5d`, Worker version `daee5c80-915f-4bd6-a0bb-a6d571b5de05`, 15 focused tests and a matching build passed, and remote checks confirming old DMG/notes/appcast and unaccepted V2 paths return 404 without release bytes or redirects. An independent bucket listing reports zero objects. This is closed-state acceptance, not acceptance of a V2 download. The staging marketing/download presentation still reflects V1 and must be aligned to the final accepted V2 version before production attachment. The live Vercel homepage and V1.1 DMG remain available; customer MDX describing that current public state is unchanged.

The coordinator's `cloudflare-dns-ui-comparison.json` records all 18 original DNS records preserved in the Cloudflare editor, including the Mintlify docs CNAME, with TTL 60 and DNS-only routing. The registrar accepted the nameserver change; its UI confirms `hassan.ns.cloudflare.com` and `rayne.ns.cloudflare.com`. The coordinator subsequently confirmed the Cloudflare zone active through its API and the same nameserver pair through Google DNS-over-HTTPS. `dns-cutover-continuity.json` records 18/18 continuity checks passed. This replaces the earlier propagation-pending status; it does not imply every local resolver has refreshed.

`vercel-license-transition-readback.json` records one added `license` CNAME to the production `workers.dev` hostname in the old Vercel DNS zone, for clients retaining cached Vercel delegation. Its readback confirms all 18 original records unchanged. Apex and wildcard records still target Vercel; website-origin cutover remains separate from DNS continuity and must follow the V2-only release plan. The earlier `dig` comparison remains non-authoritative because responses lacked the authoritative-answer flag. DNS continuity is not authenticated mail-delivery acceptance or website-origin migration.

## Validation

Mintlify 4.2.964 build validation, broken-link check, and MDX media accessibility check pass. The existing color advisory remains: primary-on-light 5.28:1 meets AA, while the CLI recommends AAA. This is not full accessibility certification.

The initial `python3 scripts/check-docs.py` run passed against the recorded repository mains: 42 MDX files, 38 navigation pages, 122 local links/assets, exact active/legacy model IDs, licensing term constants, original device-allowance preservation, and License UI action names. `git diff --check` passes.

During the focused upgrade-path clarification, the strict check correctly reported that repository mains had advanced; the recorded-source check with `--allow-newer-main` passed. Those earlier dependencies were resolved in the preceding three-repository review; the newer V2-only policy follow-up is tracked above. Build, links, whitespace, and 1440/320 px rendered checks passed for the clarification, with no page overflow or captured console errors. Follow-up logs use the `docs-upgrade-` prefix in the evidence directory.

The baseline and evidence updates change only the README and maintenance records; customer MDX, navigation and styling are unchanged from that rendered check. Strict source, Mintlify validation, broken-link and whitespace checks for the preceding baseline use the `docs-baseline-final-` prefix. The production-evidence refresh used `docs-evidence-refresh-`; the custom-domain update used `docs-domain-refresh-`. V2-only plan checks use `docs-v2-only-plan-`; final strict source, broken-link and whitespace checks use `docs-v2-only-final-` after the combined snapshot update. Unchanged public pages reuse the prior build and rendered evidence.

Rendered local checks cover the upgrade guide at 1440 × 1000 and its permission table at 320 × 740. Page width matches viewport width. The permission table scrolls within its own wrapper; keyboard Right moved it 40 px. Mobile navigation opens Release and access, and its 320 px dark layout renders correctly. A rendered price check caught unescaped dollar signs being parsed as math; both currency amounts were escaped and verified as ordinary text. Browser console errors were not observed during the final checks.

Evidence is in `/Users/home/.codex/qa-artifacts/stenox/v2-readiness-20261001/`, including build/source/link/accessibility logs, DNS/HTTP headers, responsive screenshots, and `docs-browser-checks.json`. The coordinator handoff is `docs-readiness.json` in that directory.

## Safe worktree cleanup

The missing `/private/tmp/stenox-docs-free` registration was pruned after verifying: its branch is an ancestor of main, no staged index delta remains, the directory is absent, the registration is unlocked, every metadata file matches the verified pre-consolidation archive, and the dry run names only this registration. The `codex/free-1.0-docs` branch remains at `50f063a3941d611e3ab80e673835c9584886adeb`. Full Git objects and metadata remain in the archive recorded by the consolidation report. No live worktree, persistent customer data, or preview process was removed.

## Publication requirements

1. Re-audit any source changes after the recorded commits, preserving the distinction between the signed app build SHA and release-tooling SHA. The V2-only source alignment and historical R2 cleanup review are complete.
2. Complete notarization/stapling and verification of the final public artifact, plus actual V1-to-V2 installation, data, permission and Keychain recovery before changing migration-status claims.
3. Complete native trial/existing-license activation, Polar-originated webhook delivery, compatible paid app acceptance and checkout fulfillment before removing the staged-offer notices. Preserve the reviewed original purchase rights and allowances. Backend smoke and synthetic reconciliation have passed; they do not close these gates.
4. Publish only the three accepted V2 assets listed above after release acceptance and publication authority; verify their hashes, single-item feed and unavailable historical paths. Retain the local V1 test fixture and manual V2 updater-failure fallback.
5. Obtain explicit authority to push/publish this docs commit, confirm the Mintlify repository/branch connection, then verify hosted routes, redirects, responsive rendering, and search. Local preview does not verify hosted search.
6. Leave `docs.stenox.app` on Mintlify when the separate website moves to Cloudflare.
