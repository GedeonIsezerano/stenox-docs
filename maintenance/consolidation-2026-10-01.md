# Local docs consolidation — October 1, 2026

Phase one consolidates the existing docs refresh into local `main`. It does not establish final V2 alignment, publish documentation, or change the app, website, or licensing repositories. All public-page content and theme files from the captured refresh were retained; the additional edits clarify historical audit status and repair maintenance evidence references.

## Inventory and disposition

| Item | Evidence | Disposition |
| --- | --- | --- |
| Main checkout | `/Users/home/Code/Stenox/docs`, branch `main`, starting commit `32c5564acf45f9952646e03d254a26d45ac0c0cc`; 36 changed/deleted tracked files and 15 untracked files | Integrate the complete refresh: meeting guides, model/provider corrections, navigation, theme/fonts, source audit, and validation script. |
| Missing worktree | `/private/tmp/stenox-docs-free`, branch `codex/free-1.0-docs`, commit `50f063a3941d611e3ab80e673835c9584886adeb`; Git reports a prunable registration | Branch is already an ancestor of main. Retained worktree index has no staged difference from its HEAD. No worktree directory remains to inspect for unstaged/untracked files. Registration and branch retained; cleanup eligible after ownership confirmation. |
| Remote branches | Read-only `git ls-remote --heads origin` returned `main` at `32c5564acf45f9952646e03d254a26d45ac0c0cc` and `feature/logo-update` at `8fa86536ca79f125036a3dc0f80efe881b649379` | Both are already in local main history. No remote-only branch work found. No push performed. |
| Codex capture/checkpoint refs | Both reference tree `e8010707b07033b9a2b01bb5f9c5a85739f0e253` | Every captured file hash matched the initial checkout, including untracked files. No additional variant to integrate. Refs retained. |
| Stash list | Empty | No named stash to apply. |
| Recoverable dropped stash | `2b0981a3f6ae091284c0911860fd02842bfb7503`, with index parent `75217f27a6c3240cbb957580d6a11d1e2118d9cf` | Contains only the old Parakeet vocabulary-boosting wording. Preserved in the full backup and an extracted patch; intentionally superseded by source-audited word-replacement wording. |
| Unreachable root trees | `41b4a6bee5d388bcee7be83582b5bac3918232fc`, `a64ca7454eac70b0c59d5ae5ee15b54a8598644e`, `338505f6a8310e13d6cfabf089529cf4e34db449` | Each differs from a historical main commit only in that same Parakeet claim. All objects preserved; no independent docs work omitted. |

No worktrees, branches, refs, persistent files, or preview processes were cleaned up. Historical images and existing repository guidance remain intact.

## Preservation

Before editing or staging, the complete checkout, `.git`, untracked files, missing-worktree metadata, reflogs, and unreachable objects were archived at:

`/Users/home/.codex/qa-artifacts/stenox/docs/consolidation-2026-10-01/docs-before-consolidation.tar.gz`

SHA-256: `044c47ce5ceaf410d318e16a9e0e9c558e935563b2361ad14e2fd0e50c2472b7`. All 451 archived files were read successfully. The same directory contains inventory outputs, the initial binary diff, recovered Parakeet patches, and current validation logs. Original refresh screenshots and the original Parakeet file/patch remain under `/Users/home/.codex/qa-artifacts/stenox/docs/2026-10-01/`.

## Validation and dependency

| Check | Current result |
| --- | --- |
| Mintlify 4.2.964 build validation | Pass. |
| Mintlify broken links | Pass after converting 13 filesystem evidence links in the maintenance audit to literal file references. The initial failure and successful rerun logs are retained. |
| Mintlify accessibility check | Pass for MDX media attributes; existing AA/AAA color advisory remains. This is not full accessibility certification. |
| `python3 scripts/check-docs.py --allow-newer-main` | Pass against recorded app commit `9545cffb2f19f5677a98c6801cd6c0504c3d170a`: 41 MDX files, 37 navigation pages, 108 local links/assets, and local model catalogs. |
| `python3 scripts/check-docs.py` | Dependency pending: fails only because app main advanced beyond the recorded snapshot. Observed app main was `9f16e2e41fff7f987be3f611d3d481a0e21e5338`. The final app baseline has not been supplied. |
| `git diff --check` | Pass. |
| Current local preview | Home renders at 1440 × 1000; meeting guide renders at 320 × 740. Mobile navigation opens Calendar context, and dark mode renders correctly. Document width equals viewport width at 1440 and 320 pixels. No captured browser console errors. |

The original source snapshot remains unchanged. The explicit `--allow-newer-main` run validates the reviewed snapshot only; it does not accept newer app behavior. The historical audit's rendered evidence remains useful because the public docs/theme files were unchanged during consolidation. Hosted search, publication, and provider-account acceptance were not tested.

## Next phase

Wait for the coordinator's final app SHA and release scope before updating upgrade, permissions, licensing, payments, or Cloudflare documentation. The supplied legal-identity correction is retained for that phase: use “GKI Software Inc., formerly Sophosia Software Inc.” where the docs already identify the legal publisher, without adding unnecessary legal text. If signing documentation needs it, distinguish the Apple certificate display “Sophosia Software Inc.” under Team ID `VWXR46VR26` from the current legal entity. No existing legal-publisher wording was found in the public docs during this phase.
