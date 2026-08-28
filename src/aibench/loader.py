"""Load YAML evaluation cases from the repository tree."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from aibench.schema import CaseValidationError, validate_case


class CaseLoadError(ValueError):
    """Raised when files cannot be loaded or ids collide."""


def repository_root(start: Path | None = None) -> Path:
    """Return the repository root (directory containing ``pyproject.toml``)."""
    anchor = (start or Path(__file__)).resolve()
    if anchor.is_file():
        anchor = anchor.parent
    for candidate in (anchor, *anchor.parents):
        if (candidate / "pyproject.toml").is_file() and (candidate / "cases").is_dir():
            return candidate
    raise CaseLoadError("could not locate repository root with pyproject.toml and cases/")


def case_files(root: Path | None = None) -> list[Path]:
    """Return YAML case paths in sorted order."""
    base = (root or repository_root()) / "cases"
    files = sorted(base.glob("*/*.yaml")) + sorted(base.glob("*/*.yml"))
    return files


def load_cases(root: Path | None = None) -> list[dict[str, Any]]:
    """Load and validate every case file under ``cases/``.

    Fails if a file is missing required fields or if ids are duplicated.
    """
    base = root or repository_root()
    files = case_files(base)
    if not files:
        raise CaseLoadError(f"no YAML case files found under {base / 'cases'}")

    loaded: list[dict[str, Any]] = []
    seen: dict[str, Path] = {}
    for path in files:
        raw = yaml.safe_load(path.read_text(encoding="utf-8"))
        try:
            case = validate_case(raw, source=str(path))
        except CaseValidationError as exc:
            raise CaseLoadError(str(exc)) from exc
        case_id = case["id"]
        if case_id in seen:
            raise CaseLoadError(
                f"duplicate id {case_id!r}: {seen[case_id]} and {path}"
            )
        seen[case_id] = path
        case["_source"] = str(path.relative_to(base))
        loaded.append(case)
    return loaded
