"""Cohen's kappa on known tables."""

from __future__ import annotations

import pytest

from aibench.agreement import cohens_kappa


def test_perfect_agreement_is_one() -> None:
    a = ["PASS", "PASS", "FAIL", "FAIL"]
    b = ["PASS", "PASS", "FAIL", "FAIL"]
    assert abs(cohens_kappa(a, b) - 1.0) < 1e-12


def test_balanced_disagreement_is_minus_one() -> None:
    a = ["PASS", "PASS", "FAIL", "FAIL"]
    b = ["FAIL", "FAIL", "PASS", "PASS"]
    assert abs(cohens_kappa(a, b) + 1.0) < 1e-12


def test_two_by_two_table_kappa_is_one_half() -> None:
    # Counts: (0,0)=10, (0,1)=2, (1,0)=4, (1,1)=8. n=24.
    # po = 18/24 = 0.75. Marginal products give pe = 0.5. kappa = 0.5.
    a = [0] * 12 + [1] * 12
    b = [0] * 10 + [1] * 2 + [0] * 4 + [1] * 8
    assert abs(cohens_kappa(a, b) - 0.5) < 1e-12


def test_identical_constant_labels_are_one() -> None:
    assert cohens_kappa(["PASS"] * 6, ["PASS"] * 6) == 1.0


def test_length_mismatch_and_empty_vectors_are_rejected() -> None:
    with pytest.raises(ValueError):
        cohens_kappa(["PASS"], ["PASS", "FAIL"])
    with pytest.raises(ValueError):
        cohens_kappa([], [])
