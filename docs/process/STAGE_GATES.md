# Stage gates (MC-SDLC-TOOL-001-T01)

## Rules for every stage

1. **Advancing:** a stage advances only when **both** of these exist:
   - (a) the required verification evidence;
   - (b) a recorded human decision in `control/decisions/`.
2. **Non-PASS stops progression.** There are no automatic repair-and-approve loops.
3. **Producer self-checks are labelled as such.** They never stand in for independent verification.
4. **Every verdict names the exact commit SHA.** A material change invalidates earlier verification.
5. **Decisive evidence is committed to this repository.** Chat history is not a record.

## Stages

| Stage | Inputs | Required output (Producer or tool) | Verification | Human decision | Planned enforcement (to be tested; **not yet configured**) |
|---|---|---|---|---|---|
| S1 Requirements intake | Original `.docx` | Converted Markdown; source and derived SHA-256; conversion log | Deterministic: every TLL ID in the source appears exactly once in the conversion; text spot-check | Accept the intake | Required status check on the conversion workflow |
| S2 Requirements assurance | Converted requirements (no key) | Findings (`docs/process/FINDINGS_SCHEMA.json`) with source quotes, class, severity, questions | Independent assessors (§ evaluation procedure); deterministic quote check (`tools/check_quotes.py`) | PASS / CLARIFICATION REQUIRED / BLOCK per finding | Gate check fails while any `disposition:BLOCK` Issue is open |
| S3 Requirements baseline | S2 dispositions; Product Owner clarifications | Approved requirements and acceptance criteria; baseline tag | No open BLOCK; changes traced to clarifications | Approve baseline | Ruleset: `requirements/**` changes need a code-owner review; baseline tag protected |
| S4 Architecture / design | Baseline | Design, interfaces, risks, traceability matrix | Independent design review (Codex) | Approve design | Required check plus code-owner review |
| S5 Implementation | Approved design | One bounded feature plus Producer tests | Producer evidence only, labelled as such | — | PR from Producer branch |
| S6 Independent verification | Exact candidate SHA plus baseline | Verifier report, negative and boundary tests, defects | Codex from a fresh, isolated clone | Accept or reject the verdict | Required check bound to head SHA; stale approvals dismissed |
| S7 Integration / release | Verified PR | CI results; release artifact plus digest | CI on GitHub-hosted runners | Merge and release acceptance | Ruleset plus code-owner approval |
| S8 Deployment / recovery | Approved release digest | Deployment evidence; rollback demonstration | Digest equality: approved = built = deployed | Deployment approval | Protected environment with required reviewer (public repo); digest check |
