# V2 documentation readiness — October 1, 2026

The docs describe committed development source, not a published V2 release. The fresh candidate from current app source `bb165c264a785c798d5356b500fc5d3f63499fa1` is prepared, Apple Accepted, stapled, Gatekeeper accepted and Sparkle verified. The app process launched but awaits the user’s macOS Keychain approval before its window opens; actual rendered GUI acceptance remains pending. The earlier notarized candidate from `8e46e4f` lacks the new native changes and is superseded for release; its evidence remains historical only.

The coordinator reports the earlier V1-to-V2 in-app installation as user-confirmed. The Others-account test-kit workflow is no longer required; its launchers were removed at the user's request. Fresh Sparkle installation and actual GUI production trial/existing-license acceptance are separate gates. Cloudflare site-only recovery is complete, with downloads unavailable and checkout closed; the coordinator has also confirmed ordinary Chrome, macOS HTTPS and router DNS recovery.

## Reviewed source

| Repository | Reviewed commit | Scope |
| --- | --- | --- |
| App | `bb165c264a785c798d5356b500fc5d3f63499fa1` | Includes `70291a1` Parakeet onboarding preparation and the consolidated Notetaker capture, manual generation, provider switching and Google-derived context changes. Fresh candidate source is this commit. |
| Keygen | `12c5f8f901782bd79f84dc01a17f6d83ab9c4bc2` | Unchanged contract; documentation records deployed custom licensing host. Production runtime was deployed from `6d5b243`. |
| Website | `d5aee747e50e23725dd81e4d6542e2fbda661227` | Adds source-aligned meeting, FAQ, privacy and terms disclosures after the `4375ae1` recovery runbook. Commerce terms and release controls are unchanged. Deployed code remains separately recorded as `359e9fd`; the new copy is not assumed published. |

Source inspection used clean committed app files and the app owner's `app-notetaker-provider-handoff.json`. The website's earlier `website/calendar-provider-copy-audit.json` identified stale claims but observed uncommitted app work; that earlier observation is superseded by the committed handoff. All source paths below are relative to the app repository at `bb165c2`.

`maintenance/source-snapshot.json` records candidate source separately from candidate acceptance and the superseded source. `check-docs.py` checks current repository mains; re-audit any later source delta before advancing that snapshot. Source alignment does not imply release acceptance.

## Notetaker source and claim map

| Area | Current evidence and documentation |
| --- | --- |
| Provider catalog | `NotetakerInsightProvider.swift` exposes On-device, Codex, Claude Code and Google Antigravity. Available model IDs come from each runtime, not a fixed marketing list. On-device uses the independent Qwen 3.5 4B brief model. |
| Google-derived context | `NotetakerBriefService.swift` no longer blocks selected cloud providers at update, refinement or Ask. Provenance keys remain; removing an event does not erase derived saved content. Calendar, processing, privacy and setup guides now disclose the selected-provider behavior. |
| Google permission | `NotetakerCalendarOAuth.swift` requests only `https://www.googleapis.com/auth/calendar.events.readonly`. `NotetakerCalendarHTTP.swift` uses the primary alias and user-entered Calendar IDs, with no calendar-list enumeration or Google profile identity request. The connection uses a local UUID and blank name/email; event organizer/attendee names and emails can still be read. |
| Fetched event fields | `NotetakerCalendarHTTP.swift` restricts selected-calendar/date-window queries with an explicit field selector. Events can include title, description, times, location, links, organizer/attendee details, recurrence identifiers and attachment metadata. This is broader than the model's bounded calendar context. |
| Manual controls | `NotetakerSessionInsightsView.swift` provides Generate insights and the Insights model popover during capture and editable history. The popover includes Automatic insights and provider/model/reasoning controls. Manual generation needs one contribution; scheduled reviews need two. Turning automatic reviews off preserves the ledger and does not disable explicit generation. |
| Switching | `NotetakerManager.swift` cancels pending work and uses revision checks to reject old results. Capture and accepted/user-edited outcomes remain. Provider-owned sign-ins are retained; switching to On-device does not recall earlier transfers. No new per-request consent dialog or automatic provider failover is implemented. |
| Onboarding | `OnboardingSetupView.swift` automatically prepares the selected local speech model on appearance, selection changes and provider readiness. Missing files download and cached files load; preparation failures expose Try again. `PinnedParakeetModelLoader.swift` uses the fixed model revision and correct compiled cache handling. |
| Capture recovery | `NotetakerCapture.swift` detects missing microphone buffers rather than silence or absent words. `NotetakerManager.swift` checkpoints completed text and attempts bounded capture recovery, displaying Reconnecting audio. Repeated failure becomes an interrupted session. Physical headphone/device recovery is not proven by the synthetic tests. |

The exact source paths are under `Stenox/Services/Notetaker/`, `Stenox/Managers/`, `Stenox/Views/Notetaker/`, `Stenox/Views/Onboarding/`, and `Stenox/Services/Transcription/Providers/`. Public guides retain hidden Outlook status, independent speech/insight choices, explicit reference import, and no automatic Drive attachment download.

