# Roadmap

Rater, domain, and scoring limits of the frozen YAML corpus (August 2026).

## In scope now

- Fifty-eight YAML review cases spanning economics, econometrics, statistics, mathematics, quantitative reasoning, mixed items, machine learning, GenAI/RAG, Python computation, and SQL reasoning.
- Severity, defect taxonomy, multi-dimension rubric, golden-response standard, and the flagship staggered-DiD review.
- Explicit `correct_result_invalid_reasoning` cases where the final value or a partial statement is right but the method does not justify the conclusion.
- Technical-domain cases for supervised-selection leakage, ranking versus calibration, RAG stage attribution, retrieved-text instruction hierarchy, log-sum-exp stability, Monte Carlo tolerance, join cardinality, and point-in-time SQL leakage.
- `verdict_from_profile` fails on a zero in causal validity or evidence discipline; Cohen's kappa is checked on known label tables.
- CI runs the test suite, corpus validation, and reproduction checks. Tests require deliberate cases in each new technical domain and preserve verdict diversity.

## Failures that are part of the design

Candidate answers are constructed to fail in named ways. A `PASS` verdict is not the default, and fluent wording cannot compensate for a broken target object, invalid information set, unstable computation, or unsupported inference.

The technical extension follows the same principle: identify the earliest substantive failure, give the corrected reasoning, and state how correctness would be independently checked.

Details: `docs/failures_and_corrections.md`, `docs/defect_taxonomy.md`, and `docs/ml_genai_sql_extension.md`.

## Remaining bounds

1. Cases remain constructed failure modes, not production traffic or a measure of model prevalence in the wild.
2. Cohen's kappa is arithmetic on known label vectors, not a second-rater study of the YAML corpus ([issue #5](https://github.com/pavanamthomas/ai-response-evaluation-benchmarks/issues/5)).
3. The new ML/GenAI/Python/SQL domains are intentionally small. Coverage is not exhaustive, and case count is not treated as evidence of domain completeness.
4. There is no commercial LLM judge or automated judge benchmark in this repository; the primary object remains explicit expert review against the written rubric.

## Explicitly not in scope

- Golden responses presented as chatbot transcripts.
- Invented bibliographic citations except as a candidate defect that the review catches.
- A leaderboard that hides a zero on causal validity or evidence discipline behind a high mean.
- Claims that eight initial technical cases constitute a comprehensive ML/GenAI/SQL benchmark.

Close an issue only with a new substantive case, a schema/test change, executable validation evidence, or a limitation sentence that narrows the claim.
