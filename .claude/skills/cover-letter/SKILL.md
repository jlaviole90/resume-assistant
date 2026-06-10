---
name: cover-letter
description: Write a tailored cover letter for a specific job, as a styled one-page PDF or as plain text for a textarea, drawing on the candidate's documented knowledge. Use when the user asks for a cover letter or a written application letter for a role.
---

# Cover Letter

Writes a cover letter tailored to one job, grounded in `user-knowledge/`. Supports
two output modes.

## Choose the mode

Ask (or infer) which the user wants:
- **PDF** (default): a styled one-page letter matching the resume look, via
  `templates/gen_cover_letter_template.py`.
- **Text**: plain prose to paste into a textarea/application field. Skip the
  generator; just write and return the text.

## Workflow

1. **Gather inputs.** Get the JD and read `user-knowledge/`. Capture any new facts
   to `user-knowledge/` first (see `.claude/rules/user-knowledge.md`).

2. **Draft the letter.** Structure: hook tied to the team's mission/charter, one or
   two proof paragraphs (real experience/projects mapped to the role with metrics),
   a close on fit and motivation, and a thank-you. Mirror the JD's language only
   where genuinely true.

3. **Apply hard rules.**
   - ASCII only. No em dashes (`—` or `--` as sentence dashes), no smart quotes.
   - Be honest about any partial fit rather than overclaiming.
   - Honor `user-knowledge/preferences.md` (tone, things to always/never include).

4. **Produce output.**
   - **Text mode:** return the prose directly.
   - **PDF mode:**
     ```bash
     cp templates/gen_cover_letter_template.py output/cover_letter_gen.py
     ```
     Fill `NAME`, `CONTACT`, `ROLE`, `COMPANY`, `GREETING`, `PARAGRAPHS`,
     `CLOSING`, and `OUTPUT_PATH` (e.g. `output/<lastname>_cover_<company>.pdf`).
     Run `python3 output/cover_letter_gen.py` and confirm it prints FITS /
     `Pages: 1`. If OVERFLOW, tighten paragraphs and re-run.

5. **Deliver.** Report the path (PDF) or present the text, and note how it was
   tailored.

## Setup

If `fpdf` is missing: `pip install -r requirements.txt`.
