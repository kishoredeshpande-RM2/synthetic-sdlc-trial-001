"""Deterministic traceability check for S2 findings.

Usage: python check_quotes.py <converted_requirements.md> <findings.json> [...]

For each finding, checks that:
  * every cited requirement ID exists in the converted requirements;
  * the quote occurs verbatim in the converted requirements (whitespace-normalised).
Exit code 1 if any finding fails. Failing findings are reported, never dropped.
"""
import json
import re
import sys


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    source = open(argv[1], encoding="utf-8").read()
    source_norm = norm(source)
    known_ids = set(re.findall(r"TLL-\d{3}", source))
    failures = 0
    for path in argv[2:]:
        data = json.load(open(path, encoding="utf-8"))
        for f in data["findings"]:
            problems = []
            unknown = [r for r in f.get("requirement_ids", []) if r not in known_ids]
            if unknown:
                problems.append("unknown requirement IDs: " + ", ".join(unknown))
            if norm(f.get("quote", "")) not in source_norm:
                problems.append("quote not found verbatim in source")
            status = "FAIL" if problems else "OK"
            failures += bool(problems)
            print(f"{status}\t{path}\t{f.get('finding_id')}\t{'; '.join(problems)}")
    print(f"traceability failures: {failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
