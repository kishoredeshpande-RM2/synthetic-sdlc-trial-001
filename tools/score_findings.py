"""Key-agnostic scorer for S2 findings. Run ONLY after the freeze commit and key release.

Usage: python score_findings.py <answer_key.json> <expected_key_sha256> <out_dir> <label> <findings.json> [...]

Produces (in <out_dir>):
  * <label>_candidate_matches.csv - one row per (seeded defect, candidate finding) pair that
    shares a requirement ID, plus findings without IDs offered against section-level defects.
    A human adjudicator marks each row SAME_DEFECT / DIFFERENT.
  * <label>_control_findings.csv - findings citing only clean-control requirements, for
    adjudication as VALID_UNSEEDED or FALSE_POSITIVE.
  * <label>_summary.json - PROVISIONAL detection counts by requirement-ID overlap. Final
    detection counts only after human adjudication of the candidate matches.
Several findings files are scored as their union under one label.
"""
import csv
import hashlib
import json
import os
import sys


def main(argv):
    if len(argv) < 6:
        print(__doc__)
        return 2
    key_path, expected_sha, out_dir, label = argv[1:5]
    actual_sha = hashlib.sha256(open(key_path, "rb").read()).hexdigest()
    if actual_sha != expected_sha:
        print(f"KEY FINGERPRINT MISMATCH: {actual_sha} != {expected_sha}. Stopping.")
        return 3
    key = json.load(open(key_path, encoding="utf-8"))
    findings = []
    for path in argv[5:]:
        data = json.load(open(path, encoding="utf-8"))
        for f in data["findings"]:
            f = dict(f)
            f["_source"] = f"{data.get('assessor', path)}"
            findings.append(f)
    os.makedirs(out_dir, exist_ok=True)

    controls = set(key["clean_controls"])
    rows, detected = [], {}
    for d in key["defects"]:
        ids = set(d["requirement_ids"])
        for f in findings:
            fids = set(f.get("requirement_ids", []))
            if (ids and ids & fids) or (not ids and not fids):
                ok_class = f.get("class") == d["class"] or f.get("class") in d["acceptable_alternative_classes"]
                rows.append([d["defect_id"], d["class"], d["location"], d["critical_blocking"],
                             f["_source"], f.get("finding_id"), ";".join(sorted(fids)), f.get("class"),
                             ok_class, f.get("severity"), f.get("proposed_disposition"), f.get("quote", "")[:200], ""])
                if ids:
                    detected.setdefault(d["defect_id"], True)
    with open(os.path.join(out_dir, f"{label}_candidate_matches.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["defect_id", "defect_class", "location", "critical_blocking", "assessor", "finding_id",
                    "finding_requirement_ids", "finding_class", "class_agrees", "severity",
                    "proposed_disposition", "quote_excerpt", "ADJUDICATION (SAME_DEFECT/DIFFERENT)"])
        w.writerows(rows)

    control_rows = [[f["_source"], f.get("finding_id"), ";".join(f.get("requirement_ids", [])), f.get("class"),
                     f.get("quote", "")[:200], ""]
                    for f in findings
                    if f.get("requirement_ids") and set(f["requirement_ids"]) <= controls]
    with open(os.path.join(out_dir, f"{label}_control_findings.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["assessor", "finding_id", "requirement_ids", "class", "quote_excerpt",
                    "ADJUDICATION (VALID_UNSEEDED/FALSE_POSITIVE)"])
        w.writerows(control_rows)

    defects = key["defects"]
    crit = [d["defect_id"] for d in defects if d["critical_blocking"]]
    by_class = {}
    for d in defects:
        c = by_class.setdefault(d["class"], {"seeded": 0, "provisional_detected": 0})
        c["seeded"] += 1
        c["provisional_detected"] += d["defect_id"] in detected
    summary = {
        "label": label, "key_sha256": actual_sha, "findings": len(findings),
        "seeded_defects": len(defects),
        "provisional_detected_by_id_overlap": len(detected),
        "provisional_detection_rate": round(len(detected) / len(defects), 3),
        "critical_blocking_provisional_detected": [c for c in crit if c in detected],
        "critical_blocking_total": crit,
        "by_class": by_class,
        "section_level_defects_needing_manual_match": [d["defect_id"] for d in defects if not d["requirement_ids"]],
        "control_findings_for_adjudication": len(control_rows),
        "note": "PROVISIONAL. Final scores require human adjudication of the candidate-match and control-finding worksheets.",
    }
    json.dump(summary, open(os.path.join(out_dir, f"{label}_summary.json"), "w", encoding="utf-8"), indent=2)
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
