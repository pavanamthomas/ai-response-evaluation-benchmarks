"""Schema validation tests."""

from __future__ import annotations

import pytest

from aibench.schema import CaseValidationError, validate_case

VALID = {
    "id": "TEST-001",
    "domain": "economics",
    "title": "Fixture",
    "prompt": "State whether GDP is a value-added concept.",
    "candidate_response": "GDP sums value added, so intermediate sales are not double-counted.",
    "verdict": "pass",
    "error_classification": ["none"],
    "severity": "PASS",
    "earliest_failure_point": "none",
    "explanation": "The candidate uses the value-added definition correctly.",
    "corrected_reasoning": "No correction required; the reasoning is already aligned with the national accounts identity.",
    "golden_response": (
        "GDP is the market value of final goods and services, equivalently the "
        "sum of value added. Summing all firm revenues would double-count "
        "intermediate inputs. That is the relevant definition for this prompt."
    ),
    "evaluator_notes": "Passing fixture used in schema tests.",
    "assumptions": ["Standard SNA production boundary."],
    "validation_steps": ["Check the identity: output minus intermediates equals value added."],
}


def test_valid_case_normalizes_enums() -> None:
    out = validate_case(VALID)
    assert out["verdict"] == "pass"
    assert out["severity"] == "PASS"
    assert out["domain"] == "economics"


def test_missing_field_rejected() -> None:
    data = dict(VALID)
    del data["golden_response"]
    with pytest.raises(CaseValidationError, match="missing required field"):
        validate_case(data, source="memory")


def test_unknown_field_rejected() -> None:
    data = dict(VALID)
    data["extra"] = "no"
    with pytest.raises(CaseValidationError, match="unknown field"):
        validate_case(data)


def test_empty_list_rejected() -> None:
    data = dict(VALID)
    data["assumptions"] = []
    with pytest.raises(CaseValidationError, match="assumptions"):
        validate_case(data)


def test_pass_requires_severity_pass() -> None:
    data = dict(VALID)
    data["severity"] = "MAJOR"
    with pytest.raises(CaseValidationError, match="verdict 'pass'"):
        validate_case(data)


def test_fail_cannot_use_severity_pass() -> None:
    data = dict(VALID)
    data["verdict"] = "fail"
    data["error_classification"] = ["OVB"]
    data["earliest_failure_point"] = "causal validity"
    with pytest.raises(CaseValidationError, match="severity PASS requires"):
        validate_case(data)
