# V2 documentation readiness — October 1, 2026

The docs are prepared locally against the consolidated source below. V2 remains unpublished; free V1.1 remains the public download. This audit does not establish successful V1-to-V2 migration, release signing/notarization, production licensing fulfillment, paid checkout availability, or a website hosting cutover.

## Reviewed baselines

| Repository | Commit | Review |
| --- | --- | --- |
| App | `f7d017fc7840c83abd60e9260555d134fdee9b2e` | Delta from prior docs snapshot `9545cffb2f19f5677a98c6801cd6c0504c3d170a`, plus licensing and migration source. |
| Keygen | `1395836e27f6972a3c76b9ff3fcc950960583455` | Custom Worker/D1 implementation, API contract, provider allowance handling, and operational limits. |
| Website | `3c2f69dddf3633b3145e327d8ce7bf7d06d455e7` | Committed offer/trial/device terms in `lib/commerce.ts`; retained consolidated theme. |

The source snapshot was advanced only after review. The final app release/config SHA remains a coordinator dependency; re-audit its delta before declaring release alignment. `check-docs.py` now detects drift in all three repository mains. `--allow-newer-main` deliberately validates recorded commits only.

## Delta and claim review

- `77577b9` restored full-app trial and paid access. `LicensingManager`, `LicensingService`, `LicensingSettingsContent`, onboarding, and new-work guards establish the trial/activation/verification flow. New dictation, file transcription, Polish, and meeting work are gated; saved history/export and ongoing work remain available.
- `5f756df` removed Gemma 3n 2B/4B, normalized unsupported local selections, and repaired local runtime/checkpoint lifecycle handling. Current active model IDs are unchanged. The legacy table now contains only Qwen 2.5 1.5B, Phi-3 Mini, and Qwen 3 4B. The documentation checker compares the entire legacy ID set, so removed entries cannot silently remain documented as supported.
- `9f16e2e` fixes provider ownership when activating a completed local-model download and removes obsolete audit files. Existing download/select/readiness guidance remains applicable.
- `f7d017f` preserves isolated demo data and research. Demo controls are not documented as customer features or release acceptance.

| Customer guidance | Source or authority |
| --- | --- |
| Seven-day full-app trial, explicit online start, no account/card, fixed deadline | App licensing models/manager and onboarding; keygen `API_CONTRACT.md` and `src/service.ts` trial issuance. |
| New two-Mac licenses; valid earlier paid licenses cover V2 without repurchase and retain original rights/allowance | User's explicit V2 entitlement decision, relayed by the coordinator; website/app allowance wording; Worker preserves the provider's actual `l.limit` and rejects inactive/revoked/expired grants. This does not promise access from refunded licenses. |
| Weekly paid refresh and up to 30 days offline | Worker `paid()` sets refresh at seven days and expiry at 30 days, capped by any underlying grant expiry. Native signed-credential checks enforce the deadline. |
| Temporary failures preserve the existing deadline; authoritative invalidity can block new work | Native `LicensingManager.perform`, `LicensingFailure.revokesExistingActivation`, and Worker/provider error handling. |
| Device change or lost Keychain identity | Native deactivation clears paid access after server success; Worker operations document new-key activation and releasing the old slot. No Keychain deletion is prescribed. |
| Provider credential recovery | App `KeychainService` scopes credentials to the app and preserves existing values on unsuccessful updates; API Keys and Notetaker settings own re-entry/reconnection. |
| Publisher | Coordinator-supplied identity: GKI Software Inc., formerly Sophosia Software Inc.; expected Apple signing display Sophosia Software Inc., Team VWXR46VR26. This is not a new release-artifact signature check. |
| Permission and Keychain reauthorization | Existing app permission flow and Apple's current support guidance linked in the upgrade guide. No live user permissions or credentials were modified. |

The Worker admits entitlements through explicit organization/benefit allowlists. The source preserves an admitted license's original allowance; it does not prove every historical purchase has been admitted to production. Production release-family mapping and original purchase-rights review remain release requirements. Sandbox evidence in the keygen repository is distinct from production acceptance.

## In-app upgrade path clarification

The intended normal V1-to-V2 path is the existing Sparkle updater; manual download is a fallback. App `UpdateManager.swift` owns the Sparkle controller, and `MenuBarView.swift` exposes **Check for Updates...**, replaced by **Restart to Update** when a pending update is ready. The customer guide describes the update prompt and menu actions without requiring every user to download a DMG again.

