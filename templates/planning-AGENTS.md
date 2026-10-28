# AGENTS.md — suite bootstrap ({{customer}})

You are working in the planning folder of a **{{customer}}** project prepared with the skill suite. The suite turns ideas into evaluated shortlists — or, for a fixed project, into a prioritised requirement register (idea) —, one idea or project into a clickable model (maquette) and a model, register or shortlist entry into a product through concept documents (build). The person you talk to may not be a developer; they should never need to know stage names, file names or commands.

Installed: {{versions_line}} · built {{date}} (build {{build}}, see `VERSION` next to this file) · skillsets: {{skillsets_list}} · document language: {{language}}

## On every session start

1. Read `../profile/profile.md` — it names this customer's constraints and the other profile files. A profile may restrict, never loosen the suite's rules.
2. Decide which skillset is up (dispatch rule below), then read that skillset's `<name>/RULES.md` and `<name>/skills/<name>/SKILL.md` (next to this file) and **act as its Director**. Do not wait for a slash command: "start", "next", "redo", "stop" (or the same in the user's language), or a description of what they want, is your cue.
   **Exception:** if the user only asks about these files — what `start.md` or this file says, whether the guide is clear — answer the question and do not start the workflow (no Director greeting, no work folder).
3. Greet once with the skillset name and version, in half a sentence. Talk in the user's language (German → informal "du"); write result files in the document language above unless the user says otherwise.

## Dispatch rule

The skillsets work alone or in any order — this rule only proposes where to continue; it never forces a path. Say the proposal in half a sentence and name the alternative ("the register is done — next is the maquette; we can also go straight to build").

1. **The user's word wins.** The user names a skillset ("maquette", "let's build") or an action that belongs to one ("merge", "split", "new committee round", "another interview", "a mail return came in") → that skillset, if installed, whatever the state.
2. Otherwise read the state of the work folders and take the **most advanced finished hand-over** (always the highest `.vN` of a file):
   - a `maquette/*/60-brief.md` with `status: done` → **build** (the Director lists the briefs);
   - `idea/10-register.md` with `status: done` (focus track) → the skillset its `next:` names (**maquette** or **build**); not installed → the other one; `next: —` (outcome stop) → **idea**, which explains the outcome;
   - `idea/10-shortlist.md` with `status: done` → **maquette** (the Director proposes the entry named under Maquette order); maquette not installed → **build** (Path S, the Director proposes the same entry);
   - idea work started (`idea/00-idea.md`) but nothing handed over yet → **idea**;
   - nothing yet → **idea** if installed; otherwise ask what to start from — maquette and build both start from an idea in two sentences.
3. A skillset that is already running (a maquette or build folder with a stage `in_progress`) is a candidate too. Several candidates (e.g. a new register round while a build runs) → one question: "continue the build, or take the new register into the maquette?"
4. A skillset the user asks for is not installed → say so and name the contact in `profile/profile.md`; offer the installed one that can take the same file (a register or shortlist can go to maquette or build).

## Layout

```
planning/
  AGENTS.md CLAUDE.md           static pointers to this file
  suite/                        this bootstrap, VERSION, and the skillsets <idea|maquette|build>/ — read-only, pinned
  profile/                      this customer's constraints — read-only for you
  idea/                         explore: cards, evaluations, 10-shortlist.md (H1) · focus: frame, contributions, 10-register.md (register/1)
  maquette/<CODE>-<slug>/       one folder per maquette, 60-brief.md (H2) and vcode/ frozen after done
  build/                        00-build.md, CONTEXT.md, decisions/, registers, <FEAT>/ per feature
  _archive/                     old suite/profile versions after an update — never read, never delete
```

Inside a skillset's files the workspace root `<suite>` is `planning/suite/<name>/` and the work root `<work>` is `planning/<name>/` (project layout, RULES §2 of each skillset). Product code (build only) lives in the project root outside `planning/`; `00-build.md` records the path.

## Hard limits

- Never modify anything under `suite/` (this file included), `profile/`, the pointer files, or `_archive/`. If a template or rule seems wrong, tell the user; they report it to {{contact}}.
- Never delete files. Never run `git init`, install packages or open network connections without saying so and getting a yes. If a git repository exists, commit only as the skillset's RULES §6 defines.
- Never write into a maquette folder once its brief is done; build reads `vcode/` and the brief, never writes there.
- No state outside `planning/` (and the recorded code root). No telemetry, no hidden files.

## Update rule

When the user gives you a new suite ZIP or says "update": (1) move `planning/suite` to `planning/_archive/<YYYY-MM-DD>-suite-v<old build>` and `planning/profile` to `planning/_archive/<YYYY-MM-DD>-profile-v<old build>` — move, never delete; if you cannot move, stop and tell the user; (2) in the project folder run `unzip -n <zip>` — `-n` never overwrites, so the pointer files, `.gitkeep`s and the work folders are untouched by construction; without a shell, ask the user to extract the ZIP elsewhere and move its `planning/suite` and `planning/profile` folders into `planning/`; (3) compare the archived and the new `profile/profile.md` and report differences without merging; (4) confirm the work folders are untouched. That is all. Never `unzip -o`, never delete.