## Per-operation processing boundary

- **Automatic and manual insights:** bounded changed/recent conversation, speaker IDs/names, current outcomes, new contribution IDs, elapsed duration, included reference text, and selected-event context. `NotetakerCalendar.insightContext` bounds the title to 500 characters, agenda to 6,000, organizer name to 120, and up to 100 participant names to 120 each, with scheduled start/end and time zone. Dedicated email, location, event URL, join-link and attachment-link fields are excluded. Free-form text is not a personal-information filter.
- **Refine notes:** session title and title-generation flag, accepted visible outcomes with owner names/dates/status, and included references. It does not independently append the transcript or full event snapshot.
- **Ask:** question, session title, bounded selected conversation with speaker labels, included references, and up to three previous question/answer pairs. It does not independently append the full event snapshot.
- **Continued context:** Codex and Claude Code may retain provider context across these operations for the same session/selection. Antigravity resends context for each request. Calendar-derived titles or other saved information can remain in inputs after event removal. The Personal notes field is excluded; copies placed into another input can be processed there.

App source and tests establish neither recipient retention/training guarantees nor Google review approval. The documentation makes no such claim. Provider account terms remain separate. The existing provider explanation now names transcript and included calendar/reference context; choosing a provider is not documented as a new consent screen.

## App evidence and remaining acceptance

The app owner's handoff reports 861 full Swift tests, 93 focused tests, and native preview checks at compact 559 pt and wide 756 pt widths. Preview checks exercised Generate with automatic insights off, switching provider/model and returning local, using synthetic accounts and responses. These checks do not establish live provider transfer, live Google-derived native transfer, physical headphone recovery, or GUI production licensing acceptance. This docs task did not rerun native app tests.

The fresh `candidate-2.0.0-bb165c2/release-manifest.json` binds both app and release-tooling source to `bb165c2`, with `candidate-only` and `published: false`. Its SHA-256 is `6115421a7d781fbc85ddd3d618b554183790f66f2e1654ccefe574238691ae43`. Apple submission `c3d0ead3-6c59-48e6-83d5-bceec5097a19` is Accepted. The owner logs confirm staple validation, Gatekeeper acceptance and retained-key Ed25519 verification. `coordinator-fresh-candidate-verification.json` independently confirms strict deep codesign, Team/bundle/feed/key continuity, all manifest hashes and production licensing configuration. The docs independently rehashed the manifest and all five listed local files in `docs-provider-alignment-artifact-hashes.json`.

| Fresh public candidate | SHA-256 |
| --- | --- |
| `Stenox-2.0.0.dmg` (279,326,902 bytes) | `1fb8b3e52ed8c8cbff9875c4aab5411ddbb5239b009ab70580b8c4fcb67ee895` |
| `Stenox-2.0.0.html` | `9d885cb00e764d3360cbb11293c7f85e032d1fe7892a223ac7d2c931e9540a9b` |
| `appcast.xml` | `b57ca51da603366e22ed148800cfe5ff874b833004a1c686541b850c39b229c6` |

These files are not publicly released. GUI production licensing and a fresh Sparkle install remain unaccepted in the coordinator verification. `candidate-bb165c2-native-acceptance.json` records the launched process waiting on macOS authorization for the existing API-key ACL migration. The user must handle that protected system prompt directly. The process was retained without repeated restarts, credential export or Keychain deletion; launch alone does not establish rendered app acceptance. The old `candidate-2.0.0/` manifest and `app-final-candidate.json` still refer to `8e46e4f` and must not be used as the current candidate reference.

For historical provenance, the superseded candidate used app source `8e46e4f400855354e07c2c1d848f77150fb86528` and release tooling `58583d57a7892ae1856e7ecfb45f9137e0517e64`. Apple submission `2f1b114e-1be1-4d4a-b014-a5b5170a0cc5` was Accepted; stapling, Gatekeeper and the final retained-key Sparkle signature passed. The final old DMG hash was `6d66d7a050815d741c2f5852b906f33e5f9476381912b6c9f61c2be8a6c37ae4`. The docs independently matched its three artifact hashes and manifest in `docs-notarized-recovery-artifact-hashes.json`. Those checks do not cover `bb165c2`.

The legal identity remains GKI Software Inc., formerly Sophosia Software Inc. Historical Developer ID evidence identifies Sophosia Software Inc., Team `VWXR46VR26`; no legal or licensing terms changed in this alignment.

## Licensing and publication

The full-app trial is seven days with explicit online start and no account/card. New paid licenses cover two Macs; valid earlier paid licenses retain original rights/allowances and cover V2 without repurchase. Inactive, refunded, revoked or expired licenses do not qualify. Paid verification refreshes weekly, with up to 30 days offline since successful verification, capped by underlying expiry. Temporary failures do not extend deadlines. Saved history/export and ongoing work remain available when new work is gated.

