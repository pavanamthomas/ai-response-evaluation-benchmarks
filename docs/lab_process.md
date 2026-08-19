# Laboratory process

Work is recorded in this order:

1. A failure, limitation, or identification question is written down (GitHub issue and, when it is part of the teaching design, `docs/failures_and_corrections.md`).
2. If the claim is numerical, a test is added that would fail if the claim were reversed.
3. Code or documentation changes in a commit that states the reason, not the file list.
4. CI on `main` must pass. Passing CI means the laboratory still runs under the documented commands. It is not evidence about an observational study.

The public queue is GitHub Issues. The bound on that queue is `ROADMAP.md`.

Do not treat a green badge as a correction. A correction is a change in estimator, specification, or interpretation, locked by a test or by an explicit limitation statement.
