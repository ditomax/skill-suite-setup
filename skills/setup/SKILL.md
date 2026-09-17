---
name: setup
version: "0.1"
description: >
  Tailoring dialogue of skill-suite-setup — produces a customer version of the DMBG
  skill suite (idea → maquette → build): customer.yaml plus the profile files that
  setup.py builds into start.md and a ZIP. Trigger on /setup, "new customer version",
  "tailor the suite for <customer>", or when editing an existing customer profile.
  Internal tool for the suite maintainers; runs in the skill-suite-setup repo or in a
  customer project via --customer-dir.
---

# setup — Tailoring dialogue

You produce a **customer version**: `customers/<name>/customer.yaml` and `customers/<name>/profile/*.md`, then run `setup.py check` and offer `setup.py build`. You never edit the skillset repos here — a customer wish that needs a suite change is noted under "Feedback to the suite" at the end and goes to the skillset's maintainer.

Read `../../documentation/setup-skill-design.md` §5 (profile specification) if it is reachable, else the templates in `templates/profile/` — the comments there are the field spec. Read the three `QUESTIONS.md` (`<suites>/idea|maquette|build/QUESTIONS.md`) before step 9.

## Opening

Two sentences: you will walk through what this customer needs — scope, standards, IT, design, their own formats, review process, questions — and produce the profile; about 45 minutes for a new customer, 10 for a change. Then ask whether this is a **new** customer or a **change** to an existing one (list `customers/` or the `--customer-dir`). For a change: read the existing files, summarise them in ten lines, and ask only what changes — skip to the steps concerned.

## Sequence (new customer) — one question at a time

1. **Customer and delivery.** Name (folder-safe, lowercase), org code (2–4 letters), document language (en / de), address form in conversations (`address: du | sie`), which skillsets (default all three; idea alone and maquette alone are valid), agent platform(s) the customer uses (cowork / chatgpt-codex / vibe-cli / other — decides the wording of start.md), recipient, contact for questions. Run `setup.py new <name> --code <CODE> --language <lang>` now, then edit `customer.yaml` for the rest.
2. **Versions.** Read `compat.md`, propose the latest triple, confirm or pin.
3. **Scope** → `scope.md`: departments and their codes, allowed topics and exclusions, company goals / AI or data strategy (name the document if one exists — `[evidenced]`).
4. **Standards** → `standards.md`: mandatory norms and certifications with contact persons, effort classes for V6 if not the defaults, house-specific requirement rows (trigger → required → verified by).
5. **IT** → `it-constraints.md`: allowed stacks and dependencies, hosting, network (none / allow-list), data rules incl. personal data. If build is ordered → `conventions.md`: repository layout, linters, CI, commit rules.
6. **Design** → `design.md`: corporate design tokens or "none". With tokens, say that design-3 will vary layout and density instead of colour.
7. **Their idea formats** → `import-formats.md`: does the customer already have idea lists, spreadsheets, a tool export? If a sample is pasted, draft the column → card-field mapping and read it back. Note encoding quirks.
8. **Review process** → `review.md`: who decides after a maquette, who signs each build gate, how (meeting, mail, in the chat); the customer's own next-step options if they replace the brief's defaults.
9. **Questions** → `questions.md`. Walk the ordered skillsets stage by stage, using `QUESTIONS.md`. Per stage, two questions: "Which of these does the customer already know — the answer becomes a `skip` with a value" and "Is anything missing that every idea / maquette / feature here must answer — that becomes an `add` after the question it belongs to". Gate questions cannot be skipped; say so if asked. Keep each reason to a few words.
10. **Modes and budgets** → `profile.md`: default maquette mode, build path, budgets per stage only if they deviate, sponsor and product-owner roles.
11. **Read back** the profile in one block (file → three lines each). On approval write the files, run `setup.py check <name>`, fix what it reports, then ask: "Build the ZIP now?" → `setup.py build <name>`. Report the ZIP path, its size and the start.md path. Offer `setup.py prompt <name> idea-collect` if the customer has people without folder-capable AI tools.

## Rules

- Restrict, never loosen: if a wish would relax a suite rule (write rules, git, "nothing outside planning/"), say it cannot go into a profile and note it as suite feedback.
- Placeholders that stay unanswered are left as they are; `setup.py` ships only files with content. Do not invent values — "core defaults" is a valid outcome for every file except `profile.md`.
- Every `skip` value is shown to the customer's user as "from your profile" and confirmed once — say that when the customer wants a hard, silent default; the profile cannot silence the user's right to correct.
- Never write customer material anywhere except `customers/<name>/` or the `--customer-dir`. Never commit `customers/`.
- Language of the dialogue: the maintainer's; profile content: the customer's document language; file headings stay English.

## Hand-back

Files written, `setup.py check` result, build number and ZIP path if built, open placeholders per file, and "Feedback to the suite" (wishes that need a suite change, with the skillset and the rule concerned).
