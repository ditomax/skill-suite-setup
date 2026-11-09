<!-- skill-suite pointer — appended by the suite ZIP; do not remove. -->
# Skill suite

This project uses the skill suite (idea → maquette → build) for planning work. Everything the suite needs lives in `planning/`. **Before any planning-related work, read `planning/AGENTS.md`** (Claude: `planning/CLAUDE.md`) and follow it. Product code lives outside `planning/`; the suite's build skillset is the only part that writes there.

**Secrets:** never put a secret into a shell command, a commit message, a tracked file or a chat answer — use environment variables or a git-ignored `.env`, refer to them by name. At a permission prompt, prefer a generalized rule over "don't ask again" on a literal command.
