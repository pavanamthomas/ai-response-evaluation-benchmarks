# Defect taxonomy

Every case that does not `PASS` carries one or more defect-family labels in `error_classification`. The corpus as a whole must include **each** family at least once. Labels are exact strings; do not paraphrase them in YAML.

Passing cases use `error_classification: [none]`, which is a schema token, not a defect family.

## Identification and causal design

| Family | What the candidate did |
| --- | --- |
| `correlation/causation` | Treated co-movement, a raw gap, or an uncontrolled regression as a causal effect. |
| `OVB` | Omitted a confounder that is correlated with the regressor and the outcome, and interpreted the coefficient as structural. |
| `invalid IV` | Used an instrument that fails exclusion, fails as-if random assignment, or is mechanically downstream of the outcome. |
| `weak instrument` | Proceeded with 2SLS/LIML as if consistency were enough, despite a weak first stage. |
| `incorrect DiD parallel-trends` | Reported a difference-in-differences ATT while pre-trends or event-study leads already reject the design. |
| `staggered-DiD issue` | Interpreted two-way fixed effects under staggered adoption and heterogeneous treatment effects as an average causal effect for the treated, ignoring negative weights and forbidden comparisons. |
| `incorrect placebo interpretation` | Treated a failed placebo, significant lead, or pre-policy jump as support for the design rather than as a threat. |

## Statistics and evidence

| Family | What the candidate did |
| --- | --- |
| `p-value error` | Interpreted a *p*-value as P(H0 \| data), as an effect size, or as the probability the result replicates. |
| `CI error` | Assigned a posterior probability to a realized frequentist interval, or treated “insignificant” as “zero.” |
| `statistical vs economic significance` | Equated a small *p*-value with a large or policy-relevant effect, or dismissed a large effect solely because *p* > 0.05. |
| `leakage` | Trained or validated using information that would not be available at decision time. |
| `overfitting` | Reported in-sample fit as out-of-sample performance, or chose a model class that interpolates noise. |
| `unsupported empirical claim` | Asserted a quantitative “literature fact” with no recoverable source or with a false claim of consensus. |
| `invented citation` | Named a specific work, table, or statistic that does not exist, or attributed a result to a real paper that does not contain it. |

## Economics, regression, and units

| Family | What the candidate did |
| --- | --- |
| `wrong economic definition` | Used the wrong object (GDP vs. revenue sums, elasticity vs. semi-elasticity, accounting identity vs. behavioral law). |
| `wrong regression interpretation` | Misread a coefficient’s units, functional form, or the status of a control variable. |
| `wrong sign` | Reported a comparative static, income/substitution effect, or estimated coefficient with the incorrect sign relative to the model. |
| `unit error` | Converted levels, logs, percents, or scale prefixes incorrectly, changing the quantitative claim. |

## Mathematics, optimization, and probability

| Family | What the candidate did |
| --- | --- |
| `incorrect optimization constraint` | Dropped, added, or converted a constraint (equality vs. inequality) so that the program is not the one stated. |
| `infeasible solution` | Reported a point that violates the constraint set. |
| `boundary-condition omission` | Ignored complementary slackness, non-negativity, or a corner solution that is the actual optimum. |
| `probability error` | Violated the probability axioms (double-counted unions, treated dependent events as independent without saying so). |
| `Bayes error` | Reversed a conditional probability or neglected the base rate. |
| `arithmetic error` | A numerical mistake that is not a deep conceptual error but that changes the reported answer. |

## Task and semantics

| Family | What the candidate did |
| --- | --- |
| `incomplete answer` | Stopped before addressing a required part of the prompt; what is present may be locally correct. |
| `correct result with invalid reasoning` | The final number or qualitative call matches a correct solution, but the derivation would not survive a change in parameters. |
| `technically correct but semantically wrong` | A formula is applied correctly under an assumed model that is not the model implied by the prompt (for example, iid standard errors on clustered data). |
| `answer to wrong interpretation of ambiguous prompt` | The prompt admitted more than one reasonable reading; the candidate picked one silently and answered as if it were unique. |

## How to assign labels

1. Choose the **earliest** family that, if corrected, would change the takeaway. Additional families may be listed if they independently matter.
2. Do not invent near-synonyms (`omitted variable` instead of `OVB`). Coverage tests match exact strings.
3. A single case may carry several families. Corpus coverage is evaluated on the union across cases, not on a one-family-per-case rule.
