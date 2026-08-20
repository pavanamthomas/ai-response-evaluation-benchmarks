# Flagship review case: staggered grants, two-way fixed effects, and a causal policy claim

**Audience.** Examiner or hiring reviewer assessing whether a candidate can audit a modern difference-in-differences design, not merely recite the two-by-two formula.

**Domain mix.** Public economics, panel econometrics, treatment-effect heterogeneity, and policy interpretation.

**Related corpus cases.** `ECONM-003` (parallel trends), `ECONM-004` (staggered two-way fixed effects), `ECONM-005` (placebo leads), `MIX-001` (unsafe policy certainty). This document is the long-form review; those YAML files are compact scoring items.

**Prompt (as given to the candidate).**

> Between 2011 and 2019, a federal “Career Pathways Grant” was adopted by states in three waves (2012, 2015, 2018). Never-treated states remain never-treated through 2019. A research assistant estimates
>
> \[
> y_{st} = \alpha_s + \lambda_t + \beta D_{st} + x_{st}'\gamma + u_{st}
> \]
>
> on a balanced state-year panel, where \(D_{st}=1\) after the state adopts the grant and \(y_{st}\) is the log prime-age employment-to-population ratio. The reported \(\hat\beta = -0.031\) (clustered by state, \(p=0.02\)). An event-study plot of the same TWFE specification shows coefficients of about \(-0.015\) in the two years before adoption for the 2015 and 2018 waves, and post-treatment coefficients that are near zero for early adopters and more negative for late adopters. A placebo that assigns the 2012 cohort’s adoption date to never-treated states in a fake 2011–2014 window produces \(\hat\beta^{\text{placebo}}=-0.018\) (\(p=0.11\)).
>
> The candidate is asked: (i) what causal estimand, if any, \(\beta\) identifies; (ii) whether the employment effect of the grant is negative; (iii) what diagnostics to run next; and (iv) what, if anything, a labor department should conclude about scaling the program.

**Candidate response (submitted).**

> The two-way fixed effects regression is the modern difference-in-differences estimator for staggered treatments. Because we include state and year fixed effects, parallel trends is not required in levels, only in the residual. The coefficient \(\hat\beta=-0.031\) is therefore the average treatment effect on the treated: the grant reduced employment by about 3.1 percent. The estimate is statistically significant, so the economic effect is also significant. Pre-trends of \(-0.015\) are half the main effect and are a good sign that we are picking up a smooth causal path rather than a jump. Late adopters having larger effects is heterogeneity, which TWFE averages correctly. The placebo is insignificant at 10 percent, which confirms robustness. I would scale the program down: a 3 percent employment loss is too large to justify the training expenditure. For a nationwide rollout the same \(\beta\) applies because TWFE already averaged over states.

---

## Examiner verdict

**Verdict:** fail  
**Severity:** CRITICAL  
**Earliest failure point:** causal validity  
**Defect families:** `staggered-DiD issue`; `incorrect DiD parallel-trends`; `incorrect placebo interpretation`; `statistical vs economic significance`; `correlation/causation` (policy-certainty upgrade)

The candidate’s closing policy sentence would not survive a competent referee report. The number \(-0.031\) is a weighted combination of many two-by-two comparisons, some of which use already-treated states as controls. The event study already shows pre-treatment movement. The placebo is not a pass. None of this identifies an ATT that can be shipped to a labor department as “the” effect of the grant.

---

## What the candidate got right

1. The notation for a two-way fixed effects (TWFE) linear panel model is the specification that was estimated. That is not in dispute.
2. State clustering is the right *direction* for serial correlation within states, though it does not repair identification.
3. Heterogeneity across adoption cohorts is empirically visible in the prompt. The candidate noticed the pattern. The error is the claim that TWFE “averages it correctly.”

These fragments must not be over-penalized. The failure is identification and interpretation, not algebra of dummy variables.

---

## Formalization

Index states by \(s\) and years by \(t\). Let \(G_s\) be the first treated year (the cohort), with \(G_s=\infty\) for never-treated. Let \(D_{st}=\mathbf{1}\{t\ge G_s\}\). Potential outcomes are \(Y_{st}(g)\) under first treatment at \(g\), and \(Y_{st}(\infty)\) under never treatment. The **cohort-time average treatment effect on the treated** is

\[
\mathrm{ATT}(g,t)=\mathbb{E}[Y_{st}(g)-Y_{st}(\infty)\mid G_s=g],\qquad t\ge g.
\]

