# Compatibility table

Version triples of the three skillsets that are known to work together, with the contract versions they speak. Newest first — `setup.py new` proposes the top row. `setup.py build` refuses a triple that is not listed (override with `--force`, then add the row after testing).

| setup | idea | maquette | build | H1 | H2 | tested | note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.1.0 | 0.1.3 | 0.5.2 | 0.1.3 | H1/1 | H2/2 | 2026-09-16 (build check only, smoke tests pending) | docs pass (chaining, prerequisites, PROFILE.md pointer); same contracts |
| 0.1.0 | 0.1.2 | 0.5.1 | 0.1.2 | H1/1 | H2/2 | 2026-09-16 (build check only) | first triple with profile/questions.md support |
