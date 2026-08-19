# Golden response standard

A **golden response** is the answer an expert examiner would accept for the same prompt. It is not a transcript of a conversation, not a model dump, and not a longer version of the candidate’s outline. It is a self-contained solution.

Write golden responses in the first person plural or in impersonal scientific prose (“The estimand is…”, “Under these assumptions…”). Do not attribute the golden response to a software tool or to an unnamed chatbot.

## Required properties

A golden response should do all of the following that the prompt makes relevant:

1. **Answer the exact prompt.** Restate the object being delivered (a definition, a number, a yes/no with conditions, a recommended estimator). If the prompt is ambiguous, name the reading used and, when it matters, the alternative reading.
2. **Define necessary concepts.** Introduce only the objects needed for the argument. Do not dump a textbook chapter.
3. **State material assumptions.** Identifying assumptions, regularity conditions, and measurement conventions belong in the open, not in a footnote after the claim.
4. **Show essential reasoning.** Formalize the problem, then compute or derive. Skip ornamental algebra; keep the steps that a second examiner would need to reproduce the result.
5. **Verify mathematics.** Check units, boundary conditions, feasibility, and special cases. If an optimum is claimed, confirm that constraints hold.
6. **Verify quantitative claims.** Arithmetic, compounding, elasticities, and conversions should be recomputed, not merely restated.
7. **Distinguish association from causation.** If the prompt asks for a causal claim, state the estimand (ATE, ATT, LATE, CATE) and the design. If the prompt asks only for description, do not upgrade it.
8. **Include a concrete example where helpful.** A two-period DiD table, a two-type LATE, or a one-constraint Kuhn–Tucker case often does more than an extra paragraph of taxonomy.
9. **Acknowledge limitations.** Say what would overturn the conclusion. Do not manufacture a consensus or a policy mandate.
10. **Provide the requested final output.** Close with the quantity, decision, or qualified sentence the prompt asked for.

## What a golden response must not do

- Invent bibliographic citations, working-paper titles, or journal-year-author triples. If a published result is essential, describe the **design and estimand** rather than faking a citation. Hypothetical numbers in a prompt are hypothetical; keep them labeled as such.
- Treat fluency as completeness. An elegant wrong identification strategy is not a golden response.
- Collapse LATE, ATT, and ATE without comment.
- Report an infeasible bundle, an unconstrained optimum for a constrained problem, or a *p*-value as P(H0 true).
- End with false certainty (“this proves”, “therefore implement nationwide”) unless the prompt supplies a design that actually supports that sentence.

## Relationship to other fields

| Field | Role relative to the golden response |
| --- | --- |
| `corrected_reasoning` | The patch to the candidate’s argument; may be shorter and more diagnostic. |
| `explanation` | Why the candidate failed or passed; written for the evaluator. |
| `evaluator_notes` | Scoring guidance, traps, and what not to over-penalize. |
| `assumptions` | Machine-readable list of maintained conditions. |
| `validation_steps` | Checks a reviewer or script-minded examiner can apply. |

The golden response should remain readable if those other fields were hidden.

## Length

Aim for the shortest complete solution: typically a few tight paragraphs plus a display equation or a small table when the prompt is quantitative. Do not pad. Do not omit the limitation that would change a practitioner’s use of the answer.

## Cross-checks

Before accepting a golden response in this repository:

- Recompute any number it reports.
- Confirm that every causal verb is backed by an assumption listed in `assumptions`.
- Confirm that it would receive `severity: PASS` if it were itself a candidate response.
