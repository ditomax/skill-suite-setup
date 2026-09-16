# Profile specification

**Owner: skill-suite-setup.** The skillsets idea, maquette and build read `profile/` (standalone) or `planning/profile/` (project layout); they never define the format. This file is the format. A profile may **restrict, never loosen** — write rules, git behaviour and "nothing outside the folder" stay as each skillset's `RULES.md` defines. Absent files mean core defaults; `profile.md` is the only file that must exist for a profile to count.

Every profile file starts with `# <File> — <customer>` — `setup.py build` checks that the customer named there is the one the ZIP is built for.

Every Director reads `profile/profile.md` at every start and passes the files named there to the stages (RULES §8 of each skillset). **A profile may restrict, never loosen.** Files absent = core defaults. English headings; content in the customer language.

| File | Read by | Content |
| --- | --- | --- |
| `profile.md` | all Directors | customer, org code, default `language`, default modes, budgets per stage, sponsor / product-owner roles, contact for questions, list of the other profile files present |
| `questions.md` | all Directors | `skip` / `add` per question ID (see below) |
| `scope.md` | idea-collect, sparring | allowed topic areas, exclusions, department list for the interface round, company goals / AI strategy (prefills Strategy link) |
| `standards.md` | idea-evaluate (V8), build-intake, build-concept | mandatory norms and certifications with contact persons; effort classes for V6; house-specific requirement checklist rows |
| `it-constraints.md` | plan-board, maquette-build, build-concept, build-synthesis | allowed stacks and dependencies, hosting, "no network", data rules, where a prototype may run |
| `design.md` | design-3 | corporate design tokens (typeface, colours, spacing); variants then differ in layout, density and flow |
| `import-formats.md` | idea-collect | the customer's own card formats: columns → card fields (e.g. their xlsx export), encoding notes |
| `conventions.md` | build-synthesis, build-rescue | coding conventions, repository layout, CI expectations, commit rules beyond RULES §6 |
| `review.md` | maquette Director (gate), build Director (gates) | who signs which gate, the customer's own review and release process, next-step options replacing the brief's defaults |

## `questions.md`

```markdown
# Questions — <customer>

| Skillset | Question ID | Action | Value / new question | Reason |
| --- | --- | --- | --- | --- |
| idea | D3 | skip | git: no | customer has no git |
| idea | C7 | skip | Personal data: never; legal contact: Datenschutzbeauftragter | company policy |
| maquette | F3 | skip | file in the folder, no live fetch | IT constraint |
| maquette | after P6 | add | "Does the prototype touch SAP data? If so, which export?" | every idea here touches SAP |
| build | I3 | skip | web app → OWASP ASVS, DSGVO, WCAG 2.2 AA always apply | standards.md |
```

Rules: `skip` needs a value — the Director shows it as prefilled and lets the user correct it once; a corrected value is recorded, the profile is not edited. `add` names the question after which it is asked and is asked exactly once per stage run; its answer goes into the stage's result file under the closest section, marked `(profile)`. Gate questions cannot be skipped. `setup.py check` verifies every ID exists in the skillset's `QUESTIONS.md` at the pinned version.


## Minimal profile

```markdown
# Profile — Example GmbH

- **Customer:** Example GmbH
- **Org code:** EXG
- **Document language:** de
- **Contact for questions:** Jane Doe, jane@example.com
- **Profile files present:** none
```

Templates with the field spec as comments: `templates/profile/`. The tailoring dialogue that fills them: `skills/setup/SKILL.md`.
