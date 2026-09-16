# Start — DMBG skill suite for {{customer}}

You received a ZIP file and this page. The ZIP contains a planning structure and the AI skill suite **{{skillsets_list}}** (the exact versions are in `planning/suite/VERSION` after unzipping). Nothing gets installed: it is text files that your AI app reads when you open the folder.

## 1. Unzip

Unzip the ZIP into your project folder — a new empty folder, or an existing project. Result: a `planning/` folder plus two short files `AGENTS.md` and `CLAUDE.md` at the top level. If your project already has an `AGENTS.md` or `CLAUDE.md`, append the content of the ZIP's file to yours instead of replacing it (the block is five lines and only says "read planning/AGENTS.md").

## 2. Open the folder in your AI app

{{platform_hint}}

For idea collection and maquettes, opening `planning/` is enough. For build (product development), open the project folder itself, because the code is written next to `planning/`, not inside it.

## 3. Type "start"

The AI reads the rules from the folder, tells you where things stand and what comes next, and asks after every step: **next**, **redo** or **stop**. There are no other commands. You can stop at any time — everything stays in `planning/` as readable text files and continues next time with **next**.

## Update

When you receive a newer ZIP, three steps — nothing is ever deleted, and your work in `planning/idea`, `planning/maquette` and `planning/build` is not touched:

1. Move `planning/suite` and `planning/profile` into `planning/_archive/` (e.g. `_archive/2026-10-01-suite-v1`).
2. Extract the new ZIP **somewhere else** (Finder/Explorer double-click makes a new folder) and move its `planning/suite` and `planning/profile` folders into your `planning/`. In a terminal, `unzip -n <zip>` in the project folder does the same and never overwrites anything.
3. Done. `planning/suite/VERSION` shows the new version.

Or simply give the ZIP to the AI and say "update"; it knows this rule.

Changes to your profile (constraints, questions, design) go through {{contact}} — they come back as a new ZIP.

## Questions

{{contact}}