A **group-time** family \(\{\mathrm{ATT}(g,t)\}\) is the natural estimand once adoption is staggered and effects may depend on calendar time and on time since treatment. The TWFE coefficient \(\beta\) in the candidate’s equation is **not** an average of \(\mathrm{ATT}(g,t)\) with non-negative weights that sum to one, once effects are heterogeneous and treatment timing varies.

Write the TWFE estimator as a weighted sum of two-by-two DiD comparisons (Goodman-Bacon type decomposition): treated-versus-not-yet-treated, treated-versus-never-treated, and treated-versus-already-treated. The last family uses already-treated units as controls. If those units are still experiencing changing treatment effects, the “control” change is itself a treatment path. The associated weights can be negative. Negative weights mean that a positive \(\mathrm{ATT}(g,t)\) can pull \(\hat\beta\) toward zero or through zero, and a negative \(\hat\beta\) need not sign any economically relevant average of \(\mathrm{ATT}(g,t)\).

Early adopters in this prompt have post-treatment coefficients “near zero”; late adopters are “more negative.” That is exactly the setting in which already-treated early cohorts contaminate later comparisons. Interpreting \(\hat\beta\) as ATT is therefore not a harmless simplification.

---

## Assumptions the candidate skipped or reversed

A staggered binary treatment design can identify group-time ATTs under, at least:

1. **No anticipation** (or a known anticipation window). Outcomes in \(t<G_s\) do not already embed the grant. The event-study leads of about \(-0.015\) are a direct threat.
2. **Parallel trends in untreated potential outcomes** between groups that are actually used as controls, possibly conditional on \(x_{st}\). Parallel trends is **not** implied by the presence of \(\alpha_s\) and \(\lambda_t\). Those terms absorb time-invariant state differences and common shocks. They do not absorb differential pre-trends.
3. **Overlap / common support in calendar time** for the comparisons one intends to use.
4. **SUTVA / no interference** across states (labor markets that straddle borders, migration, federal budget spillovers).
5. **Correct timing** of \(D_{st}\) relative to when funds, eligibility, and take-up actually move.
6. **If covariates are used for identification,** they must not be post-treatment (bad controls) and the parallel-trends statement must be the conditional one that matches the specification.

The candidate’s sentence “parallel trends is not required in levels, only in the residual” is a confusion. TWFE *imposes* a linear residual restriction; it does not *test* or *create* parallel untreated paths. If untreated outcomes already diverge, \(\hat\beta\) is a mix of treatment effects and differential drift.

---

## Computation: what \(\hat\beta=-0.031\) can and cannot be

Under homogeneous constant effects, TWFE \(\beta\) coincides with that common effect, and the event-study leads should be near zero. The prompt violates both the homogeneity pattern and the lead pattern.

A numerical sketch, not a substitute for the actual Bacon table, is enough to see the trap. Suppose three comparisons:

- 2012 cohort versus never-treated, long post window: effect near 0.
- 2015 cohort versus not-yet-treated (including 2012 cohort already treated): late negative effects minus the early cohort’s continuing path.
- 2018 cohort versus already-treated: similar contamination.

If the already-treated path is flatter than the untreated path of late adopters, the DiD subtraction can manufacture a negative composite even if some group-time ATTs are zero. Conversely, shrinking effects after a large first-year impact can contribute **negative weights** on those first-year ATTs. Either way, “employment fell 3.1 percent because of the grant” is not identified.

The *p*-value of 0.02 answers a different question: whether this particular weighted combination is distinguishable from zero under the chosen clustering, **assuming the TWFE model is the causal model**. It is not evidence that the grant reduced employment by a policy-relevant 3 percent.

---

## Validation and diagnostic sequence

The next steps are not optional polish. They are the identification audit.

**Step A — Event study that does not use already-treated as controls.**  
Re-estimate leads and lags with an estimator built for staggered adoption and a clean control group (never-treated, or not-yet-treated with a method that does not re-use treated units as controls). Plot cohort-specific event studies, not only a pooled TWFE event study. The prompt’s pooled leads of \(-0.015\) already indicate trouble; cohort plots may show that 2015 and 2018 were selected on declining employment.

**Step B — Goodman-Bacon (or equivalent) decomposition of the TWFE coefficient.**  
Report the weight and the two-by-two estimate on each family of comparisons. If a large weight sits on treated-versus-already-treated, stop using \(\hat\beta\) as ATT.

