"""Case schema: required fields, allowed vocabularies, and dict validation.

Validation is pydantic-free. Cases are ordinary mappings checked against a
closed set of fields and enumerations.
"""

from __future__ import annotations

from typing import Any, Mapping

REQUIRED_FIELDS: tuple[str, ...] = (
    "id",
    "domain",
    "title",
    "prompt",
    "candidate_response",
    "verdict",
    "error_classification",
    "severity",
    "earliest_failure_point",
    "explanation",
    "corrected_reasoning",
    "golden_response",
    "evaluator_notes",
    "assumptions",
    "validation_steps",
)

VALID_DOMAINS: frozenset[str] = frozenset(
    {
        "economics",
        "econometrics",
        "statistics",
        "mathematics",
        "quantitative_reasoning",
        "mixed",
    }
)

VALID_SEVERITIES: frozenset[str] = frozenset({"CRITICAL", "MAJOR", "MINOR", "PASS"})

VALID_VERDICTS: frozenset[str] = frozenset(
    {"pass", "fail", "correct_result_invalid_reasoning"}
)

VALID_FAILURE_POINTS: frozenset[str] = frozenset(
    {
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
        "none",
    }
)

LIST_FIELDS: frozenset[str] = frozenset(
    {"error_classification", "assumptions", "validation_steps"}
)

NONEMPTY_TEXT_FIELDS: frozenset[str] = frozenset(
    {
        "id",
        "title",
        "prompt",
        "candidate_response",
        "explanation",
        "corrected_reasoning",
        "golden_response",
        "evaluator_notes",
    }
)


class CaseValidationError(ValueError):
    """Raised when a case mapping fails schema checks."""


def _as_text(value: Any) -> str:
    if not isinstance(value, str):
        raise CaseValidationError("expected a string")
    return value.strip()


def validate_case(data: Mapping[str, Any], *, source: str = "") -> dict[str, Any]:
    """Validate one case mapping and return a normalized copy.

    Parameters
    ----------
    data:
        Parsed YAML mapping.
    source:
        Optional path or label included in error messages.
    """
    prefix = f"{source}: " if source else ""
    if not isinstance(data, Mapping):
        raise CaseValidationError(f"{prefix}case must be a mapping")

    missing = [field for field in REQUIRED_FIELDS if field not in data]
    if missing:
        raise CaseValidationError(
            f"{prefix}missing required field(s): {', '.join(missing)}"
        )

    unknown = sorted(set(data) - set(REQUIRED_FIELDS))
    if unknown:
        raise CaseValidationError(
            f"{prefix}unknown field(s): {', '.join(unknown)}"
        )

    case: dict[str, Any] = {}
    for field in REQUIRED_FIELDS:
        case[field] = data[field]

    case_id = _as_text(case["id"])
    if not case_id:
        raise CaseValidationError(f"{prefix}id must be a non-empty string")
    case["id"] = case_id

    domain = _as_text(case["domain"])
    if domain not in VALID_DOMAINS:
        raise CaseValidationError(
            f"{prefix}{case_id}: domain must be one of {sorted(VALID_DOMAINS)}"
        )
    case["domain"] = domain

    verdict = _as_text(case["verdict"]).lower()
    if verdict not in VALID_VERDICTS:
        raise CaseValidationError(
            f"{prefix}{case_id}: verdict must be one of {sorted(VALID_VERDICTS)}"
        )
    case["verdict"] = verdict

    severity = _as_text(case["severity"]).upper()
    if severity not in VALID_SEVERITIES:
        raise CaseValidationError(
            f"{prefix}{case_id}: severity must be one of {sorted(VALID_SEVERITIES)}"
        )
    case["severity"] = severity

    if verdict == "pass" and severity != "PASS":
        raise CaseValidationError(
            f"{prefix}{case_id}: verdict 'pass' requires severity PASS"
        )
    if verdict != "pass" and severity == "PASS":
        raise CaseValidationError(
            f"{prefix}{case_id}: severity PASS requires verdict 'pass'"
        )

    failure_point = _as_text(case["earliest_failure_point"]).lower()
    if failure_point not in VALID_FAILURE_POINTS:
        raise CaseValidationError(
            f"{prefix}{case_id}: earliest_failure_point must be one of "
            f"{sorted(VALID_FAILURE_POINTS)}"
        )
    if verdict == "pass" and failure_point != "none":
        raise CaseValidationError(
            f"{prefix}{case_id}: passing cases must set earliest_failure_point to 'none'"
        )
    if verdict != "pass" and failure_point == "none":
        raise CaseValidationError(
            f"{prefix}{case_id}: non-passing cases must name an earliest failure point"
        )
    case["earliest_failure_point"] = failure_point

    for field in NONEMPTY_TEXT_FIELDS:
        if field == "id":
            continue
        text = case[field]
        if not isinstance(text, str) or not text.strip():
            raise CaseValidationError(
                f"{prefix}{case_id}: {field} must be a non-empty string"
            )
        case[field] = text.strip()

    for field in LIST_FIELDS:
        values = case[field]
        if not isinstance(values, list) or not values:
            raise CaseValidationError(
                f"{prefix}{case_id}: {field} must be a non-empty list"
            )
        cleaned: list[str] = []
        for item in values:
            if not isinstance(item, str) or not item.strip():
                raise CaseValidationError(
                    f"{prefix}{case_id}: {field} entries must be non-empty strings"
                )
            cleaned.append(item.strip())
        case[field] = cleaned

    if verdict == "pass" and case["error_classification"] != ["none"]:
        raise CaseValidationError(
            f"{prefix}{case_id}: passing cases must set error_classification to [none]"
        )

    return case
