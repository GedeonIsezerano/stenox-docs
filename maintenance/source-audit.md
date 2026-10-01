# Documentation source audit — October 1, 2026

This historical audit completed locally against app main **`9545cffb2f19f5677a98c6801cd6c0504c3d170a`** (`Add optional speaker diarization for file transcripts`). At the time of this audit, the changes were uncommitted, unpushed, and unpublished. The refresh is now being consolidated into local docs main; see `maintenance/consolidation-2026-10-01.md` for current integration status. This report is maintenance evidence and is excluded from the public documentation.

## Source boundary

- App repository: `/Users/home/Code/Stenox/app`. Read committed source with `git show` and an initial clean archive; uncommitted app changes and synthetic preview fixtures were not treated as product behavior.
- Initial main snapshot: `4fd0032ea95976d0e74b78b06231f72f7a7c5d38`. Main advanced during the audit. The new file-transcription commit was inspected and incorporated before final validation.
- Final remote refresh: `origin/main` remained `67ef44d69b80c3cd2403a52b56c511838837bac8`. Local main was 17 commits ahead, with no remote-only commits. These guides therefore describe committed development work, not proof of a public release.
- Website reference: the working tree at `/Users/home/Code/Stenox/website`, especially `app/globals.css`, `app/layout.tsx`, `lib/commerce.ts`, and `docs/paid-relaunch-brief.md`; visually compared with `http://127.0.0.1:3011/`.
- The public [download page](https://stenox.app/download) inspected during this audit still described the existing free v1.1 download. The [public homepage](https://stenox.app/) separated calendar development previews from that download. The docs banner and Release and access page preserve this distinction.

## What changed

All existing content guides were reviewed and rewritten around the current workflows. Seven Notetaker guides now cover capture, conversation editing, insights and personal notes, reference files and Ask, calendar context, processing, and exports. New pages document Cohere local speech, Gemini transcription, and local model management.

The provider pages now reflect the current runtime catalog, including 11 Whisper variants, two Parakeet variants, Cohere Transcribe, five current local cleanup models, and the separate meeting insight and speaker models. Deprecated local cleanup selections are identified as migration behavior. Removed Groq URLs remain as brief migration pages outside navigation. Existing redirects remain intact.

Dictation is documented as deterministic transcription followed by optional, explicit Polish. Profiles, hotkeys, word replacements, file transcription, permissions, privacy, troubleshooting, and support instructions were corrected. Unsupported vocabulary-learning and Parakeet vocabulary-boosting claims were removed. File transcription includes the newly committed cloud-provider Speakers & timestamps option and its validated TXT, Markdown, JSON, SRT, and VTT exports.

The visual update uses the website's warm paper surfaces, blue accents, pale blue and lavender panels, Satoshi headings, DM Sans body text, and JetBrains Mono code. Light mode is the default; dark mode remains explicit and usable. Navigation, metadata, banner, buttons, callouts, tables, focus treatment, and footer were included. Old animated mock UI and its unused loader/styles were removed; historical image assets were left in place but are not used as current screenshots.

## Claim-to-source map

Paths below are relative to the app repository at the recorded commit. Product behavior was checked in implementation and views rather than inferred from previews alone.

| Documentation area | Principal source | What the docs preserve |
| --- | --- | --- |
| Provider choices and defaults | `Stenox/Core/Models/ProviderMetadata.swift`; `Stenox/Managers/SettingsStore.swift` | Separate speech, cleanup, and meeting insight choices; no removed Groq choices; optional cleanup starts disabled. |
| Local speech | `Stenox/Services/Transcription/Providers/ParakeetProvider.swift`, `WhisperKitProvider.swift`, `CohereTranscribeProvider.swift` | Exact catalog IDs and estimated downloads; language limits; no Parakeet vocabulary hinting claim. |
| Local cleanup | `Stenox/Services/LLM/Providers/MLXProvider.swift`; `Stenox/Services/LLM/S1Correction.swift` | Five current models, legacy selected-only models, fixed S1 behavior, specialized Yooz path, current Gemma/Qwen selections. Runtime catalog takes precedence over an outdated module README or partial resource catalog. |
| Dictation and Polish | `Stenox/Managers/Recording/DictationCompletionManager.swift`; `Stenox/Services/TranscriptionService.swift` | Insert original transcript first; deterministic filler/replacement steps; explicit Polish; preserve original on failure or cancellation; no silent cloud fallback or model download. |
| Model lifecycle | `Stenox/Managers/LocalModelReadinessMonitor.swift`; settings model UI | Download is distinct from selection; selected cached models can warm automatically and remain resident; active/profile-used model deletion is guarded. |
| Profiles | `Stenox/Managers/ProfileManager.swift`; profile settings views | Global defaults, manual versus automatic mode, application matching, browser-title matching, and first eligible rule/profile behavior. |
| Plain and timed file transcription | `Stenox/Core/Models/FileTranscript.swift`; `Stenox/Managers/FileTranscriptionSession.swift`; `Stenox/Views/Settings/FileTranscriptionSettings.swift`, `FileTranscriptionResult.swift`, `FileTranscriptionTabView.swift`; transcription service and cloud adapters | Plain text workflow versus opt-in Deepgram/AssemblyAI/Gemini speakers and timings; provider-dependent timing; no invented timestamps; timed text bypasses cleanup/replacements; Gemini duration limit; five export formats. |
| Meeting capture and lifecycle | `Stenox/Managers/NotetakerManager.swift`; `Stenox/Services/Notetaker/NotetakerCapture.swift`, `NotetakerPipeline.swift`, `NotetakerSpeechSession.swift`; `Stenox/Views/Notetaker/NotetakerNewSessionView.swift` | New-session preparation; microphone and system audio; no meeting bot; permissions; pause/resume/end; active speech selection; closing the window does not end capture; no cross-launch capture resume. |
| Meeting models and providers | `Stenox/Services/Notetaker/NotetakerBriefModel.swift`, `NemotronDiarizer.swift`, `NotetakerInsightProvider.swift`, `NotetakerAgentProcess.swift` | Separate Qwen3.5 4B insight model and Nemotron diarizer; local and subscription-provider boundaries; bundled Codex/Claude runtimes; separate Antigravity CLI; saved model availability must not cause silent escalation. |
| Conversation and speakers | `Stenox/Services/Notetaker/NotetakerConversationTurn.swift`; `Stenox/Views/Notetaker/NotetakerTranscriptField.swift`, `NotetakerSpeakerField.swift`; document and manager logic | Grouped turns, speaker renaming/reassignment, transcript edits, retained source IDs/timing, and uncertainty when provider evidence is incomplete. |
| Insights, questions, and notes | `Stenox/Managers/NotetakerInsightManager.swift`; `Stenox/Services/Notetaker/NotetakerDocument+Notes.swift`, `NotetakerQuestionQueue.swift`, `NotetakerQuestionExposure.swift`; `Stenox/NotetakerQuestionOverlayController.swift`; note/editor views | Cited takeaways/decisions/tasks/questions; bounded cadence/context; protect edits/removals; sequential notch questions; personal notes; current/refined notes and suggestion acceptance. |
| References and Ask | `Stenox/Services/Notetaker/NotetakerReference.swift`, `NotetakerBriefContext.swift`, `NotetakerBriefService.swift`; sources/page views | Supported readable document text and limits; duplicate handling; no OCR/image understanding promise; bounded context; citations; explicit saving of answers. |
| Calendar | `Stenox/Managers/NotetakerCalendarManager.swift`; `Stenox/Services/Notetaker/NotetakerCalendar.swift`, `NotetakerCalendarOAuth.swift`, `NotetakerCalendarHTTP.swift`; calendar/new-session views | Read-only Google events; manual calendar IDs; seven-day initial window; invitees are not verified attendees; saved context; Google-derived context requires on-device insight/Ask/refinement; no automatic Drive import; Outlook hidden in normal launches. |
| Storage and export | `Stenox/Services/Notetaker/NotetakerStore.swift`, `NotetakerExport.swift`; history/document views | Plaintext local SQLite; editable saved history; active-session delete guard; SRT, timestamped TXT, refined Markdown, current structured Markdown; no promise of a bundled export of personal notes, references, and Ask. |
| Release and access | Website `lib/commerce.ts`, `docs/paid-relaunch-brief.md`, public download page | Staged C$69/C$100 offer and planned trial/licensing terms are not live checkout or proof of a released compatible binary. |

## Validation

Historical validation from the original refresh follows. CLI version: **Mintlify 4.2.964**. No Mintlify account login, publication, or app runtime tests were performed. The consolidation report records the subsequent checks and app-source drift.

| Check | Result |
| --- | --- |
| `mint validate --telemetry false` | Passed build validation. |
| `mint broken-links --telemetry false` | Passed; no broken links reported. |
| `python3 scripts/check-docs.py` | Passed: 41 MDX files, 37 navigation pages, 108 local links/assets, exact local model catalog IDs, legacy model presence, redirects, and current-main snapshot match. |
| `git diff --check` | Passed. |
| `mint a11y --telemetry false` | No MDX image/video accessibility issues. Primary-on-light contrast 5.28:1 meets AA; CLI retains an advisory for AAA. Light-on-dark 8.89:1 meets AAA. Button color contrast meets the CLI's 3:1 threshold on both backgrounds. This is not a full WCAG certification. |
| Desktop rendered checks | Home and meeting guides at 1440 × 1000 in light/dark themes; sidebar, TOC, cards, banner, and footer inspected; no horizontal page overflow. Rendered heading/body families match Satoshi/DM Sans. Home cards navigate by keyboard. |
| Mobile rendered checks | 390 × 844 model guide and 320 × 740 home/calendar/navigation/footer. Mobile menu link opens Calendar context; page width equals viewport width. Wide tables remain horizontally scrollable inside their own wrapper with a visible hint and keyboard focus. Arrow keys moved the table 55 px without widening the page. |
| Browser console | No captured error entries in the final home preview check. |
| Search | Panel opens; local CLI explicitly requires `mint login` to activate search. Hosted search results remain unverified. |

Logs and screenshots are saved in `/Users/home/.codex/qa-artifacts/stenox/docs/2026-10-01/`:

- Build log (`/Users/home/.codex/qa-artifacts/stenox/docs/2026-10-01/mint-validate.log`)
- Link log (`/Users/home/.codex/qa-artifacts/stenox/docs/2026-10-01/mint-broken-links.log`)
- Accessibility log (`/Users/home/.codex/qa-artifacts/stenox/docs/2026-10-01/mint-a11y.log`)
- Catalog and source check (`/Users/home/.codex/qa-artifacts/stenox/docs/2026-10-01/catalog-links-check.log`)
- Desktop home, light (`/Users/home/.codex/qa-artifacts/stenox/docs/2026-10-01/desktop-home-light.jpg`)
- Desktop meetings, light (`/Users/home/.codex/qa-artifacts/stenox/docs/2026-10-01/desktop-meetings-light.jpg`)
- Desktop meetings, dark (`/Users/home/.codex/qa-artifacts/stenox/docs/2026-10-01/desktop-meetings-dark.jpg`)
- Mobile table keyboard focus (`/Users/home/.codex/qa-artifacts/stenox/docs/2026-10-01/mobile-models-keyboard.jpg`)
- 320 px mobile navigation (`/Users/home/.codex/qa-artifacts/stenox/docs/2026-10-01/mobile-navigation-320.jpg`)
- 320 px calendar guide (`/Users/home/.codex/qa-artifacts/stenox/docs/2026-10-01/mobile-calendar-light-320.jpg`)
- 320 px dark footer (`/Users/home/.codex/qa-artifacts/stenox/docs/2026-10-01/mobile-footer-dark-320.jpg`)

## Preserved work and limits

The pre-existing uncommitted Parakeet documentation edit was preserved before rewriting it as an original patch (`/Users/home/.codex/qa-artifacts/stenox/docs/2026-10-01/original-parakeet-edit.patch`) and a full original file (`/Users/home/.codex/qa-artifacts/stenox/docs/2026-10-01/original-parakeet-local.mdx`). Its vocabulary-boosting claim conflicts with the reviewed implementation, so the current guide documents downstream word replacements instead. No app or website working-tree edits were changed.

Source inspection establishes implemented behavior, not successful execution with every provider, account entitlement, model download, or microphone setup. In particular, Antigravity real-account sign-in/inference acceptance remains unverified and is identified as such in the guide. No provider secrets were read or used. Catalog sizes are estimates, not measured memory or speed requirements.

The original audit left a local preview at **http://127.0.0.1:3022/**. Local consolidation commits were authorized in the later phase-one task. Push, publication, payment enablement, and release are outside that phase.
