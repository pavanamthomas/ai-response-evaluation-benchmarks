# AI Response Evaluation Benchmarks

[![CI](https://github.com/pavanamthomas/ai-response-evaluation-benchmarks/actions/workflows/ci.yml/badge.svg)](https://github.com/pavanamthomas/ai-response-evaluation-benchmarks/actions)

Structured review cases for economics, econometrics, statistics, mathematics, machine learning, GenAI/RAG, Python computation, SQL reasoning, and quantitative AI answers.

Each item is a prompt, a candidate answer, and an explicit review. The object is not writing style. It is whether the response identified the right target, respected the information set and assumptions, used a valid method, survived a check, and limited its conclusion to what the evidence supports.

Dr. Pavanam Thomas · [pavanamthomas](https://github.com/pavanamthomas) · thomaspavanam@gmail.com  
MIT License · Copyright 2026

The golden responses are reference reviews, not transcripts of a commercial chatbot. One author coded the YAML corpus; there is no claimed second-rater study.

## What the corpus tests

The original core covers:

- economics and public policy;
- econometrics and causal inference;
- statistics and scientific inference;
- mathematics and quantitative reasoning.

A technical extension now adds deliberately adversarial cases in:

- **machine learning** — supervised-selection leakage and ranking versus probability quality;
- **GenAI/RAG** — retrieval/context/generation attribution and retrieved-text instruction hierarchy;
- **Python computation** — numerical stability and stochastic ground-truth tolerance;
- **SQL reasoning** — join cardinality and point-in-time information leakage.

See [`docs/ml_genai_sql_extension.md`](docs/ml_genai_sql_extension.md) for the reasoning behind the extension and its limits.

Fluent prose is cheap in this corpus. Correct objects, valid procedures, and independent checks are not.

## Review method

Every defensible review should make the following chain visible:

**target object → assumptions/information set → method → validation → interpretation limit**

That is the backbone of [`GOLDEN_RESPONSE_STANDARD.md`](GOLDEN_RESPONSE_STANDARD.md). Skipping the validation step is how an invalid IV, leaked feature table, unstable computation, or infeasible optimum can survive while still sounding plausible.

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

## Who coded the labels

One author wrote the YAML reviews. Cohen's kappa is checked on known label tables as arithmetic; it is not double-coding of the corpus. Details: [`docs/label_authorship.md`](docs/label_authorship.md) and [issue #5](https://github.com/pavanamthomas/ai-response-evaluation-benchmarks/issues/5).

## Repository layout

```text
RUBRIC.md
GOLDEN_RESPONSE_STANDARD.md
FLAGSHIP_REVIEW_CASE.md
docs/
cases/economics/
cases/econometrics/
cases/statistics/
cases/mathematics/
cases/quantitative_reasoning/
cases/mixed/
cases/machine_learning/
cases/genai_rag/
cases/python_computation/
cases/sql_reasoning/
src/aibench/
scripts/validate_cases.py
tests/
```

Each YAML case includes `id`, `domain`, `title`, `prompt`, `candidate_response`, `verdict`, `error_classification`, `severity`, `earliest_failure_point`, `explanation`, `corrected_reasoning`, `golden_response`, `evaluator_notes`, `assumptions`, and `validation_steps`.

The corpus contains mixed verdicts and the required defect families remain covered. Tests also require at least two deliberate cases in every new technical domain and at least one technical `correct_result_invalid_reasoning` case.

## Current technical examples

- `ML-001`: supervised SelectKBest run before the split contaminates the evaluation boundary.
- `ML-002`: higher ROC-AUC does not establish better probability accuracy when Brier score says otherwise.
- `RAG-001`: gold retrieved at rank two but removed by the context budget is a context-construction failure, not automatically a retrieval failure.
- `RAG-002`: retrieved document text remains evidence, not privileged instruction.
- `PY-001`: algebraically correct log-sum-exp can overflow before the logarithm sees a finite result.
- `PY-002`: a fixed seed makes Monte Carlo coverage repeatable, not exactly equal to its nominal probability.
- `SQL-001`: two one-to-many joins can multiply rows even when neither source contains duplicates.
- `SQL-002`: one numerically correct toy feature does not make a future-looking `LEAD` expression point-in-time safe.

These are constructed review fixtures. They do not measure how often such failures occur in production systems.

## Related implementation laboratories

Use the companion repositories to inspect constructive implementations behind several review questions:

- [computational-ml-stem-problem-forge](https://github.com/pavanamthomas/computational-ml-stem-problem-forge) — independent ground truth, adversarial computational cases, stochastic tolerance, numerical checks;
- [machine-learning-model-selection-lab](https://github.com/pavanamthomas/machine-learning-model-selection-lab) — leakage, grouped/time-aware validation, nested selection, imbalance, calibration;
- [genai-rag-evaluation-lab](https://github.com/pavanamthomas/genai-rag-evaluation-lab) — retrieval/context/generation failure partition;
- [sql-ml-feature-engineering-lab](https://github.com/pavanamthomas/sql-ml-feature-engineering-lab) — point-in-time SQL and sentinel tests;
- [pytorch-deep-learning-lab](https://github.com/pavanamthomas/pytorch-deep-learning-lab) — analytic gradients, finite differences, and autograd;
- [econometrics-causal-inference-lab](https://github.com/pavanamthomas/econometrics-causal-inference-lab) — identification and causal estimands;
- [statistical-reasoning-validation](https://github.com/pavanamthomas/statistical-reasoning-validation) — probability and inferential validation.

## Install and checks

Python 3.11+:

```bash
pip install -e ".[dev]"
pytest -q
python scripts/validate_cases.py
python scripts/run_all.py
```

`validate_cases.py` requires at least 50 cases, unique ids, and full required defect-family coverage. CI runs the test suite and corpus checks.

Recorded failures and corrections: [`docs/failures_and_corrections.md`](docs/failures_and_corrections.md). Open work: [`ROADMAP.md`](ROADMAP.md) and GitHub Issues.

## Boundaries

- The cases are constructed review problems, not production traffic.
- The new technical domains are intentionally small and not exhaustive.
- There is no second independent human rater for the YAML corpus.
- No commercial LLM-judge benchmark or production model-evaluation claim is made.
- A passing CI run establishes repository consistency, not universal correctness of every possible technical answer.

## Citation

See `CITATION.cff`.
