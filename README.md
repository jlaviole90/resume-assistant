# resume-assistant

An AI-assistant toolkit for building, tailoring, reviewing, and assessing resumes.
It is designed to be driven by an agent (see `CLAUDE.md`) but the generators are
plain Python you can run yourself.

## What's inside

- **Skills** (`.claude/skills/`) the agent uses:
  - `knowledge-intake` bootstraps your `user-knowledge/` files from an existing
    resume (PDF, docx, txt, md).
  - `resume-review` validates any resume file (PDF, docx, txt, md) for grammar,
    spelling, consistency, readability, and AI-generated tells like em dashes. The
    review runs in a fresh subagent so it is not biased by prior context.
  - `resume-generate` builds a general single-page resume from your documented
    knowledge.
  - `resume-tailor` rewrites a resume for a specific job description, mirroring the
    JD's terminology for skills you genuinely have.
  - `resume-fitment` judges how well you fit a job description, with actionable
    improvements and honest hard gaps.
  - `cover-letter` writes a tailored cover letter as a styled PDF or as plain text
    for a textarea.
  - `interview-prep` generates likely interview questions and STAR talking points
    grounded in your real experience.
- **Knowledge base** (`user-knowledge/`): the single source of truth about you.
  Fill these in; the agent reads and updates them.
- **Generators** (`templates/`): `fpdf2`-based Python that renders clean, ATS-
  friendly, one-page PDFs.

## Quick start

```bash
pip install -r requirements.txt

# Try the templates directly
python3 templates/gen_resume_template.py
python3 templates/gen_resume_tailored_template.py
python3 templates/gen_cover_letter_template.py
# -> writes PDFs into output/ and prints a one-page fit check
```

Then fill in `user-knowledge/` and ask the agent to generate, tailor, review, or
assess your resume.

## Conventions

- Output is a single page. Generators print `Final Y: <n> / 792 (FITS|OVERFLOW)`.
- ASCII only, no em dashes or smart quotes.
- Nothing is fabricated: tailoring is emphasis and wording, never invented skills.
