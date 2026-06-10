---
name: resume-tailor
description: Rewrite a resume for a specific job description using the tailored Python generator, mirroring the JD's terminology for skills the candidate genuinely has and asking the user to fill missing pieces. Use when the user provides a job description and asks to tailor, customize, or target a resume to it.
---

# Resume Tailor

Produces a single-page PDF tailored to one job description, built from
`user-knowledge/` using `templates/gen_resume_tailored_template.py`.

## Workflow

1. **Get the JD.** Ask for the full job description if not provided.

2. **Load knowledge.** Read all of `user-knowledge/`.

3. **Parse the JD.** Extract required qualifications, preferred/nice-to-haves, and
   the recurring terminology/entities (specific tools, frameworks, methods).

4. **Find and fill gaps.** Compare JD requirements to documented knowledge. For any
   JD item that might be true but is not recorded, ASK the user (use AskQuestion,
   multi-select) which they genuinely have. Record confirmed facts to
   `user-knowledge/`. Never fabricate to improve the match.

5. **Create the working generator.** Copy the tailored template:
   ```bash
   cp templates/gen_resume_tailored_template.py output/resume_tailored_gen.py
   ```
   Edit it and set `OUTPUT_PATH` (e.g. `output/<lastname>_resume_<role>.pdf`).
   Tailor the content:
   - Subtitle and summary oriented to the role.
   - Skills reordered and reworded to mirror JD terms the candidate truly has.
   - Most JD-relevant experience bullets first; reframe in the JD's language where
     genuinely accurate. Surface real keywords in CONTEXT (bullets), not just the
     skills list, since that ranks better in ATS/semantic matchers.
   - Use the deep `project_header` + multi-`bullet` block for the single most
     relevant project; compress or drop the least relevant content.

6. **Enforce hard rules.** ASCII only (no em dashes/smart quotes); one page.

7. **Generate and fit.** Run it; read `Final Y` and iterate to FITS / `Pages: 1`.

8. **Deliver.** Report the path and a short note on how it was tailored. Flag any
   JD requirement the candidate does not meet (hand off to `resume-fitment` if they
   want a full gap analysis).

## Setup

If `fpdf` is missing: `pip install -r requirements.txt`.

## Honesty guard

Tailoring means emphasis and wording, never invention. If the candidate lacks a
required skill, say so plainly rather than implying it.
