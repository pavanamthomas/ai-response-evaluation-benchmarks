# Roadmap

Current as of August 2026.

## In scope now

- Fifty YAML cases across economics, econometrics, statistics, mathematics, quantitative reasoning, and mixed items.
- Severity, defect taxonomy, multi-dimension rubric, golden-response standard, flagship staggered DiD review.
- `verdict_from_profile` fails on a zero in causal validity or evidence discipline; Cohen's kappa is checked on known tables.
- CI: `python -m pytest` and `python scripts/validate_cases.py`.

## Failures that are part of the design

Candidate answers are constructed to fail in named ways. A `PASS` verdict is not the default. The corpus must keep mixed verdicts, including correct results with invalid reasoning.

Details: `docs/failures_and_corrections.md` and `docs/defect_taxonomy.md`.

## Open (issues)

1. Cases remain constructed failure modes, not production traffic.
2. Cohen's kappa is implemented as arithmetic on label vectors, not as a second-rater study of the YAML corpus.

## Explicitly not in scope

- Golden responses presented as chatbot transcripts.
- Invented bibliographic citations except as a *candidate* defect that the review catches.
- A leaderboard that hides a zero on causal validity behind a high mean.

Close an issue only with a new case, a schema/test change, or a limitation sentence.
