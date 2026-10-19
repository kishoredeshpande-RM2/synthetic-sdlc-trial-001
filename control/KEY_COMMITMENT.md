# Answer-key commitment

The seeded-defect answer key for the requirements fixture is **sealed** and is **not** in this repository. Only its SHA-256 fingerprints are published here. This is a commitment, so that the key cannot be changed after any assessor's findings are seen.

| Sealed file | SHA-256 |
|---|---|
| `answer_key.json` | `94abc347a888d4cac426eb210a0072869500c555684c844179d009997b2185b7` |
| `answer_key.md` (human-readable rendering of the same key) | `f51828007d6434557a28ecbcb270bb253ff0d1ebeaab6a0405fd5be03ac592e1` |
| `build_fixture_and_key.py` (generator of the Word fixture and the key) | `1cbf949aac7e0d7359c0cf5851c63cc5af91edd18ce2ea4c92c60b4e3a084f6e` |

**The key is bound to this fixture.** It records the Word fixture's SHA-256: `3a47ed2ea549f1a9bcca0386354bac2d52cd8c045e212baccb0b39d835f6159f`, the same value as in `requirements/source/SOURCE_FINGERPRINT.md`.

**Custody** (Product Owner and Mission Control):
1. The key was created by the Producer (Claude), who is therefore **disqualified** from acting as a requirements-assurance assessor.
2. The sealed files are to be moved off the trial machine by the Product Owner, under the custody arrangement Mission Control approves.
3. At scoring time, the custodian releases the key. Before any score is computed, its fingerprint must match this table.
4. Scoring happens only after every assessor's findings have been committed, with the freezing commit's SHA recorded.

**No scored detection result may be claimed** before Mission Control approves custody and the evaluation boundary.
