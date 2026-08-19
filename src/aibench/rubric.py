"""Rubric helpers: fixture severities and cheap heuristic checks.

A structured score profile can be computed from the ten rubric dimensions.
It is a diagnostic summary, not a substitute for expert judgement. See
``RUBRIC.md``.
"""

from __future__ import annotations

from typing import Any, Mapping

RUBRIC_DIMENSIONS: tuple[str, ...] = (
    "task interpretation",
    "conceptual correctness",
    "mathematical correctness",
    "statistical correctness",
    "causal validity",
    "assumptions",
    "completeness",
    "clarity",
    "evidence discipline",
    "final-answer alignment",
)

# Known fixtures used by tests. Keys are case ids; values are expected severity.
FIXTURE_SEVERITY: dict[str, str] = {
    "ECON-008": "PASS",
    "ECON-009": "MAJOR",
    "ECONM-002": "CRITICAL",
    "ECONM-004": "CRITICAL",
    "STAT-001": "MAJOR",
    "STAT-008": "PASS",
    "MATH-003": "CRITICAL",
    "MATH-006": "PASS",
    "QR-003": "MAJOR",
    "MIX-005": "PASS",
}

DIMENSION_SCORE_RANGE = (0, 3)


def expected_severity(case_id: str) -> str:
    """Return the fixture severity for a known case id."""
    if case_id not in FIXTURE_SEVERITY:
        raise KeyError(f"no fixture severity registered for {case_id!r}")
    return FIXTURE_SEVERITY[case_id]


def heuristic_checks(case: Mapping[str, Any]) -> list[str]:
    """Return a list of heuristic warnings (empty if none).

    These checks do not assign a quality score. They flag empty golden
    responses, missing assumptions, and severity/verdict mismatches that
    should already have been rejected by the schema.
    """
    warnings: list[str] = []
    golden = str(case.get("golden_response") or "").strip()
    if not golden:
        warnings.append("golden_response is empty")
    if len(golden) < 200:
        warnings.append("golden_response is shorter than 200 characters")

    corrected = str(case.get("corrected_reasoning") or "").strip()
    if not corrected:
        warnings.append("corrected_reasoning is empty")

    assumptions = case.get("assumptions") or []
    if not assumptions:
        warnings.append("assumptions list is empty")

    steps = case.get("validation_steps") or []
    if not steps:
        warnings.append("validation_steps list is empty")

    return warnings


def structured_profile(dimension_scores: Mapping[str, int]) -> dict[str, Any]:
    """Assemble a diagnostic profile from per-dimension integer scores.

    Each dimension is scored on {0, 1, 2, 3}. The returned mapping includes
    those scores and simple descriptives. Callers must not treat the mean as
    the evaluation.
    """
    missing = [name for name in RUBRIC_DIMENSIONS if name not in dimension_scores]
    if missing:
        raise ValueError(f"missing dimension score(s): {', '.join(missing)}")

    scores: dict[str, int] = {}
    lo, hi = DIMENSION_SCORE_RANGE
    for name in RUBRIC_DIMENSIONS:
        value = dimension_scores[name]
        if not isinstance(value, int) or value < lo or value > hi:
            raise ValueError(
                f"{name}: score must be an integer in [{lo}, {hi}], got {value!r}"
            )
        scores[name] = value

    values = list(scores.values())
    return {
        "dimensions": scores,
        "mean": sum(values) / len(values),
        "minimum": min(values),
        "failing_dimensions": [name for name, score in scores.items() if score == 0],
        "note": (
            "This profile is a structured diagnostic. Expert judgement is not "
            "a single score; a zero on causal validity or evidence discipline "
            "can dominate a high mean."
        ),
    }


def verdict_from_profile(profile: Mapping[str, Any]) -> str:
    """Map a rubric profile to pass/fail without using the mean as the rule.

    A zero on causal validity or evidence discipline is a fail even when
    the mean is high.
    """
    failing = set(profile.get("failing_dimensions") or [])
    if "causal validity" in failing or "evidence discipline" in failing:
        return "fail"
    if int(profile.get("minimum", 0)) == 0:
        return "fail"
    return "pass"
