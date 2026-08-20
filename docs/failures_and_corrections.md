# Failures and corrections

In this repository the **candidate answer** is the object that fails. The correction is the review: earliest failure point, severity, and golden response. The test suite fails if those failures are edited away.

| Failure class | What goes wrong | Correction in the review | Locked by | What remains unknown |
| --- | --- | --- | --- | --- |
| Uniform verdicts | A corpus of only `PASS` or only `fail` cannot train a reviewer | Mixed `pass` / `fail` / `correct_result_invalid_reasoning` | `tests/test_known_verdicts.py::test_verdicts_are_not_uniform` | Live traffic mix |
| Missing defect family | A taxonomy item with no case is an unchecked claim | Every family in `REQUIRED_DEFECT_FAMILIES` appears at least once | `tests/test_known_verdicts.py::test_required_defect_families_present` | Families not yet named |
| Flagship DiD review gutted | Staggered adoption, parallel trends, placebo would disappear | Length and token checks on `FLAGSHIP_REVIEW_CASE.md` | `tests/test_known_verdicts.py::test_flagship_file_exists_and_is_nontrivial` | Other policy settings |
| Collapsing the rubric to one score | A high mean can hide a zero on causal validity | Ten dimensions; `verdict_from_profile` fails on that zero | `tests/test_rubric.py::test_zero_causal_validity_fails_despite_high_mean` | Weights for hiring workflows |
| Treating kappa on label tables as a second-rater study | Agreement arithmetic is not double-coding of the YAML corpus | Known-table checks only; limitation kept | `tests/test_agreement.py` | Human double-coding of severity and failure point |
| Golden response as chatbot paste | Would misrepresent authorship | Expert examination style; no commercial-model attribution | README; `GOLDEN_RESPONSE_STANDARD.md` | Wording variants that remain valid |
| Invented citation in a *golden* answer | That would be a defect in the key, not in the candidate | Allowed only in `candidate_response` when the case is about fabricated evidence | Reviewer notes in those YAML files | Bibliographic completeness in other domains |

Process: `docs/lab_process.md`. Open extensions: `ROADMAP.md`. Companion methods: econometrics, statistics, and optimization laboratories.
