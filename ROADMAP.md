# Roadmap

Current as of August 2026.

## In scope now

- Fifty YAML cases across economics, econometrics, statistics, mathematics, quantitative reasoning, and mixed items.
- Severity, defect taxonomy, multi-dimension rubric, golden-response standard, flagship staggered DiD review.
- CI: `python -m pytest` and `python scripts/validate_cases.py`.

## Failures that are part of the design

Candidate answers are constructed to fail in named ways. A `PASS` verdict is not the default. The corpus must keep mixed verdicts, including correct results with invalid reasoning.

Details: `docs/failures_and_corrections.md` and `docs/defect_taxonomy.md`.

## Open (issues)

1. Cases are constructed failure modes, not a sample of production model traffic. Expanding the corpus is useful only when a new defect family or a harder identification error is named.
2. Rubric profiles are not a single quality score. Automated aggregation beyond the documented profile would be a methodology change and needs an issue first.
3. Inter-rater reliability across human reviewers is not measured here.
4. Linking a case to a companion laboratory (econometrics, statistics, optimization) by id is informal; a machine-readable cross-walk is not implemented.

## Explicitly not in scope

- Golden responses presented as chatbot transcripts.
- Invented bibliographic citations except as a *candidate* defect that the review catches.
- A leaderboard that hides a zero on causal validity behind a high mean.

Close an issue only with a new case, a schema/test change, or a limitation sentence.
