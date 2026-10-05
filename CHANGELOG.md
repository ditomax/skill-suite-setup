# Changelog — skill-suite-setup

## 0.1.11 — 2026-10-05
compat.md: new top row idea 0.3.1 · maquette 0.6.3 · build 0.1.10 (running cost and Users & scale in idea; running cost, load and growth, capacity & scaling in build; AI tools named in every ATTRIBUTION.md). examples/example pinned to it. No contract change.

## 0.1.10 — 2026-09-30
compat.md: new top row idea 0.3.0 · maquette 0.6.2 · build 0.1.9 (idea focus track, contract register/1 — not yet read downstream; explore unchanged). examples/example pinned to it. `setup.py prompt` carries only the profile rows of collect questions (C…, I…) — Director and evaluate rows (D…, E…, V…) no longer leak into the collect prompt file; it still renders the explore collect only, the focus prompt file follows. No change to H1/2 or H2/2.

## 0.1.9 — 2026-09-28
Prompt file (`setup.py prompt … idea-collect`): tailored questions now carry the text of the question they refer to and say what skip and add mean — the prompt file has no QUESTIONS.md, so a bare `skip C1` was unreadable for the chat model, and `add` lost its `after`. Cards stay in the background: one line when a card is captured, complete cards only on request and at the closing — in a chat the full card after every answer buried the next question. compat.md: new top row (same triple). No contract change.

## 0.1.8 — 2026-09-25
compat.md: new top row idea 0.2.4 · maquette 0.6.2 · build 0.1.9 (pre-mortem wording; V6 operating model at idea stage, operator names and time shares in build intake I7; also covers build 0.1.8). examples/example pinned to it. No contract change.

## 0.1.7 — 2026-09-17
AGENTS.md / CLAUDE.md gain a hard limit: public files (README, compat.md, CHANGELOG, PROFILE.md, everything in a release) name what was tested or changed, never a customer, a customer project, an internal folder or an internal test-run ID — the guard catches markers, not paraphrases. compat.md: the 0.2.2 row's test note no longer carries internal run IDs.
DMBG removed from README, AGENTS.md / CLAUDE.md, `setup.py`, the setup skill and every template (start.en/de, root- and planning-AGENTS, prompt-idea-collect) — the product is simply the skill suite. compat.md: new top row idea 0.2.3 · maquette 0.6.2 · build 0.1.7 (README section order aligned across the three). examples/example pinned to it. No contract change.

## 0.1.6 — 2026-09-17
`release.py`: the work-folder check no longer counts Finder/editor droppings (`.DS_Store`, `Thumbs.db`, `desktop.ini`, `._*`, `*.swp`/`*.swo`) as stray files — a `.DS_Store` in `maquettes/` aborted the v0.6.1 release although git never tracked it. Real files in the work folder still refuse the release. `.gitignore` here gained the `Thumbs.db` / `*.swp` lines the skillsets already had. No contract change.

## 0.1.5 — 2026-09-17
compat.md: new top row idea 0.2.2 · maquette 0.6.1 · build 0.1.6 (idea fixes from run-03). examples/example pinned to it.
Prompt file (`setup.py prompt … idea-collect`) reworked for the mail-only collection: how-to line in the customer language (open → copy → paste → type **start**), explicit start trigger, solo mode, conversation rules inlined (RULES.md is not in the file), address form from the new `customer.yaml` key `address` (du | sie, default du), personal-data reminder, provisional card IDs, closing with all cards and the reply-mail sentence.

## 0.1.4 — 2026-09-17
README: two kinds of users named — anyone assembling or tailoring the suite as one project folder (new → check → build, prompt) and maintainers (guard, release, hooks); "maintainers' tool" became "the suite's setup tool" here and in AGENTS.md / CLAUDE.md. compat.md: new top row idea 0.2.1 · maquette 0.6.1 · build 0.1.6 (README/START only). examples/example pinned to it. No contract change.

## 0.1.3 — 2026-09-17
compat.md: new top row idea 0.2.0 · maquette 0.6.0 · build 0.1.5 (H1/2, H2/2). Bootstrap dispatch: maquette proposes the shortlist's Maquette order; "merge" / "split" / "new committee round" route to idea in any state. examples/example pinned to the new triple.

## 0.1.2 — 2026-09-16
README fix: "Usage" example was a single `git clone` call with four ellipsis placeholders as if it were one literal, copy-pasteable command — not valid git syntax and not runnable as written. Replaced with four separate `git clone` commands using the real repo URLs. No contract change.

## 0.1.1 — 2026-09-16
README fixes: version line now points to `VERSION` (matching idea/maquette/build) instead of a hardcoded "0.1" string; `templates/` listing now includes `planning-pointer-AGENTS.md`. No contract change.

## 0.1.0 — 2026-09-16
First version. `setup.py` (new · check · build · prompt · list), tailoring dialogue `skills/setup/SKILL.md`, templates (root and planning pointers, suite bootstrap with dispatch and update rule, `start.en/de.md`, `customer.yaml`, nine profile files, idea-collect prompt file), `PROFILE.md` (the profile specification the skillsets read), `compat.md` (idea 0.1.3 · maquette 0.5.2 · build 0.1.3, H1/1, H2/2), customer-data guard (`guard.py`, allowlist builds, profile header binding, `hooks/pre-commit`), `release.py` for public skillset ZIPs, `examples/example` (fictitious Example GmbH), smoke-test log skeleton in `tests/`.