The coordinator's `sparkle-continuity.json`, read from `/Users/home/.codex/qa-artifacts/stenox/v2-readiness-20261001/`, reports successful Ed25519 verification of the published V1.1 archive and a retained-key signing challenge against the retained public key. It records V1.1 DMG SHA-256 `03fa5529db5924c6a1a77793f7a92a808e7c9db4fabd8aca433d860e1005d002`, with no private-key export. This establishes signing-key continuity evidence, not successful end-to-end delivery/install of V2 or data, permission, and Keychain migration. Those acceptance gates remain open until release evidence arrives.

## Public availability and hosting

Read-only checks on October 1 found:

- `https://stenox.app/download` offers free V1.1 and says that build does not require a license.
- `docs.stenox.app` resolves through CNAME `cname.mintlify-dns.com` and returns HTTP 200 with Mintlify proxy/client headers. Its rendered footer identifies Mintlify hosting.
- Response headers also mention Vercel, which is part of the observed serving path; this does not make the docs a website-project deployment to migrate. The docs domain stays on Mintlify. No DNS or hosting settings were changed.

The docs banner, home, installation, release/access, and new upgrade guide retain the V2-unpublished boundary. Website Cloudflare migration status is not represented as complete.

## Validation

Mintlify 4.2.964 build validation, broken-link check, and MDX media accessibility check pass. The existing color advisory remains: primary-on-light 5.28:1 meets AA, while the CLI recommends AAA. This is not full accessibility certification.

The initial `python3 scripts/check-docs.py` run passed against the recorded repository mains: 42 MDX files, 38 navigation pages, 122 local links/assets, exact active/legacy model IDs, licensing term constants, original device-allowance preservation, and License UI action names. `git diff --check` passes.

During the focused upgrade-path clarification, app main advanced to `8e46e4f400855354e07c2c1d848f77150fb86528`. The strict check now reports that source dependency; the recorded-source check with `--allow-newer-main` passes. The snapshot remains unchanged pending the final app SHA. Build, links, whitespace, and 1440/320 px rendered checks passed again for the clarification, with no page overflow or captured console errors. Follow-up logs use the `docs-upgrade-` prefix in the evidence directory.

Rendered local checks cover the upgrade guide at 1440 × 1000 and its permission table at 320 × 740. Page width matches viewport width. The permission table scrolls within its own wrapper; keyboard Right moved it 40 px. Mobile navigation opens Release and access, and its 320 px dark layout renders correctly. A rendered price check caught unescaped dollar signs being parsed as math; both currency amounts were escaped and verified as ordinary text. Browser console errors were not observed during the final checks.

Evidence is in `/Users/home/.codex/qa-artifacts/stenox/v2-readiness-20261001/`, including build/source/link/accessibility logs, DNS/HTTP headers, responsive screenshots, and `docs-browser-checks.json`. The coordinator handoff is `docs-readiness.json` in that directory.

## Safe worktree cleanup

The missing `/private/tmp/stenox-docs-free` registration was pruned after verifying: its branch is an ancestor of main, no staged index delta remains, the directory is absent, the registration is unlocked, every metadata file matches the verified pre-consolidation archive, and the dry run names only this registration. The `codex/free-1.0-docs` branch remains at `50f063a3941d611e3ab80e673835c9584886adeb`. Full Git objects and metadata remain in the archive recorded by the consolidation report. No live worktree, persistent customer data, or preview process was removed.

## Publication requirements

1. Receive the final app release/config SHA and re-audit its delta; likewise review any changed backend contract or website terms before updating snapshots.
2. Obtain release evidence for signing/notarization and actual V1-to-V2 data, permission, and Keychain recovery before changing migration-status claims.
3. Confirm production entitlement mapping, licensing service/configuration, compatible paid app, and checkout fulfillment before removing the staged-offer notices. Preserve original purchase rights and allowances.
4. Obtain explicit authority to push/publish this docs commit, confirm the Mintlify repository/branch connection, then verify hosted routes, redirects, responsive rendering, and search. Local preview does not verify hosted search.
5. Leave `docs.stenox.app` on Mintlify when the separate website moves to Cloudflare.
