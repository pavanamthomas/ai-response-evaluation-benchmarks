# Working on this laboratory

This is a personal research repository. The useful unit of work is a limitation, a failed specification, or a tighter check.

1. Open or update a GitHub issue. Name the estimand, the DGP, and the mismatch.
2. If the claim is numerical, add a test that fails on `main` before the change and passes after.
3. Keep commits narrow. Do not bundle formatting with a scientific change.
4. Do not add generator comments, co-author trailers, or editor metadata.

Recorded failures: `docs/failures_and_corrections.md`.  
Queue and bounds: `ROADMAP.md` and GitHub Issues.  
Checks: `python -m pytest` and `.github/workflows/ci.yml`.
