#!/usr/bin/env python3
"""Print a corpus summary and run integrity checks."""

from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from aibench.loader import load_cases  # noqa: E402
from aibench.rubric import heuristic_checks  # noqa: E402
from aibench.validate import assert_valid_corpus  # noqa: E402


def main() -> int:
    cases = load_cases(ROOT)
    report = assert_valid_corpus(cases)
    domains = Counter(case["domain"] for case in cases)
    severities = Counter(case["severity"] for case in cases)
    verdicts = Counter(case["verdict"] for case in cases)

    warnings: list[str] = []
    for case in cases:
        for item in heuristic_checks(case):
            warnings.append(f"{case['id']}: {item}")

    print(f"cases: {report.case_count}")
    print("domains:")
    for name, count in sorted(domains.items()):
        print(f"  {name}: {count}")
    print("severities:")
    for name, count in sorted(severities.items()):
        print(f"  {name}: {count}")
    print("verdicts:")
    for name, count in sorted(verdicts.items()):
        print(f"  {name}: {count}")
    if warnings:
        print("heuristic warnings:")
        for item in warnings:
            print(f"  {item}")
    else:
        print("heuristic warnings: none")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
