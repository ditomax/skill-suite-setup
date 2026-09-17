# AGENTS.md — skill-suite-setup

You are in the setup tool of the skill suite (idea → maquette → build) — used by the suite's maintainers and by anyone who assembles or tailors their own version. This repo builds **customer versions**: a tailoring dialogue produces `customers/<name>/` (or a folder in the customer project via `--customer-dir`), and `setup.py build` renders `start.md` + one ZIP the customer unzips into a project folder.

## On every session start

1. Read `README.md` (what the tool does, the ZIP layout, the customer-data guard) and `PROFILE.md` (the profile format the skillsets read).
2. If the user wants a new customer version or a change to one, read `skills/setup/SKILL.md` and run the dialogue described there — one question at a time. Otherwise help with the tool itself.
3. The three skillset repos are expected as siblings (`../idea`, `../maquette`, `../build`) or via `--suites DIR`; the private marker list at `../guard-markers.txt` or via `--markers`.

## Hard limits

- **Customer material never enters this repo**: `customers/` and `dist/` are gitignored; never copy customer files anywhere else, never paste customer content into templates, README, examples or tests. `examples/` holds only the fictitious "Example GmbH".
- **Public files say what, never who**: `README.md`, `compat.md`, `CHANGELOG.md`, `PROFILE.md` and everything shipped in a release name only what was tested or changed — never a customer, a customer project (not even paraphrased as "the pending customer project"), an internal folder or an internal test-run ID. Customer context belongs in `customers/` and in the private test folders. The guard catches markers, not paraphrases — this rule is the part a human or an agent has to keep.
- Never bypass the guard: do not use `SUITE_GUARD_SKIP`, do not edit `guard.py` to make a build pass, do not add a customer name to an allowlist. If the guard refuses, the input is wrong.
- Never `git init`, commit, tag or push here; the maintainer does that. Never delete files — move them if something must go.
- Changes to the skillsets themselves (RULES, templates, skills, QUESTIONS.md) are made in their repos, not here; a customer wish that needs one is noted as "Feedback to the suite".
