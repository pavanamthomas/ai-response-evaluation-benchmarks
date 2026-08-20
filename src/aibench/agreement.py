"""Agreement statistics for two label sequences.

Cohen's kappa here is arithmetic on known tables. It is not a second-rater
study of the YAML corpus.
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Sequence


def cohens_kappa(rater_a: Sequence[object], rater_b: Sequence[object]) -> float:
    """Cohen's kappa for two categorical label vectors of equal length."""
    a = list(rater_a)
    b = list(rater_b)
    if not a or len(a) != len(b):
        raise ValueError("label vectors must be non-empty and the same length")

    n = len(a)
    po = sum(x == y for x, y in zip(a, b, strict=True)) / n
    labels = set(a) | set(b)
    freq_a = Counter(a)
    freq_b = Counter(b)
    pe = sum((freq_a[lab] / n) * (freq_b[lab] / n) for lab in labels)
    if abs(1.0 - pe) < 1e-15:
        return 1.0 if po >= 1.0 - 1e-15 else 0.0
    return (po - pe) / (1.0 - pe)
