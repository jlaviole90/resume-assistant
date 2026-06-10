---
name: knowledge-intake
description: Bootstrap or update the candidate's user-knowledge files by parsing an existing resume (PDF, docx, txt, md) or other supplied materials. Use when the user wants to import an existing resume, set up their profile, or onboard to the assistant.
---

# Knowledge Intake

Populates `user-knowledge/` from an existing resume or other supplied materials, so
the generate/tailor/fitment skills have a source of truth to work from.

## Workflow

1. **Get the source.** Ask for the resume path (or LinkedIn export, bio, notes).
   Extract text:
   - PDF, txt, md: Read tool.
   - docx: `pandoc resume.docx -t plain -o /tmp/resume.txt` (fallback:
     `textutil -convert txt resume.docx -output /tmp/resume.txt`), then read.

2. **Parse into sections.** Map the content onto the knowledge files:
   - `profile.md`: name, contact, links, location, headline, summary themes
   - `experience.md`: each role/client with title, employer, dates, scope, bullets,
     metrics
   - `projects.md`: projects with stack and standout detail
   - `skills.md`: skills grouped by category
   - `education.md`, `certifications.md`

3. **Write the files.** Update existing entries in place; do not duplicate. Keep
   entries terse and factual. ASCII only.

4. **Flag uncertainty.** Anything ambiguous, undated, or possibly aspirational:
   ask the user to confirm rather than guessing. Mark in-progress items explicitly
   (e.g. a certification not yet earned).

5. **Confirm.** Summarize what was imported and what is missing or needs
   confirmation. Suggest filling `preferences.md` (dashes, tone, length) if empty.

## Principles

- Record only what the source actually states or the user confirms. Do not invent
  or upgrade titles, metrics, or skills.
- This skill writes the knowledge base; it does not produce a resume. Hand off to
  `resume-generate` afterward.