**Step C — Group-time ATT estimators.**  
Callaway–Sant’Anna, Sun–Abraham, or an imputation estimator (Borusyak–Jaravel–Spiess type) with an explicit control group and an explicit parallel-trends statement. Report \(\widehat{\mathrm{ATT}}(g,t)\) and a small set of summary aggregations: event-time averages, calendar-time averages, and a cohort-weighted overall ATT **with the weights stated**. If those aggregations disagree in sign with TWFE, TWFE is not “the” answer.

**Step D — Pre-trend and selection analysis.**  
Ask whether declining employment *predicts adoption*. If governors adopt the grant when factories close, \(D_{st}\) is endogenous to \(Y_{s,t-1}\). Then even a clean staggered estimator needs a different design (instrumenting adoption, a discontinuity in grant scoring, or a synthetic-control / matching approach with a credible donor pool)—or the study should be rewritten as descriptive.

**Step E — Placebo battery with a pre-committed rule.**  
The submitted placebo already fails a scientific, not a ritual, test: a fake treatment on never-treated states in 2011–2014 yields \(-0.018\), more than half of \(-0.031\), with \(p=0.11\). “Insignificant at 10 percent” is not confirmation. A placebo that reproduces a large share of the main coefficient, with a *p*-value that would be described as “marginal” if it were the main estimate, is a **warning**. Additional placebos: shift all adoption dates back two years inside a pre-period; estimate effects on a pre-determined outcome the grant should not affect (for example, lagged age structure if it is not itself a channel); and, if the grant is sector-targeted, estimate a contrast between eligible and ineligible industries *inside* treated states only after showing that industry composition is not itself the selection margin.

**Step F — Heterogeneity that is economic, not only statistical.**  
Late-adopter effects being more negative can be (i) worse labor markets selecting into late adoption, (ii) a different federal cycle, (iii) a different grant implementation, or (iv) genuine CATE. Split by manufacturing share, by unemployment at \(G_s-1\), and by take-up of funds per worker. If “effects” vanish when conditioning on pre-adoption employment trends, the story is selection, not training.

**Step G — Multiple testing and economic magnitude.**  
A 3 percent movement in a state employment-population ratio is large. Before discussing scale-down, show that the implied jobs change is consistent with administrative take-up. If 2 percent of prime-age adults receive training, a 3 percent employment drop would require enormous displacement or a mismeasured outcome. That back-of-envelope is a **validation**, not a rhetorical flourish.

---

## Placebo analysis, interpreted correctly

| Object | Candidate’s reading | Examiner’s reading |
| --- | --- | --- |
| Event-study leads \(\approx -0.015\) | “Smooth causal path” | Pre-treatment movement; no-anticipation / parallel trends threatened |
| Larger late-adopter post coefficients | “TWFE averages heterogeneity correctly” | Symptom of HTE and of forbidden comparisons |
| Fake-adoption \(\hat\beta=-0.018\), \(p=0.11\) | “Robust because \(p>0.10\)” | Placebo coefficient is first-order relative to the main estimate; failure to reject at an arbitrary threshold is not validation |
| Main \(p=0.02\) | “Economically significant” | Statistical detectability of a possibly non-interpretable weighted sum |

A placebo is a **specified null**. Here the null is “a treatment that did not happen should estimate zero.” An estimate of \(-0.018\) is not zero in any economic sense relative to \(-0.031\). The *p*-value of 0.11 says the placebo is noisily estimated, not that it passed.

---

## Corrected identification strategy

1. **Define the estimand in writing** before opening the regression: for example, the average effect of *adopting the grant* on log employment for states that adopt, in the first three post years, relative to never-treated states, under conditional parallel trends and no anticipation. If the department cares about *nationwide scale-up*, that is a different parameter (external validity, general-equilibrium wages, federal financing).
2. **Choose a staggered-safe estimator** with never-treated (or not-yet-treated) controls, cohort-time ATTs, and aggregation weights that are stated and non-negative by construction for the summary chosen.
3. **Do not condition on post-treatment covariates** that lie on the path (employment composition, contemporaneous UI claims) unless the target is a filtered partial effect, which must be labeled as such.
4. **Pre-trend test as a design test**, not as a coefficient to be “explained away” by a causal smoother.
5. **If pre-trends fail,** either (a) restrict to a subsample where they do not, with a multiple-testing caveat, (b) move to an identification strategy that does not need those trends (RDD on a grant scoring threshold, if one exists), or (c) report a descriptive event study and **stop** the causal sentence.
6. **For policy,** map the identified parameter to a decision: a negative ATT on employment among late adopters, even if credibly estimated, does not imply that a nationwide expansion has the same sign, because scale changes wages, displacement, and who enrolls.

