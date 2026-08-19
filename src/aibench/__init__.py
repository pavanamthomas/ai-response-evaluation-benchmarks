"""Public API for loading and validating evaluation cases."""

from aibench.loader import CaseLoadError, load_cases, repository_root
from aibench.schema import REQUIRED_FIELDS, CaseValidationError, validate_case
from aibench.validate import REQUIRED_DEFECT_FAMILIES, ValidationReport, validate_corpus

__all__ = [
    "REQUIRED_DEFECT_FAMILIES",
    "REQUIRED_FIELDS",
    "CaseLoadError",
    "CaseValidationError",
    "ValidationReport",
    "load_cases",
    "repository_root",
    "validate_case",
    "validate_corpus",
]

__version__ = "0.1.0"
