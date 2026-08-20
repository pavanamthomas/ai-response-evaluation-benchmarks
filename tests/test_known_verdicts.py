"""Corpus-level known-verdict and coverage tests."""

from __future__ import annotations

from aibench.loader import load_cases, repository_root
from aibench.rubric import FIXTURE_SEVERITY, heuristic_checks
from aibench.validate import REQUIRED_DEFECT_FAMILIES, MINIMUM_CASE_COUNT, validate_corpus


def test_at_least_fifty_cases() -> None:
    cases = load_cases()
    assert len(cases) >= MINIMUM_CASE_COUNT


def test_required_defect_families_present() -> None:
    cases = load_cases()
    report = validate_corpus(cases)
    assert report.missing_families == []
    observed = {item for case in cases for item in case["error_classification"]}
    for family in REQUIRED_DEFECT_FAMILIES:
        assert family in observed


def test_known_fixtures_have_expected_severity() -> None:
    by_id = {case["id"]: case for case in load_cases()}
    for case_id, severity in FIXTURE_SEVERITY.items():
        assert case_id in by_id, f"missing fixture {case_id}"
        assert by_id[case_id]["severity"] == severity


def test_heuristic_checks_pass_on_corpus() -> None:
    for case in load_cases():
        assert heuristic_checks(case) == [], case["id"]


def test_flagship_file_exists_and_is_nontrivial() -> None:
    path = repository_root() / "FLAGSHIP_REVIEW_CASE.md"
    assert path.is_file()
    text = path.read_text(encoding="utf-8")
    assert len(text) >= 8000
    lowered = text.lower()
    for token in ("staggered", "difference-in-differences", "parallel", "placebo"):
        assert token in lowered


def test_label_authorship_states_one_coder_and_no_second_rater() -> None:
    path = repository_root() / "docs" / "label_authorship.md"
    assert path.is_file()
    text = path.read_text(encoding="utf-8").lower()
    assert "one author" in text
    assert "not a second-rater" in text
    assert "none will be invented" in text


def test_verdicts_are_not_uniform() -> None:
    cases = load_cases()
    verdicts = {case["verdict"] for case in cases}
    assert "pass" in verdicts
    assert "fail" in verdicts
    assert "correct_result_invalid_reasoning" in verdicts


def test_math_plus_quantitative_reasoning_at_least_ten() -> None:
    cases = load_cases()
    n = sum(
        1
        for case in cases
        if case["domain"] in {"mathematics", "quantitative_reasoning"}
    )
    assert n >= 10
