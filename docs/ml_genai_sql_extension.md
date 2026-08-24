# ML, GenAI/RAG, Python, and SQL review extension

The original corpus was built around economics, econometrics, statistics, mathematics, and quantitative reasoning. The technical extension keeps the same review object rather than starting a second scoring system: a prompt, a candidate response, an earliest substantive failure, a corrected reasoning path, and a golden response with explicit validation steps.

The added domains are deliberately small. Their purpose is to test whether the existing review method transfers to technical work where a plausible final number can survive an invalid procedure.

## Machine learning

The first cases target two distinctions that frequently disappear in fluent answers:

- supervised feature selection is part of model fitting and therefore belongs inside the resampling boundary;
- ranking discrimination and probability accuracy are different objects, so a higher ROC-AUC does not establish better calibration.

One case is marked `correct_result_invalid_reasoning` because the candidate correctly interprets the AUC ordering before making an invalid probability-quality inference.

## GenAI / RAG

The cases preserve stage-local diagnosis:

- gold evidence can be retrieved and then lost during context packing;
- retrieved document text remains evidence, not privileged instruction.

A wrong final answer is therefore not automatically a retrieval failure. The evaluator must identify the first stage that broke the evidence path.

## Python computation

The first cases separate mathematical formulas from computational validity:

- naive log-sum-exp is algebraically correct but numerically unstable on large inputs;
- a fixed random seed makes a Monte Carlo experiment repeatable, not free of Monte Carlo error.

The validation route matters as much as the final scalar.

## SQL reasoning

The first cases focus on relational grain and information-set integrity:

- two independent one-to-many joins can create many-to-many multiplication with no duplicate source rows;
- `LEAD` can violate a prediction cutoff even when one toy row happens to return the intended value.

The second example is another `correct_result_invalid_reasoning` case: accidental numerical agreement does not validate the query.

Issue #6 requested these domains. The YAML files, schema, and tests on `main` are the implementation; remaining work is additional distinct failure modes, not the existence of the folders.

## Boundaries

This extension does not claim exhaustive ML, GenAI, Python, or SQL coverage. It does not represent production traffic, a second-rater study, or a benchmark of commercial systems. New cases should be added only when they introduce a distinct technical failure mode or a materially different validation argument; case count by itself is not a quality target.
