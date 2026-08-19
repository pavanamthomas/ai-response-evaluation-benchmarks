# Severity rubric

Severity is assigned from the **earliest material failure** that would change how a careful reader should use the answer. It is not a count of typos, and it is not a weighted average of rubric dimensions. A response can be fluent and still be `CRITICAL`.

Use the labels below as a closed vocabulary. Case files store them in uppercase.

## CRITICAL

The answer would mislead a decision-maker on identification, mathematics, evidence, or policy confidence.

Assign `CRITICAL` when **any** of the following holds:

1. **False causal identification.** The response treats an associational estimate as an average treatment effect, LATE, or policy-invariant structural parameter without the identifying assumptions that would support that claim. Typical settings include uncontrolled OLS, two-way fixed effects under staggered adoption with heterogeneous effects, invalid or weak instruments presented as “as good as random,” and difference-in-differences when pre-trends already reject the parallel-trends design.
2. **Invalid mathematics that changes the answer.** An algebraic, analytic, or optimization error reverses a sign, changes a reported optimum, or produces a number that would not survive a correct derivation.
3. **Fabricated evidence.** Invented papers, tables, statistics, or quotations are offered as support. This includes specific journal-year-author citations that do not correspond to a real source, and invented numerical “stylized facts.”
4. **Unsafe or wrong policy certainty.** The response recommends a high-stakes intervention (scale-up, repeal, targeting) as if the evidence were decisive, when the design cannot support that certainty.

A `CRITICAL` case may still contain locally correct formulas. The severity attaches to the claim a reader would take away.

## MAJOR

The reasoning is wrong in a way that changes the **conclusion**, but it does not reach the four `CRITICAL` triggers, or it reaches them only in a muted form (for example, a causal overclaim without a scale-up recommendation).

Assign `MAJOR` when **any** of the following holds:

1. **Material conceptual error.** A definition is used as if it were another definition (GDP as sum of revenues; elasticity as a semi-elasticity; LATE as ATE) and the prompt’s question is answered with the wrong object.
2. **Wrong estimator interpretation.** A coefficient, standard error, or diagnostic is read incorrectly (log-level as levels; clustered dependence ignored as if the formula were merely optional).
3. **Missing identifying assumption that changes the conclusion.** Parallel trends, exclusion, relevance, no-anticipation, SUTVA, or stability of the measurement system is omitted, and restoring it would reverse or sharply qualify the claim.

`correct_result_invalid_reasoning` cases are typically `MAJOR`: the reported number or qualitative answer happens to match a correct derivation, but the argument would not generalize.

## MINOR

The answer is **directionally usable** but incomplete, poorly worded, or missing caveats that a referee would request. Restoring the missing material would **not reverse** the conclusion.

Examples:

- A correct comparative-static sign with no statement of the maintained functional form.
- A confidence interval interpreted a bit loosely, while the interval still excludes the null and the economic conclusion is unchanged.
- An incomplete list of limitations that does not hide a broken design.

Do not use `MINOR` to soften a broken identification argument.

## PASS

The response answers the prompt that was asked; the material reasoning is sound; maintained assumptions are stated; and the write-up does not manufacture certainty.

`PASS` does not mean “exhaustive,” “publishable in a top journal,” or “the unique correct essay.” It means a competent examiner could accept the answer without a required correction to the claim.

Passing cases set:

- `verdict: pass`
- `severity: PASS`
- `error_classification: [none]`
- `earliest_failure_point: none`

## Mapping from failure point to severity

`earliest_failure_point` names the first rubric dimension at which a careful reader should stop trusting the answer. Severity then follows the definitions above, not the name of the dimension. A failure in `clarity` is usually `MINOR`. A failure in `causal validity` or `evidence discipline` is usually `MAJOR` or `CRITICAL`.

## What severity is not

- It is not the mean of the ten rubric scores.
- It is not “how confident the candidate sounded.”
- It is not automatically `CRITICAL` merely because the topic is causal inference; a carefully qualified associational answer can `PASS`.
