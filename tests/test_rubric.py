"""Rubric helper tests."""

from __future__ import annotations

import pytest

from aibench.rubric import (
    FIXTURE_SEVERITY,
    RUBRIC_DIMENSIONS,
    expected_severity,
    heuristic_checks,
    structured_profile,
)


def test_expected_severity_for_known_fixture() -> None:
    assert expected_severity("ECONM-004") == "CRITICAL"
    assert expected_severity("ECON-008") == "PASS"
    assert FIXTURE_SEVERITY["QR-003"] == "MAJOR"


def test_expected_severity_unknown_id() -> None:
    with pytest.raises(KeyError):
        expected_severity("NO-SUCH-CASE")


def test_heuristic_checks_flag_short_golden() -> None:
    warnings = heuristic_checks(
        {
            "golden_response": "too short",
            "corrected_reasoning": "still short but present",
            "assumptions": ["a"],
            "validation_steps": ["b"],
        }
    )
    assert any("golden_response is shorter" in item for item in warnings)


def test_structured_profile_is_not_a_single_verdict() -> None:
    scores = {name: 3 for name in RUBRIC_DIMENSIONS}
    scores["causal validity"] = 0
    profile = structured_profile(scores)
    assert profile["mean"] > 2
    assert "causal validity" in profile["failing_dimensions"]
    assert "not a single score" in profile["note"]
