"""Integrity checks for the ML-facing extension of the review corpus."""

from __future__ import annotations

from collections import Counter

from aibench.loader import load_cases


def test_new_domains_have_deliberate_cases() -> None:
    cases = load_cases()
    counts = Counter(case["domain"] for case in cases)
    for domain in ("machine_learning", "genai_rag", "python_computation", "sql_reasoning"):
        assert counts[domain] >= 2


def test_new_domains_include_correct_result_invalid_reasoning() -> None:
    cases = load_cases()
    technical = [
        case
        for case in cases
        if case["domain"] in {"machine_learning", "genai_rag", "python_computation", "sql_reasoning"}
    ]
    assert any(case["verdict"] == "correct_result_invalid_reasoning" for case in technical)


def test_new_cases_name_validation_steps_not_only_verdicts() -> None:
    cases = load_cases()
    technical = [case for case in cases if case["id"].startswith(("ML-", "RAG-", "PY-", "SQL-"))]
    assert technical
    for case in technical:
        assert len(case["validation_steps"]) >= 3
        assert case["golden_response"].strip()
        assert case["explanation"].strip()
