# Requirements-assurance evaluation procedure (S2)

**Status: PROPOSED.** It must not be run for scoring until Mission Control approves answer-key custody and this evaluation boundary.

## 1. Independence boundary

| Party | May see | May not see |
|---|---|---|
| **Fixture author: Claude, the Producer and trial-integrator session** | Everything. **Disqualified as an assessor** | — |
| **Assessor A: Codex**, run from a separate, restricted Windows account (the Verifier account) in a fresh clone under `C:\sdlc_trial_001\verifier\` | The converted requirements; this procedure; the findings schema | The sealed key; the generator; the Producer's notes; any chat transcript |
| **Assessor B: a fresh Claude Code session** with no prior context, also run under a separate account or with path-deny rules | Same as A | Same as A; **also** the Producer session's transcripts under the Product Owner's user profile |
| **Assessor C: Spec Kit** (`specify` CLI 1.1.0), run as a tool step driven by Assessor A or B | Same as A | Same as A |
| **Custodian: the Product Owner**, or a party Mission Control names | The sealed key | — |

**Pre-run isolation probe.** Required before each assessor run; its output is committed as evidence.
- **What the assessor environment attempts:**
  1. listing and reading the sealed-key folder;
  2. reading the Producer working copy;
  3. reading the Producer session transcript directory.
- **Pass condition:** each must be **denied or absent**.
- **Interpretation rules** (pilot lesson):
  - "blocked" text or missing output is **INCONCLUSIVE**, not PASS;
  - INCONCLUSIVE stops the run.

## 2. Inputs (frozen before any run)

1. **Converted requirements:** the S1 output. Its source fingerprint is checked against `requirements/source/SOURCE_FINGERPRINT.md`.
2. **Assessor instructions:**
   - written **before** any run and committed;
   - their SHA-256 is recorded;
   - **they must not be changed after a run**, nor tuned against the key.
3. **Same instructions for every assessor:** Assessors A and B receive identical instructions.

## 3. Assessor output

**Format:** one JSON file per assessor, following `docs/process/FINDINGS_SCHEMA.json`.

**Each finding gives:**
- the requirement IDs (or a section, for omissions);
- a **verbatim quote** from the converted text;
- the class, one of: `ambiguity` | `contradiction` | `omission` | `untestable` | `dependency` | `incomplete business rule` | `other`;
- the severity: `critical` | `major` | `minor`;
- the proposed disposition: `PASS` | `CLARIFICATION REQUIRED` | `BLOCK`;
- the rationale;
- a stakeholder question.

**Where the files go:** they are committed to `evidence/S2/<assessor>/findings.json`, together with:
- the run transcript or log;
- the tool and version;
- the instruction hash.

**Freezing:** the commit that adds **all** assessor outputs is the **freeze commit**, and its SHA is recorded before the key is released.

## 4. Deterministic checks (tool: `tools/check_quotes.py`)

- **Every finding's quote** must occur verbatim, after whitespace normalisation, in the converted requirements.
- **Every cited requirement ID** must exist.
- **Failing findings** are reported as *traceability failures*. They are not silently dropped.

## 5. Scoring (after the freeze only)

1. **Key release and integrity:** the custodian releases the key, and its SHA-256 must match `control/KEY_COMMITMENT.md`.
2. **Scoring tool:** `tools/score_findings.py` is run for each assessor, and for the union of assessors.
3. **Results are reported separately by source:** Assessor A (Codex), B (Claude), C (Spec Kit), deterministic checks, and the union.
4. **What is reported:**
   - detection rate overall;
   - detection of predesignated critical blocking contradictions;
   - detection per defect class;
   - classification agreement;
   - findings with traceability failures;
   - findings on clean controls, for adjudication.
5. **Thresholds** (experimental, set by Mission Control):
   - at least 80% of seeded defects detected;
   - 100% of the critical blocking contradictions;
   - every finding traceable.
6. **Adjudication of control findings:** findings on requirements the key marks as clean controls are adjudicated by Mission Control as a **valid unseeded defect** or a **false positive**. The fixture author's intent is not authoritative.
7. **A failed gate is a result.** The evidence is preserved, and no re-run with changed instructions may be presented as an independent pass.

## 6. Human dispositions

- **Findings become Issues:** each finding becomes, or is grouped into, an Issue labelled `stage:S2` plus its proposed disposition.
- **The Product Owner decides:** they answer the questions and set the final disposition in the GitHub web UI.
- **An open `disposition:BLOCK` Issue prevents S3,** a control to be configured and tested.