Production licensing Worker version `30024785-dfe5-487b-814f-d708557f046f` passed seven workers.dev and seven custom-host checks. `license.stenox.app` is attached and healthy; the dedicated webhook uses `https://license.stenox.app/webhooks/polar`. Both existing Lifetime records retained three Macs and no expiry through read-only eligibility and synthetic duplicate-webhook reconciliation. Zero customer activations occurred. Polar-originated delivery and actual GUI trial/existing-license activation remain unverified. The coordinator's fresh-candidate verification confirms its licensing configuration matches the live backend; configuration equality is not GUI activation acceptance.

The publication policy remains **candidate-only**: exactly `/updates/Stenox-2.0.0.dmg`, `/updates/Stenox-2.0.0.html`, and `/updates/appcast.xml`. The single-item feed keeps the existing URL/trusted key and optional-major-upgrade framing. Retain the manual V2 download fallback; installed V1 remains usable, without a promise of public V1 installers. Manifests, signing uploads, licensing configuration and test fixtures stay local.

The 119 exact task-created historical R2 objects were removed in the earlier authorized cleanup, and the bucket was verified empty. No V2 assets are published. The older test kit is not a current release prerequisite. Fresh artifact verification, native acceptance, release-note review, hash-bound publication authority, upload verification, and paid fulfillment remain separate from the user-confirmed earlier upgrade.

## Hosting state

Website code `359e9fd8aabbf729b4c818c527cab41e461ef603` is deployed as Cloudflare Worker version `6e8b9225-9d23-461c-962f-fa3efe8bd64d`, with apex and www enabled. The owner/coordinator evidence reports public TLS/HTTP acceptance, apex 200, www 307, desktop/mobile rendering, disabled installer buttons, no old feed, and closed checkout (POST redirects unavailable; GET rejects the method). The later `ad859e2` and `4375ae1` commits record recovery and DNS transition; they do not change deployed code. Site-only publication is complete; V2 downloads and checkout remain closed.

The conflicting original apex CNAME is already absent; no further deletion is requested here. The coordinator diagnosed this Mac/router's stale Vercel answers and added apex/www A records targeting the then-verified `172.64.80.1` with TTL 60 only in the former Vercel zone, preserving its 19 existing records. Cloudflare authoritative DNS and Worker were unchanged. The later `coordinator-browser-recovery.json` and updated `website-cloudflare.json` confirm normal Chrome, ordinary macOS HTTPS (200 from Cloudflare) and router DNS recovery. These observations resolve the earlier local-access blocker. The Vercel project is deleted and is not a rollback origin.

`docs.stenox.app` remains Mintlify, with CNAME `cname.mintlify-dns.com` and owner health checks returning 200. This docs task changes no DNS or hosting. The website's separate calendar/provider copy work is not assumed deployed by this source review.

## Docs verification and retained evidence

The focused checks cover the strict source snapshot, Mintlify 4.2.964 build validation, broken links, whitespace and rendered desktop/narrow behavior. Fresh logs/screenshots use `docs-provider-alignment-` in `/Users/home/.codex/qa-artifacts/stenox/v2-readiness-20261001/`. The final handoff records exact outcomes and source observations in `docs-readiness.json` and `docs-provider-alignment-review.json`. Local preview does not prove hosted search or public documentation acceptance.

Focused validation passes for 42 MDX files, 38 navigation pages and 127 local links/assets, with exact model/term checks against the recorded sources. Mintlify build and broken-link checks pass. Calendar and operation-input sections render at 1440 × 1000 and 320 × 740 without page overflow; scope text, manual generation and onboarding preparation also fit at 320 px. The payload table scrolls 40 px with the keyboard, and the calendar-to-processing link opens its destination by keyboard. No browser console errors were captured. The website main advanced during finalization to `d5aee74`; its disclosure-only delta was reviewed before the final strict source check.

Prior records, logs and screenshots remain intact, including the original source audit, consolidation report, `docs-notarized-recovery-review.json`, and the pre-refresh `9bed6cf` audit in Git history. The original media accessibility check passed with the existing AA/AAA color advisory; it is not full accessibility certification. This refresh preserves navigation, typography and styling.

The earlier missing worktree registration was safely pruned only after backup/ancestor/index checks; its branch and full verified archive remain, as documented in the consolidation report. This refresh removes no worktrees, app data, credentials or unrelated WIP, and stops no pre-existing process.

## Remaining gates

1. Review later source or artifact deltas. The fresh `bb165c2` manifest, notarization and signature evidence are reviewed; do not substitute the superseded `8e46e4f` artifacts.
2. Complete actual GUI production trial/existing-license acceptance for the fresh candidate and any new-build checks required by the app owner. Preserve the user-confirmed earlier in-app installation as that specific evidence, without reimposing the removed Others workflow.
3. Complete Polar-originated webhook delivery, compatible paid-app/fulfillment and merchant receipt acceptance before opening the staged offer. Preserve earlier purchase rights and allowances.
4. Publish only the three accepted V2 assets with explicit authority and full hash verification; align website version/presentation to that accepted release. Website hosting recovery alone does not authorize these actions.
5. Obtain docs push/publication authority, verify the Mintlify integration, then check hosted routes, redirects, responsive behavior and search. No docs push or publication is performed by this task.
