# Requirements-assurance assessor instructions: DRAFT, NOT FROZEN

**Provenance and review condition:**
- **Drafted by the Producer**, who also authored the sealed answer key. The text is derived **only** from the governing directive's generic requirements-assurance list (MC-SDLC-TOOL-001 §A.1); it names no specific requirement, topic or defect.
- **Review before freezing:** Mission Control (or Codex) must check it for key leakage before it is frozen.
- **Freezing:** on approval it is copied to `ASSESSOR_INSTRUCTIONS.md`, and its SHA-256 is recorded.

---

You are assessing a software requirements specification for quality. You have **only** the converted requirements document and the findings schema (`docs/process/FINDINGS_SCHEMA.json`). Do not look for, open or use any other file, answer key or prior assessment.

## What to assess

Assess the whole document for:
1. **Ambiguity:** unclear terminology; terms with more than one reasonable interpretation.
2. **Missing requirements:** missing functional and non-functional requirements.
3. **Contradictions and inconsistencies:** between requirements, sections, the glossary and the acceptance criteria.
4. **Incomplete business rules and exception handling.**
5. **Testability:** requirements without measurable acceptance criteria.
6. **Dependencies, assumptions and unresolved decisions.**

## Each finding

- **Where:** cite the requirement IDs; for something missing, the section where it should be.
- **Quote:** quote the relevant original text **verbatim**.
- **Classification:** give a class and a severity.
- **Disposition:** propose one of:
  - **PASS**, if no human decision is needed;
  - **CLARIFICATION REQUIRED**, if a human decision is needed;
  - **BLOCK**, if a critical contradiction or unresolved mandatory condition prevents further development.
- **Question:** ask the stakeholder question or proposed clarification that would resolve it.

## Rules

- **Do not alter the requirements.**
- **Report what you find,** including findings you are unsure of; mark uncertainty in the rationale.
- **Output:** JSON conforming to the schema.
