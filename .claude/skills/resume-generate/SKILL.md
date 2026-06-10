---
name: resume-generate
description: Generate a new single-page PDF resume from the candidate's documented knowledge using the Python generator template. Use when the user asks to build, generate, create, or refresh their main (non-tailored) resume.
---

# Resume Generate

Builds a fresh general-purpose resume PDF from `user-knowledge/` plus any new
information the user provides, using `templates/gen_resume_template.py`.

## Workflow

1. **Load knowledge.** Read all of `user-knowledge/`. If the user supplied new
   facts in the request, capture them to `user-knowledge/` first (see
   `.claude/rules/user-knowledge.md`), then proceed.

2. **Check completeness.** A solid resume needs: name + contact, a summary, skills,
   at least one role with measurable bullets, education. If anything essential is
   missing, ask the user (use AskQuestion) before generating. Do not invent facts.

3. **Create the working generator.** Copy the template to the output workspace:
   ```bash
   cp templates/gen_resume_template.py output/resume_gen.py
   ```
   Edit `output/resume_gen.py`: replace the CONTENT block and `OUTPUT_PATH`
   (e.g. `output/<lastname>_resume.pdf`) with the user's real data. Honor
   `user-knowledge/preferences.md`.

4. **Enforce the hard rules.**
   - ASCII only. No em dashes (`—` or `--` as sentence dashes), no smart quotes.
     Use commas, colons, or " - ".
   - Order sections by strength; lead bullets with strong verbs and metrics.

5. **Generate and fit.** Run it:
   ```bash
   python3 output/resume_gen.py
   ```
   Read the printed `Final Y: <n> / 792 (FITS|OVERFLOW)`. If OVERFLOW, trim or
   tighten content (shorten bullets, drop the weakest item, reduce summary) and
   re-run until it reports FITS and `Pages: 1`.

6. **Deliver.** Report the output path. Offer to run `resume-review` on it.

## Setup

If `fpdf` is missing: `pip install -r requirements.txt`.

## Notes

- The template's helper methods (`section_divider`, `job_header`, `bullet`,
  `project_bullet`, `skill_row`, etc.) define the layout. Reuse them; do not
  restyle unless asked.
- Keep a single generator per resume variant so it can be regenerated later.
