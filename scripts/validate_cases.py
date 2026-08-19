#!/usr/bin/env python3
"""Fail the process if the case corpus is not internally consistent."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from aibench.loader import CaseLoadError, load_cases  # noqa: E402
from aibench.validate import CorpusValidationError, assert_valid_corpus  # noqa: E402


def main() -> int:
    try:
        cases = load_cases(ROOT)
        report = assert_valid_corpus(cases)
    except (CaseLoadError, CorpusValidationError) as exc:
        print(f"VALIDATION FAILED: {exc}", file=sys.stderr)
        return 1
    print(f"OK: {report.case_count} cases, unique ids, required defect families present")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
