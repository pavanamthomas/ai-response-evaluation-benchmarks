# Evaluation rubric

Score the ten dimensions **separately**. Do not collapse them into a single total as the only output of a review. A structured profile (means, minima, lists of failing dimensions) is allowed as a diagnostic. It is not the evaluation.

Expert judgement in this repository is a **severity label**, a **verdict**, an **earliest failure point**, and a written explanation. Those objects can disagree with a high average of dimension scores. A zero on causal validity can dominate nines elsewhere.

Each dimension is scored on `{0, 1, 2, 3}` when a numeric profile is requested:

| Score | Meaning |
| --- | --- |
| 3 | Meets the standard a careful examiner would accept for this prompt |
| 2 | Usable with a local patch |
| 1 | Material defect; conclusion would change if corrected |
| 0 | Broken, fabricated, or unsafe on this dimension |

## Dimensions

### 1. Task interpretation

Did the response answer the prompt that was asked, including the requested object (definition, derivation, estimate, recommendation, or caveat list)? Penalize silent substitution of an easier question. If the prompt is ambiguous, a high score requires stating the reading that is being used.

### 2. Conceptual correctness

Are the economic, statistical, or mathematical objects the right objects? Examples: value added versus revenue; LATE versus ATE; elasticity versus semi-elasticity; estimator versus estimand.

### 3. Mathematical correctness

Are algebra, calculus, optimization, and identities valid? A correct qualitative story with an invalid derivation scores low here even if other dimensions are high.

### 4. Statistical correctness

Are probability, sampling, inference, and predictive claims valid under the stated stochastic model? This includes *p*-values, confidence intervals, Bayes, leakage, and overfitting.

### 5. Causal validity

Would the stated assumptions identify the claimed causal object? This is where correlation/causation, OVB, IV, DiD, staggered adoption, and placebo logic live. Associational language used honestly can score well.

### 6. Assumptions

Are maintained assumptions explicit, necessary, and not contradicted by information in the prompt? Hidden assumptions that do the identifying work score low.

### 7. Completeness

Are the required steps present: formalization, computation or estimation, validation, interpretation, limitations? An elegant fragment that omits a requested part scores low.

### 8. Clarity

Could a second examiner reconstruct the argument? Penalize contradictions, undefined notation, and conclusions that do not follow from the body. Do not reward fluency that conceals a wrong claim.

### 9. Evidence discipline

Are empirical statements sourced or clearly labeled as hypothetical? Invented citations, fake consensus, and unsourced magnitudes score 0.

### 10. Final-answer alignment

Does the closing claim match the derivation and the prompt? Penalize a careful body with an overconfident last paragraph, or a correct last line reached by cancelled errors when the prompt asked for reasoning.

## Using the profile

The helper `aibench.rubric.structured_profile` stores the ten scores and reports a mean, a minimum, and the list of dimensions scored 0. Reviewers should read the minimum and the failing-dimension list **before** the mean.

Recommended review order:

1. Task interpretation and final-answer alignment (did they answer the question?).
2. Evidence discipline (is anything fabricated?).
3. Causal validity and statistical correctness.
4. Mathematical and conceptual correctness.
5. Assumptions, completeness, clarity.
6. Assign `severity` from `docs/severity.md`, not from the mean.

## Verdicts

| Verdict | Use when |
| --- | --- |
| `pass` | Material reasoning is sound; severity is `PASS`. |
| `fail` | The takeaway should not be used as stated. |
| `correct_result_invalid_reasoning` | The reported result matches a correct solution, but the argument is not one a reviewer can trust. |

Verdict is not a tenth-plus dimension. It is a discrete call after the dimension review.
