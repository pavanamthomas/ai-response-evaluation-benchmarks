"""Corpus-level validation: counts, unique ids, and defect coverage."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Iterable, Sequence

REQUIRED_DEFECT_FAMILIES: tuple[str, ...] = (
    "wrong economic definition",
    "correlation/causation",
    "OVB",
    "invalid IV",
    "weak instrument",
    "incorrect DiD parallel-trends",
    "staggered-DiD issue",
    "incorrect placebo interpretation",
    "p-value error",
    "CI error",
    "statistical vs economic significance",
    "leakage",
    "overfitting",
    "wrong regression interpretation",
    "wrong sign",
    "unit error",
    "incorrect optimization constraint",
    "infeasible solution",
    "boundary-condition omission",
    "probability error",
    "Bayes error",
    "arithmetic error",
    "unsupported empirical claim",
    "invented citation",
    "incomplete answer",
    "correct result with invalid reasoning",
    "technically correct but semantically wrong",
    "answer to wrong interpretation of ambiguous prompt",
)

MINIMUM_CASE_COUNT = 50


@dataclass
class ValidationReport:
    """Outcome of corpus validation."""

    case_count: int
    ids: list[str]
    missing_families: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors and not self.missing_families and self.case_count >= MINIMUM_CASE_COUNT


class CorpusValidationError(ValueError):
    """Raised when the case corpus fails integrity checks."""


def _family_set(cases: Iterable[dict[str, Any]]) -> set[str]:
    observed: set[str] = set()
    for case in cases:
        for item in case.get("error_classification") or []:
            observed.add(item)
    return observed


def validate_corpus(cases: Sequence[dict[str, Any]]) -> ValidationReport:
    """Check uniqueness, size, and required defect-family coverage."""
    errors: list[str] = []
    ids = [str(case["id"]) for case in cases]
    if len(ids) != len(set(ids)):
        seen: set[str] = set()
        duplicates: list[str] = []
        for case_id in ids:
            if case_id in seen and case_id not in duplicates:
                duplicates.append(case_id)
            seen.add(case_id)
        errors.append(f"duplicate ids: {', '.join(duplicates)}")

    if len(cases) < MINIMUM_CASE_COUNT:
        errors.append(
            f"expected at least {MINIMUM_CASE_COUNT} cases, found {len(cases)}"
        )

    observed = _family_set(cases)
    missing = [name for name in REQUIRED_DEFECT_FAMILIES if name not in observed]

    report = ValidationReport(
        case_count=len(cases),
        ids=ids,
        missing_families=missing,
        errors=errors,
    )
    if missing:
        report.errors.append(
            "missing required defect families: " + ", ".join(missing)
        )
    return report


def assert_valid_corpus(cases: Sequence[dict[str, Any]]) -> ValidationReport:
    """Validate and raise if the corpus is not acceptable."""
    report = validate_corpus(cases)
    if not report.ok:
        raise CorpusValidationError("; ".join(report.errors))
    return report
