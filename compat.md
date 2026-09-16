# Compatibility table

Version triples of the three skillsets that are known to work together, with the contract versions they speak. Newest first — `setup.py new` proposes the top row. `setup.py build` refuses a triple that is not listed (override with `--force`, then add the row after testing).

| setup | idea | maquette | build | H1 | H2 | tested | note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.1.1 | 0.1.5 | 0.5.4 | 0.1.5 | H1/1 | H2/2 | 2026-09-16 (READMEs only, smoke tests pending) | README consistency pass (symlink option, version line, templates listing, copy-paste fix, German-only aside removed) — same contracts |
| 0.1.0 | 0.1.4 | 0.5.3 | 0.1.4 | H1/1 | H2/2 | 2026-09-16 (onboarding tests T1–T3, smoke tests pending) | agent onboarding pass (README § For agents, chained cold start, clone git rule); same contracts |
| 0.1.0 | 0.1.3 | 0.5.2 | 0.1.3 | H1/1 | H2/2 | 2026-09-16 (build check only, smoke tests pending) | docs pass (chaining, prerequisites, PROFILE.md pointer); same contracts |
| 0.1.0 | 0.1.2 | 0.5.1 | 0.1.2 | H1/1 | H2/2 | 2026-09-16 (build check only) | first triple with profile/questions.md support |
