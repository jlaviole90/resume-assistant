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

## First-run bootstrap (autoload for your own tool)

If your tool autoloads skills/rules from a path other than `.claude/`, replicate
this setup into your expected location once, so it loads automatically going
forward. Keep `.claude/` as the canonical source; your copy must mirror it, not
diverge.

1. Detect your tool's conventional config path, for example:
   - Cursor: `.cursor/skills/<name>/SKILL.md` and `.cursor/rules/<name>.mdc`
   - Other tools: use whatever path that tool autoloads.
2. Mirror the contents of `.claude/skills/` (and `.claude/rules/`) there. Prefer
   symlinks so the two stay in sync automatically:
   - `mkdir -p .cursor && ln -s ../.claude/skills .cursor/skills`
   If symlinks are not viable, copy the files instead and re-copy whenever
   `.claude/` changes.
3. If your tool's rule format differs (e.g. Cursor `.mdc` needs YAML frontmatter
   with `description`/`globs`/`alwaysApply`), wrap the same rule content in that
   format rather than rewriting the guidance.
4. Do not edit the mirrored copies as a source of truth. Make changes in `.claude/`
   and re-sync.

