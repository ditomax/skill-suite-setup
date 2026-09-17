# Compatibility table

Version triples of the three skillsets that are known to work together, with the contract versions they speak. Newest first — `setup.py new` proposes the top row. `setup.py build` refuses a triple that is not listed (override with `--force`, then add the row after testing).

| setup | idea | maquette | build | H1 | H2 | tested | note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.1.5 | 0.2.2 | 0.6.1 | 0.1.6 | H1/2 | H2/2 | 2026-09-17 (run-03 ChatGPT/Codex on idea 0.2.0; fixes not yet re-tested — run-04) | idea-merge read-back gate, staleness on every start, appended relations, complete shortlist entries — same contracts |
| 0.1.4 | 0.2.1 | 0.6.1 | 0.1.6 | H1/2 | H2/2 | 2026-09-17 (READMEs only, smoke tests pending) | README § The suite in all three skillsets (sibling links, pointer to skill-suite-setup); setup README names its two kinds of users; idea README names `setup.py prompt` — same contracts |
| 0.1.3 | 0.2.0 | 0.6.0 | 0.1.5 | H1/2 | H2/2 | 2026-09-17 (check + build of examples/example, smoke tests pending) | idea-merge (consolidate · umbrella · split); shortlist Maquette order — maquette 0.6.0 proposes the committee's choice; H1/2 is additive, maquette 0.4–0.5 read it as H1/1 |
| 0.1.2 | 0.1.5 | 0.5.4 | 0.1.5 | H1/1 | H2/2 | 2026-09-16 (README only, smoke tests pending) | setup README usage example fixed (real clone URLs, one command per line) — same contracts |
| 0.1.1 | 0.1.5 | 0.5.4 | 0.1.5 | H1/1 | H2/2 | 2026-09-16 (READMEs only, smoke tests pending) | README consistency pass (symlink option, version line, templates listing, copy-paste fix, German-only aside removed) — same contracts |
| 0.1.0 | 0.1.4 | 0.5.3 | 0.1.4 | H1/1 | H2/2 | 2026-09-16 (onboarding tests T1–T3, smoke tests pending) | agent onboarding pass (README § For agents, chained cold start, clone git rule); same contracts |
| 0.1.0 | 0.1.3 | 0.5.2 | 0.1.3 | H1/1 | H2/2 | 2026-09-16 (build check only, smoke tests pending) | docs pass (chaining, prerequisites, PROFILE.md pointer); same contracts |
| 0.1.0 | 0.1.2 | 0.5.1 | 0.1.2 | H1/1 | H2/2 | 2026-09-16 (build check only) | first triple with profile/questions.md support |
