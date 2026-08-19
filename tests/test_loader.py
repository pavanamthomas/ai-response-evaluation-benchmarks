"""Loader tests: corpus load, duplicate ids, missing fields."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from aibench.loader import CaseLoadError, load_cases, repository_root
from aibench.schema import REQUIRED_FIELDS


def test_repository_root_contains_cases() -> None:
    root = repository_root()
    assert (root / "cases").is_dir()
    assert (root / "pyproject.toml").is_file()


def test_all_cases_load() -> None:
    cases = load_cases()
    assert cases
    ids = [case["id"] for case in cases]
    assert len(ids) == len(set(ids))
    for case in cases:
        for field in REQUIRED_FIELDS:
            assert field in case


def test_duplicate_id_rejected(tmp_path: Path) -> None:
    cases_dir = tmp_path / "cases" / "economics"
    cases_dir.mkdir(parents=True)
    (tmp_path / "pyproject.toml").write_text("[project]\nname='tmp'\n", encoding="utf-8")
    payload = {
        "id": "DUP-001",
        "domain": "economics",
        "title": "Duplicate",
        "prompt": "Prompt text for the duplicate-id fixture.",
        "candidate_response": "A candidate answer long enough to be a string.",
        "verdict": "fail",
        "error_classification": ["incomplete answer"],
        "severity": "MINOR",
        "earliest_failure_point": "completeness",
        "explanation": "Used only to test duplicate id detection.",
        "corrected_reasoning": "The second file should never be accepted beside the first.",
        "golden_response": (
            "This golden response exists only so the schema accepts the fixture "
            "before the loader rejects the colliding identifier."
        ),
        "evaluator_notes": "Duplicate-id fixture.",
        "assumptions": ["Test fixture."],
        "validation_steps": ["Confirm the loader raises CaseLoadError."],
    }
    (cases_dir / "a.yaml").write_text(yaml.safe_dump(payload), encoding="utf-8")
    (cases_dir / "b.yaml").write_text(yaml.safe_dump(payload), encoding="utf-8")
    with pytest.raises(CaseLoadError, match="duplicate id"):
        load_cases(tmp_path)


def test_missing_field_file_rejected(tmp_path: Path) -> None:
    cases_dir = tmp_path / "cases" / "economics"
    cases_dir.mkdir(parents=True)
    (tmp_path / "pyproject.toml").write_text("[project]\nname='tmp'\n", encoding="utf-8")
    payload = {
        "id": "MISS-001",
        "domain": "economics",
        "title": "Missing field",
        "prompt": "Prompt",
        "candidate_response": "Answer",
        "verdict": "fail",
        "error_classification": ["incomplete answer"],
        "severity": "MINOR",
        "earliest_failure_point": "completeness",
        "explanation": "Missing golden_response on purpose.",
        "corrected_reasoning": "Should fail schema validation.",
        "evaluator_notes": "Missing-field fixture.",
        "assumptions": ["Test fixture."],
        "validation_steps": ["Confirm missing field is rejected."],
    }
    (cases_dir / "missing.yaml").write_text(yaml.safe_dump(payload), encoding="utf-8")
    with pytest.raises(CaseLoadError, match="missing required field"):
        load_cases(tmp_path)
