# synthetic-sdlc-trial-001

> **SYNTHETIC TRIAL ONLY.**
> - This repository contains no real product, customer or proprietary content.
> - *ToolShare Commons* is a fictional community tool-lending library, invented to test a software-development process.

**Purpose:** a controlled trial (MC-SDLC-TOOL-001-T01) of a GitHub-centred Producer–Verifier development workflow. The workflow runs from a Word requirements document through to deployment and rollback.

**What success means:** working, tested controls and less manual coordination, not a large amount of code.

## Current status

**The authoritative state is [`control/stage_state.yml`](control/stage_state.yml).** Stage gate Issues (label `gate`) mirror it in the web UI.

| Stage | Name | Status |
|---|---|---|
| S0 | Trial setup (Phase 1) | IN PROGRESS: awaiting Mission Control Phase 1 acceptance |
| S1 | Requirements intake | NOT STARTED |
| S2 | Requirements assurance | NOT STARTED: **blocked** until answer-key custody is approved |
| S3 | Requirements baseline | NOT STARTED |
| S4 | Architecture / design | NOT STARTED |
| S5 | Implementation | NOT STARTED |
| S6 | Independent verification | NOT STARTED |
| S7 | Integration / release | NOT STARTED |
| S8 | Deployment / recovery | NOT STARTED |

## Roles

| Role | Who | Notes |
|---|---|---|
| **Producer** | Claude Code | Commits are labelled `Claude Code (Producer, synthetic trial)` |
| **Independent Verifier** | Codex | Works from a fresh, isolated clone of the exact commit |
| **Acceptance** | Mission Control, with the Product Owner approving at stage gates | — |

**The Producer's self-checks are never independent verification.**

## Layout

| Path | Contents |
|---|---|
| `requirements/source/` | The original Word specification and its SHA-256 fingerprint |
| `control/` | Stage state, decision records and the answer-key commitment |
| `docs/process/` | Stage-gate definitions and the requirements-assurance evaluation procedure |
| `tools/` | Small deterministic checks: quote traceability and scoring |
| `evidence/` | Trial evidence, added stage by stage |
