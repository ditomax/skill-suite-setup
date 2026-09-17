# Changelog — skill-suite-setup

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
