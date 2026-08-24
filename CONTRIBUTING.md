# Contributing to the evaluation corpus

Useful work is a case where fluency and validity split, a rubric dimension that actually moves, or a domain extension that does not pretend to be multi-rater.

1. Open an issue naming the domain, the intended failure, and the label source.
2. Add a failing test before changing scoring behaviour.
3. Keep commits to one case or one scorer change.
4. Comment the intended failure and the single-author limit, not obvious YAML keys.

See `FLAGSHIP_REVIEW_CASE.md`, `docs/ml_genai_sql_extension.md`, `ROADMAP.md`, and `.github/workflows/ci.yml`.