---

## Golden response (examiner-quality solution to the same prompt)

The coefficient \(\beta\) in the two-way fixed effects specification is a linear combination of many two-by-two difference-in-differences comparisons, including comparisons that use already-treated states as controls. When treatment effects vary by cohort or by time since adoption, those weights need not be non-negative and need not recover the ATT, the ATE, or any other standard causal mean. With staggered adoption from 2012 to 2018 and the heterogeneity described in the prompt (early-adopter post effects near zero, late-adopter effects more negative), \(\hat\beta=-0.031\) should **not** be read as “the grant reduced employment by 3.1 percent.”

Parallel trends is an assumption on untreated potential outcomes, not a by-product of including \(\alpha_s\) and \(\lambda_t\). The event-study leads of about \(-0.015\) are large relative to the TWFE coefficient and are evidence against a clean pre-period. They are not a “smooth causal path.” A leading explanation is selection: states adopt when employment is already weakening. In that case even a staggered-safe estimator of ATT\((g,t)\) can remain biased without a richer design.

The placebo that assigns a fake 2012-style adoption date to never-treated states and obtains \(-0.018\) (\(p=0.11\)) does **not** validate the design. The point estimate is more than half the headline coefficient. Failure to reject zero at the 10 percent level is consistent with a noisy placebo, not with a passed specification test. Statistical significance of the main TWFE coefficient (\(p=0.02\)) is not economic identification, and it is not a license to treat \(-0.031\) as a structural employment elasticity of the grant.

What to do next, in order: (i) decompose the TWFE coefficient into two-by-two families and inspect the weight on already-treated controls; (ii) estimate group-time ATTs with a clean control group and report event-time aggregations with explicit weights; (iii) show cohort-specific pre-trends and a regression of adoption on lagged employment; (iv) interpret placebos by coefficient size relative to the main estimate, not only by a 0.10 cutoff; (v) check whether implied job losses are consistent with take-up. If pre-trends and placebos remain first-order, the honest report is that the panel does **not** identify the employment effect of the grant.

For the labor department: do **not** scale the program up or down on the basis of this TWFE coefficient. The present evidence is not a credible ATT, and even a future credible ATT for late-adopting states would not automatically travel to a nationwide expansion. Commission an estimator that matches a stated estimand, or commission a design that exploits grant-scoring discontinuities or randomized pilot slots if those exist. Until then, the employment effect of the Career Pathways Grant is **not identified** from the regression that was shown.

---

## Scoring notes for reviewers

- **Do not reward** the phrase “modern DiD” as if it named a single estimator. After about 2018–2021 applied work, “DiD with staggered treatment” is a family of estimands and estimators, not TWFE by default.
- **Do reward** a candidate who refuses to sign the employment effect, who names negative weights, and who treats \(p=0.11\) on a large placebo as a problem.
- **Over-penalize** only if the review misses that TWFE can be fine under **homogeneous** effects *and* clean pre-trends—neither of which holds here.
- **Evidence discipline:** this prompt is a hypothetical panel. A golden response must not invent a paper that “already estimated Callaway–Sant’Anna on this grant.”

## Suggested dimension profile (candidate)

| Dimension | Score (0–3) | Note |
| --- | --- | --- |
| Task interpretation | 2 | All four sub-questions are touched |
| Conceptual correctness | 0 | TWFE coefficient treated as ATT |
| Mathematical correctness | 2 | Linear panel written correctly |
| Statistical correctness | 1 | *p*-values used as robustness and as economic size |
| Causal validity | 0 | Staggered HTE, pre-trends, placebo |
| Assumptions | 0 | Parallel trends “not required” |
| Completeness | 1 | No diagnostic sequence |
| Clarity | 2 | Fluent, internally consistent in its error |
| Evidence discipline | 2 | No invented citations; over-reads the given numbers |
| Final-answer alignment | 0 | Recommends scale-down from a non-identified parameter |

Mean of these scores would be misleadingly middling. Severity is **CRITICAL** because of false identification plus a policy action.

## Closing examiner sentence

A competent review in this area is not the one that can write \(\alpha_s+\lambda_t+\beta D_{st}\). It is the one that can say that this \(\hat\beta\) is not an ATT, that the pre-trends and placebo already contradict the design, and that a labor department should not move a program on that number.
