# Compatibility table

Version triples of the three skillsets that are known to work together, with the contract versions they speak. Newest first — `setup.py new` proposes the top row. `setup.py build` refuses a triple that is not listed (override with `--force`, then add the row after testing).

| setup | idea | maquette | build | H1 | H2 | tested | note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.1.10 | 0.3.0 | 0.6.2 | 0.1.9 | H1/2 · register/1 | H2/2 | 2026-09-30 (check + build of examples/example; explore track unchanged since 0.2.4 — field-tested; focus track not yet tested) | idea: new focus track (focus-collect, focus-consolidate, focus-review) with its own contract register/1 — not yet read by maquette 0.6.2 or build 0.1.9 (paste `10-register.md` at their cold start); skip rule in both tracks. Explore contracts unchanged |
| 0.1.9 | 0.2.4 | 0.6.2 | 0.1.9 | H1/2 | H2/2 | 2026-09-28 (prompt file rendered and read) | prompt file: tailored questions carry the question text and the skip/add semantics — same contracts |
| 0.1.8 | 0.2.4 | 0.6.2 | 0.1.9 | H1/2 | H2/2 | 2026-09-25 (check + build of examples/example; idea and maquette field-tested on ChatGPT/Codex before the fix) | idea: pre-mortem asks which success criterion is most likely missed; V6 asks for an operating model only — names and time shares move to build intake (I7). build 0.1.8 (DRS checklists) is included — same contracts |
| 0.1.7 | 0.2.3 | 0.6.2 | 0.1.7 | H1/2 | H2/2 | 2026-09-17 (READMEs only, end-to-end test pending) | README section order aligned across idea, maquette and build; maquette gained a Contracts section, build a Language and Git section — same contracts |
| 0.1.5 | 0.2.2 | 0.6.1 | 0.1.6 | H1/2 | H2/2 | 2026-09-17 (ChatGPT/Codex end-to-end on idea 0.2.0; fixes not yet re-tested) | idea-merge read-back gate, staleness on every start, appended relations, complete shortlist entries — same contracts |
| 0.1.4 | 0.2.1 | 0.6.1 | 0.1.6 | H1/2 | H2/2 | 2026-09-17 (READMEs only, smoke tests pending) | README § The suite in all three skillsets (sibling links, pointer to skill-suite-setup); setup README names its two kinds of users; idea README names `setup.py prompt` — same contracts |
| 0.1.3 | 0.2.0 | 0.6.0 | 0.1.5 | H1/2 | H2/2 | 2026-09-17 (check + build of examples/example, smoke tests pending) | idea-merge (consolidate · umbrella · split); shortlist Maquette order — maquette 0.6.0 proposes the committee's choice; H1/2 is additive, maquette 0.4–0.5 read it as H1/1 |
| 0.1.2 | 0.1.5 | 0.5.4 | 0.1.5 | H1/1 | H2/2 | 2026-09-16 (README only, smoke tests pending) | setup README usage example fixed (real clone URLs, one command per line) — same contracts |
| 0.1.1 | 0.1.5 | 0.5.4 | 0.1.5 | H1/1 | H2/2 | 2026-09-16 (READMEs only, smoke tests pending) | README consistency pass (symlink option, version line, templates listing, copy-paste fix, German-only aside removed) — same contracts |
| 0.1.0 | 0.1.4 | 0.5.3 | 0.1.4 | H1/1 | H2/2 | 2026-09-16 (onboarding tests T1–T3, smoke tests pending) | agent onboarding pass (README § For agents, chained cold start, clone git rule); same contracts |
| 0.1.0 | 0.1.3 | 0.5.2 | 0.1.3 | H1/1 | H2/2 | 2026-09-16 (build check only, smoke tests pending) | docs pass (chaining, prerequisites, PROFILE.md pointer); same contracts |
| 0.1.0 | 0.1.2 | 0.5.1 | 0.1.2 | H1/1 | H2/2 | 2026-09-16 (build check only) | first triple with profile/questions.md support |
