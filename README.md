# Response evaluation cases

[![CI](https://github.com/pavanamthomas/ai-response-evaluation-benchmarks/actions/workflows/ci.yml/badge.svg)](https://github.com/pavanamthomas/ai-response-evaluation-benchmarks/actions)

Dr. Pavanam Thomas · [pavanamthomas](https://github.com/pavanamthomas) · thomaspavanam@gmail.com  
MIT License · Copyright 2026

A prompt, a candidate answer, and a written review. I am not scoring prose. I am asking whether the response named the right target, respected the information set and assumptions, used a valid method, survived a check, and limited its conclusion to what the argument actually supports.

The golden responses are reference reviews I wrote, not transcripts of a commercial chatbot. One author coded the YAML; there is no second-rater study.

## What the corpus covers

Economics and public policy; econometrics and causal inference; statistics; mathematics and quantitative reasoning. A later batch adds adversarial cases in:

- **machine learning** — supervised-selection leakage; ranking versus probability quality
- **retrieval-augmented generation** — retrieval / context / generation attribution; retrieved-text instruction hierarchy
- **Python computation** — numerical stability; stochastic ground-truth tolerance
- **SQL** — join cardinality; point-in-time information leakage

Notes on that extension: [`docs/ml_genai_sql_extension.md`](docs/ml_genai_sql_extension.md).

Fluent prose is cheap in this corpus. Correct objects, valid procedures, and independent checks are not.

## Review chain

**target object → assumptions/information set → method → validation → interpretation limit**

That is the backbone of [`GOLDEN_RESPONSE_STANDARD.md`](GOLDEN_RESPONSE_STANDARD.md). Skipping validation is how an invalid IV, a leaked feature table, an unstable computation, or an infeasible optimum can survive while still sounding plausible.

Reviews do not collapse to a single score as the only output.

| Object | Role |
| --- | --- |
| Ten rubric dimensions | Scored separately in `RUBRIC.md` |
| Structured profile | Diagnostic only; a high mean cannot hide a zero on a decisive dimension |
| `severity` | `CRITICAL`, `MAJOR`, `MINOR`, or `PASS` |
| `verdict` | `pass`, `fail`, or `correct_result_invalid_reasoning` |
| `earliest_failure_point` | First rubric dimension that breaks trust |
| Written fields | Explanation, corrected reasoning, golden response, assumptions, validation steps |

The `correct_result_invalid_reasoning` verdict matters in the technical domains. A toy SQL row can produce the intended value even when `LEAD` is not point-in-time safe; an AUC statement can be correct while the downstream probability-quality conclusion is invalid. Numerical agreement is not automatically methodological correctness.

One author wrote the YAML reviews. Cohen's kappa is checked on known label tables as arithmetic; it is not double-coding of the corpus. Details: [`docs/label_authorship.md`](docs/label_authorship.md) and [issue #5](https://github.com/pavanamthomas/ai-response-evaluation-benchmarks/issues/5).

## Layout

```text
RUBRIC.md
GOLDEN_RESPONSE_STANDARD.md
FLAGSHIP_REVIEW_CASE.md
cases/economics/  econometrics/  statistics/  mathematics/
cases/quantitative_reasoning/  mixed/
cases/machine_learning/  genai_rag/  python_computation/  sql_reasoning/
src/aibench/
scripts/validate_cases.py
tests/
```

Each YAML case includes `id`, `domain`, `title`, `prompt`, `candidate_response`, `verdict`, `error_classification`, `severity`, `earliest_failure_point`, `explanation`, `corrected_reasoning`, `golden_response`, `evaluator_notes`, `assumptions`, and `validation_steps`.

The corpus contains mixed verdicts. Tests also require at least two deliberate cases in every new technical domain and at least one technical `correct_result_invalid_reasoning` case.

## Examples I actually use when explaining the corpus

- `ML-001`: supervised SelectKBest run before the split contaminates the evaluation boundary.
- `ML-002`: higher ROC-AUC does not establish better probability accuracy when Brier score says otherwise.
- `RAG-001`: gold retrieved at rank two but removed by the context budget is a context-construction failure, not automatically a retrieval failure.
- `RAG-002`: retrieved document text remains evidence, not privileged instruction.
- `PY-001`: algebraically correct log-sum-exp can overflow before the logarithm sees a finite result.
- `PY-002`: a fixed seed makes Monte Carlo coverage repeatable, not exactly equal to its nominal probability.
- `SQL-001`: two one-to-many joins can multiply rows even when neither source contains duplicates.
- `SQL-002`: one numerically correct toy feature does not make a future-looking `LEAD` expression point-in-time safe.

These are constructed fixtures. They do not measure how often such failures occur in production systems.

I keep constructive implementations of some of the same objects in other repositories (identification, leakage, point-in-time SQL, retrieval traces). This corpus scores *answers*; those labs implement *procedures*.

## Install and checks

Python 3.11+:

```bash
pip install -e ".[dev]"
pytest -q
python scripts/validate_cases.py
python scripts/run_all.py
```

`validate_cases.py` requires at least 50 cases, unique ids, and full required defect-family coverage. CI runs the test suite and corpus checks.

Recorded failures: [`docs/failures_and_corrections.md`](docs/failures_and_corrections.md). Open work: [`ROADMAP.md`](ROADMAP.md) and GitHub Issues.

## Boundaries

- Constructed review problems, not production traffic.
- The technical domains are small on purpose and not exhaustive.
- No second independent human rater for the YAML corpus.
- No commercial judge-benchmark or production model-evaluation claim.
- A passing CI run establishes repository consistency, not universal correctness of every possible technical answer.

See `CITATION.cff`.
