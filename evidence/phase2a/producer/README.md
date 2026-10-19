# Phase 2A evidence (Producer). Not independent verification.

`trial-records` is an **unprotected** branch. It is used because `main` is protected by a ruleset with no bypass, and a solo account cannot approve its own pull requests. Integrity rests on the commit SHAs recorded in the Mission Control report.

| File | Content |
|---|---|
| `phase2a_negative_tests.txt` | Raw output of negative tests N1–N9 and N6 offline |
| `phase2a_codex_sandbox_probe_as_User.txt` | Codex-sandbox read probe with positive and negative controls. Protected paths are labelled, not named |
| `ruleset_*.json` | Rulesets as read back from the API. The push ruleset was rejected (HTTP 422) |

## Control inventory

| Control | Class | Configured | Negative test | Result |
|---|---|---|---|---|
| No direct push to `main` | NATIVE (ruleset) | yes | N1 | **ENFORCED** (GH013 "Changes must be made through a pull request") |
| No force push / deletion of `main` | NATIVE | yes | N2 | **ENFORCED** |
| PR author cannot self-approve | NATIVE | inherent | N5 | **ENFORCED** ("Can not approve your own pull request") |
| Merge requires approval, code owner and last-push approval | NATIVE | yes | N4, N4b, N7 | **ENFORCED**, including against `--admin` (no bypass actors) |
| Required checks `source-integrity`, `requirements-block-gate` (GitHub Actions app 15368) | CONFIGURED + CUSTOM (`pull_request_target`, base-branch definition) | yes | N3, N8 | Real checks fail correctly. **BUT FORGEABLE** (N7) |
| Required check `independent-verification` (signed Verifier verdict) | CUSTOM | yes, **no key enrolled** (fails closed) | N6a, N6b, N7 | Malformed and unenrolled verdicts rejected. **Forged by a PR-defined workflow (N7): FAIL** |
| Source-document baseline protection | CUSTOM check + CODEOWNERS + PR rule | yes | N3, N7 | Check detects the change; **forgeable**; held only by the approval rule |
| Push ruleset restricting `requirements/source/**`, `.github/**` | — | **UNAVAILABLE** (422: user-owned public repos cannot have push rules) | — | — |
| Baseline tags `baseline/*` immutable | NATIVE (tag ruleset) | yes | N9 | **ENFORCED** (update and delete rejected) |
| Unresolved BLOCK prevents advancement | CUSTOM check | yes | N8 | **ENFORCED** as a check (fails while open, passes when closed). Forgeable as above |
| Fork-PR workflows need approval | NATIVE | `all_external_contributors` | not tested | Configured |
| Stale approval dismissed on push | NATIVE | yes | **pending** (needs a human approval first) | Not tested |
