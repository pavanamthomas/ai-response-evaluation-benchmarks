# AI Response Evaluation Benchmarks

[![CI](https://github.com/pavanamthomas/ai-response-evaluation-benchmarks/actions/workflows/ci.yml/badge.svg)](https://github.com/pavanamthomas/ai-response-evaluation-benchmarks/actions)

Benchmark cases for evaluating economics, econometrics, statistics, mathematics, and quantitative AI responses.

This repository is a **scoring laboratory**: each item is a prompt, a candidate answer, and an expert review. The subject matter is the evaluation of quantitative reasoning. The golden responses are written as an economist and econometrician would write an accepted examination solution. They are not transcripts of a commercial chatbot.

**Author:** Dr. Pavanam Thomas ([GitHub](https://github.com/pavanamthomas), thomaspavanam@gmail.com)  
**License:** MIT. Copyright 2026 Dr. Pavanam Thomas.

## What this is for

Use the cases to train or audit reviewers who must judge answers in:

- economics and public policy
- econometrics and causal inference
- statistics and scientific inference
- mathematics at the level expected of a mathematically trained economist
- quantitative reasoning (units, compounding, ambiguous averages)

Typical setting: an expert-review or evaluation role in which fluency is cheap and **identification, evidence discipline, and correct objects** are not.

## Methodology

Every golden response, and every fair candidate review, should be reconstructible as:

**Problem → formalization → assumptions → computation or estimation → validation → interpretation → limitations**

That sequence is the backbone of `GOLDEN_RESPONSE_STANDARD.md`. Skipping “validation” is how invalid IV, leaked features, and infeasible optima survive.

## How judgement is recorded

Reviews **do not** collapse to a single score as the only output.

| Object | Role |
| --- | --- |
| Ten rubric dimensions | Scored separately (`RUBRIC.md`) |
| Structured profile | Optional diagnostic (mean, minimum, failing dimensions). **Expert judgement is not a single score.** |
| `severity` | `CRITICAL` / `MAJOR` / `MINOR` / `PASS` (`docs/severity.md`) |
| `verdict` | `pass` / `fail` / `correct_result_invalid_reasoning` |
| `earliest_failure_point` | First rubric dimension that breaks trust |
| Written fields | `explanation`, `corrected_reasoning`, `golden_response` |

A high mean with a zero on causal validity is still a fail. See the flagship staggered difference-in-differences review.

## Repository layout

```text
RUBRIC.md
GOLDEN_RESPONSE_STANDARD.md
FLAGSHIP_REVIEW_CASE.md
docs/severity.md
docs/defect_taxonomy.md
cases/economics/
cases/econometrics/
cases/statistics/
cases/mathematics/
cases/quantitative_reasoning/
cases/mixed/
src/aibench/          # schema, loader, rubric helpers, corpus checks
scripts/validate_cases.py
tests/
```

Each YAML case includes: `id`, `domain`, `title`, `prompt`, `candidate_response`, `verdict`, `error_classification`, `severity`, `earliest_failure_point`, `explanation`, `corrected_reasoning`, `golden_response`, `evaluator_notes`, `assumptions`, `validation_steps`.

The corpus is constructed so that **all** defect families in `docs/defect_taxonomy.md` appear at least once. Verdicts are mixed: some items `PASS`; some report a correct final result with invalid reasoning.

## Cross-links

This benchmark is meant to sit beside three companion laboratories in the same quantitative portfolio:

- [econometrics-causal-inference-lab](https://github.com/pavanamthomas/econometrics-causal-inference-lab) — identification designs, diagnostics, and estimands (LATE vs ATE, staggered adoption, IV).
- [statistical-reasoning-validation](https://github.com/pavanamthomas/statistical-reasoning-validation) — *p*-values, intervals, leakage, overfitting, and calibration of claims.
- [optimization-decision-models](https://github.com/pavanamthomas/optimization-decision-models) — constraints, feasibility, and boundary conditions in decision models.

Use those repositories for constructive methods. Use **this** repository to score whether a written answer respected those methods.

## Install and checks

Python 3.11+:

```bash
pip install -e ".[dev]"
pytest -q
python scripts/validate_cases.py
python scripts/run_all.py
```

`validate_cases.py` requires at least 50 cases, unique ids, and full defect-family coverage. CI (`.github/workflows/ci.yml`) runs the same commands.

Recorded corpus failures (mixed verdicts, required defect families, flagship length): `docs/failures_and_corrections.md`. Open work: `ROADMAP.md` and GitHub Issues. Process: `docs/lab_process.md`.

## Citation

See `CITATION.cff`.
