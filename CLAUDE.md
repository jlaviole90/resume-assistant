# Resume Assistant

An AI-driven toolkit for building, tailoring, reviewing, and assessing resumes. The
assistant keeps a structured record of the candidate in `user-knowledge/` and uses
Python generators to produce clean, single-page PDF resumes.

## Layout

```
.claude/
  rules/user-knowledge.md      How/when to persist facts about the candidate
  skills/
    resume-review/             Validate any resume file; flags errors + AI tells
    resume-generate/           Build a general resume from documented knowledge
    resume-tailor/             Rewrite a resume for a specific job description
    resume-fitment/            Judge candidate vs JD fit, with hard gaps
    cover-letter/              Write a tailored cover letter (PDF or text)
    knowledge-intake/          Bootstrap user-knowledge from an existing resume
    interview-prep/            Likely questions + STAR talking points for a role
templates/
  gen_resume_template.py       Main resume generator (copy, fill, run)
  gen_resume_tailored_template.py  Tailored resume generator (deep project block)
  gen_cover_letter_template.py     Cover letter generator (PDF)
user-knowledge/                Single source of truth about the candidate
output/                        Generated working generators and PDFs (gitignored)
TODO.md                        Backlog (e.g. application-tracker)
requirements.txt               fpdf2
```

## Core concepts

- **`user-knowledge/` is the source of truth.** Read it before generating or
  assessing. Write to it whenever the user shares durable facts (see the rule in
  `.claude/rules/user-knowledge.md`). Never fabricate facts to improve a match.
- **Templates are copied, not edited in place.** Each skill copies a template into
  `output/`, fills the CONTENT block from `user-knowledge/`, and runs it.
- **One page, always.** Every generator prints `Final Y: <n> / 792 (FITS|OVERFLOW)`
  and `Pages: N`. Iterate until it FITS on one page.
- **ASCII only. No em dashes.** No `—` or `--` as sentence dashes, no smart quotes.
  Use commas, colons, or " - ". The review skill flags em dashes as an AI tell, and
  the Helvetica core font cannot encode them anyway.
- **Honesty over optimization.** Tailoring is emphasis and wording, never
  invention. Surface real-but-buried experience; do not claim skills the candidate
  lacks.

## Skills quick reference

| Intent | Skill |
|--------|-------|
| "Import / set up from my existing resume" | `knowledge-intake` |
| "Review / proofread this resume" | `resume-review` |
| "Build / generate my resume" | `resume-generate` |
| "Tailor my resume to this job" | `resume-tailor` |
| "How well do I fit this job?" | `resume-fitment` |
| "Write a cover letter for this job" | `cover-letter` |
| "Help me prep for the interview" | `interview-prep` |

## Setup

```bash
pip install -r requirements.txt
```

Generators run with `python3 output/<file>.py` and write PDFs into `output/`.
