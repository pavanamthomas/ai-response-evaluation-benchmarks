"""Rubric helper tests."""

from __future__ import annotations

import pytest

from aibench.rubric import (
    FIXTURE_SEVERITY,
    RUBRIC_DIMENSIONS,
    expected_severity,
    heuristic_checks,
    structured_profile,
    verdict_from_profile,
)


def test_expected_severity_for_known_fixture() -> None:
    assert expected_severity("ECONM-004") == "CRITICAL"
    assert expected_severity("ECON-008") == "PASS"
    assert FIXTURE_SEVERITY["QR-003"] == "MAJOR"


def test_expected_severity_unknown_id() -> None:
    with pytest.raises(KeyError):
        expected_severity("NO-SUCH-CASE")


def _all_threes(**overrides: int) -> dict[str, int]:
    scores = {name: 3 for name in RUBRIC_DIMENSIONS}
    scores.update(overrides)
    return scores


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
    profile = structured_profile(_all_threes(**{"causal validity": 0}))
    assert profile["mean"] > 2
    assert "causal validity" in profile["failing_dimensions"]
    assert "not a single score" in profile["note"]
    assert verdict_from_profile(profile) == "fail"


def test_zero_causal_validity_fails_despite_high_mean() -> None:
    profile = structured_profile(_all_threes(**{"causal validity": 0}))
    assert abs(profile["mean"] - 2.7) < 1e-12
    assert verdict_from_profile(profile) == "fail"


def test_zero_evidence_discipline_fails() -> None:
    profile = structured_profile(_all_threes(**{"evidence discipline": 0}))
    assert verdict_from_profile(profile) == "fail"


def test_all_threes_is_a_pass() -> None:
    profile = structured_profile(_all_threes())
    assert profile["minimum"] == 3
    assert profile["failing_dimensions"] == []
    assert verdict_from_profile(profile) == "pass"
