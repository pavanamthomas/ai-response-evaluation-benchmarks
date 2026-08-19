"""Agreement statistics for two label sequences.

These functions check the arithmetic of Cohen's kappa on known tables.
They are not a second-rater study of the YAML corpus.
"""

from __future__ import annotations

import numpy as np
from numpy.typing import ArrayLike


def cohens_kappa(rater_a: ArrayLike, rater_b: ArrayLike) -> float:
    """Cohen's kappa for two categorical label vectors of equal length."""
    a = np.asarray(rater_a).reshape(-1)
    b = np.asarray(rater_b).reshape(-1)
    if a.size != b.size or a.size == 0:
        raise ValueError("label vectors must be non-empty and the same length")
    labels = np.unique(np.concatenate([a, b]))
    n = a.size
    po = float(np.mean(a == b))
    pe = 0.0
    for lab in labels:
        pe += float(np.mean(a == lab) * np.mean(b == lab))
    if abs(1.0 - pe) < 1e-15:
        return 1.0 if po >= 1.0 - 1e-15 else 0.0
    return float((po - pe) / (1.0 - pe))
