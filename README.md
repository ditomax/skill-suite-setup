# skill-suite-setup

**Builds customer versions of the DMBG skill suite — idea → maquette → build — as `start.md` + one ZIP.**

Version: see `VERSION` · September 2026 · DMBG · https://github.com/ditomax/skill-suite-setup

This is the maintainers' tool. It takes the three skillset repos ([idea](https://github.com/ditomax/idea), [maquette](https://github.com/ditomax/maquette), [build](https://github.com/ditomax/build)) at pinned versions, adds a customer profile produced in a guided dialogue, and renders a delivery that the customer's IT unzips into a project folder. Nothing is installed or fetched at the customer; the agent reads `planning/AGENTS.md` / `planning/CLAUDE.md` when the folder is opened and acts as the right Director. Anyone who knows the suite may use this repo to tailor their own version.

## Usage

```
git clone https://github.com/ditomax/idea
git clone https://github.com/ditomax/maquette
git clone https://github.com/ditomax/build
git clone https://github.com/ditomax/skill-suite-setup
# all four side by side in one parent folder (the dev layout) — or pass --suites DIR to point elsewhere
cd skill-suite-setup
python3 setup.py new acme --code ACM --language de          # scaffold customers/acme/
# run the tailoring dialogue (skills/setup/SKILL.md) or edit customers/acme/profile/*.md by hand
python3 setup.py check acme                                  # versions vs compat.md, question IDs, profile files
python3 setup.py build acme                                  # dist/acme-suite-v1.zip + dist/acme-start-v1.md
python3 setup.py prompt acme idea-collect                    # optional: prompt file for chat tools without folder access
```

`--customer-dir <path>` keeps a customer's folder inside the customer project instead of `customers/` (which is gitignored either way). A complete, fictitious customer is in `examples/example` — `python3 setup.py build example --customer-dir examples` shows the whole flow. Python ≥ 3.10, no dependencies.

## What the ZIP contains

```
AGENTS.md  CLAUDE.md          static pointer to planning/AGENTS.md — appended if the project already has one
start.md                     three steps for the human, in the customer's language, plus the update rule — static
planning/
  AGENTS.md  CLAUDE.md       static pointer to suite/AGENTS.md
  suite/
    AGENTS.md  CLAUDE.md     the bootstrap: dispatch rule (which skillset is up), installed versions, hard limits, update rule
    VERSION                  customer, build number, skillset versions, setup version, date
    <idea|maquette|build>/   the ordered skillsets, pinned, standalone bootstraps stripped
  profile/                   the customer's constraints — only files with content
  idea/ maquette/ build/     empty work folders
```

Everything that changes between builds lives under `planning/suite/` and `planning/profile/`; everything else is static. So an update never deletes and never overwrites: move the two folders to `planning/_archive/`, then `unzip -n` (or extract elsewhere and move the two folders in). The rule is in `start.md` and in `planning/suite/AGENTS.md`, so a human or an agent can do it — also in sandboxes that forbid deleting.

## Profile

The profile format is specified in `PROFILE.md` (owned here; derived from the design document in skill-suite-dev); the skillsets only read it. Files: `profile.md` (always), `questions.md`, `scope.md`, `standards.md`, `it-constraints.md`, `design.md`, `import-formats.md`, `conventions.md`, `review.md`. A profile may restrict, never loosen. `questions.md` tailors the questions each skillset asks, by the IDs in its `QUESTIONS.md`: `skip` with a value (shown as prefilled, confirmed once) or `add` after a named question.

## Customer-data guard

Customer information must never reach a public repo or a ZIP, except the target customer's own profile. Four layers enforce it: `setup.py build` and `release.py` ship only an allowlist of files (never "everything minus"); `guard.py` scans every shipped file against a private marker list (`../guard-markers.txt`, outside every repo — one `[group]` per customer) and refuses other customers' markers in a profile and any marker in suite files; every profile file's first line must name its customer; and `hooks/pre-commit` (activate once per clone: `git config core.hooksPath hooks`) blocks commits with markers in all four repos.

```
python3 guard.py scan ../idea ../maquette ../build          # clean?
python3 release.py maquette                                  # public release ZIP, guarded, from git-tracked files only
```

## Structure

```
setup.py            new · check · build · prompt · list
guard.py            customer-marker scan (scan / staged)
release.py          public release ZIP of one skillset, guarded
hooks/pre-commit    the guard as a git hook — copy of the one in each skillset repo
PROFILE.md          the profile specification the skillsets read
compat.md           version triples known to work together, with contract versions H1/H2
skills/setup/       the tailoring dialogue
templates/          root-AGENTS.md · planning-AGENTS.md · planning-pointer-AGENTS.md · start.en.md · start.de.md · customer.yaml · profile/*.md · prompt-idea-collect.md
customers/          gitignored — one folder per customer
examples/example/   a fictitious customer (Example GmbH) — the reference for a filled profile
AGENTS.md CLAUDE.md bootstrap for an agent working in this repo
CHANGELOG.md
dist/               gitignored — built ZIPs, start files, prompt files
tests/              smoke-test logs per platform
```

## License

© 2026 Dietmar Millinger, MIT License (`LICENSE`).
