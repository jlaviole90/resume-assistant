# Agent Instructions

This project's full configuration lives in the Claude-specific setup. To avoid
duplicating it, any agent working here should read and follow that setup directly:

1. Read **`CLAUDE.md`** in the repo root. It is the authoritative guide: layout,
   core conventions (single source of truth in `user-knowledge/`, one-page output,
   ASCII only / no em dashes, honesty over optimization), and the skill index.
2. Read the rule in **`.claude/rules/`** and apply it (persisting candidate facts to
   `user-knowledge/`).
3. Use the skills in **`.claude/skills/<name>/SKILL.md`**. Each `SKILL.md` has a
   `name` and `description` (when to use it) plus its workflow. Match the user's
   request to the right skill via the index in `CLAUDE.md`, then follow that
   skill's `SKILL.md`.

Treat `CLAUDE.md` and everything under `.claude/` as the source of truth. If
guidance ever appears to conflict, `CLAUDE.md` wins.
