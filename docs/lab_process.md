# How this lab records work

Evaluation claims here are claims about a labelled corpus and a rubric, not about a production LLM. Write the domain, the intended failure (wrong target, leaked information, invalid method, unbounded interpretation), and whether the label is single-author before changing YAML or the scorer.

If the claim is numerical, add a test that would fail if a fluent wrong answer scored as correct. CI on `main` means pytest still passes on the frozen YAML. It is not a second-rater study and not a leaderboard.

Issues are the public queue. `ROADMAP.md` is the bound. A green badge is not inter-rater reliability.
