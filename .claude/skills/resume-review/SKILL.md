---
name: resume-review
description: Scrutinize and validate a resume of any readable file type (PDF, docx, txt, md) for grammar, spelling, consistency, readability, skills, impact, and AI-generated tells like em dashes. Use when the user asks to review, critique, proofread, or validate a resume.
---

# Resume Review

Reviews a finished resume against general resume expectations and returns a
structured, prioritized report. The actual review runs in a fresh subagent so it
is not biased by prior conversation context.

## Workflow

1. **Get the file.** Ask for the resume path if not provided. Accept any readable
   type:
   - PDF, txt, md: read directly with the Read tool.
   - docx: convert first, then read the result. Try in order:
     - `pandoc resume.docx -t plain -o /tmp/resume.txt`
     - macOS fallback: `textutil -convert txt resume.docx -output /tmp/resume.txt`
   - If you cannot extract text, stop and tell the user.

2. **Spawn a review subagent.** Launch one subagent (Task tool, `generalPurpose`,
   `readonly: true`) with the prompt template below. Pass the FULL extracted resume
   text inline. Do not add your own commentary or prior context. This keeps the
   review clean.

3. **Relay the report.** Present the subagent's report to the user as-is, lightly
   formatted. Offer to fix the issues if they want.

## Subagent prompt template

> You are an expert resume reviewer. Review ONLY the resume text below. You have no
> other context; do not assume anything not present in the text.
>
> Evaluate against this rubric and report concrete, specific findings (quote the
> offending text and give the fix):
>
> 1. Spelling and grammar errors.
> 2. Consistency: verb tense within a role, punctuation, date formats (flag
>    "May." with an erroneous period and similar), capitalization, spacing
>    (e.g. "ReactNative" should be "React Native").
> 3. Readability and formatting: length vs. one page, section order, scannability,
>    overly dense or run-on bullets, filler words ("various", "responsible for").
> 4. Impact: bullets that state duties instead of measurable outcomes; missing
>    quantification; weak opening verbs.
> 5. Skills: filler/low-value entries (e.g. listing code editors as skills),
>    relevance, and obvious omissions.
> 6. AI-generated tells: em dashes (the characters U+2014 "—" or "--" used as
>    sentence dashes), smart quotes, and overused AI phrasing ("leverage",
>    "robust", "seamless", "delve", uniform tricolon sentences, generic openers).
>    Call these out explicitly and recommend removal.
> 7. Contact/links sanity and professionalism.
>
> Output exactly these sections:
> - **Verdict**: one or two sentences on overall quality.
> - **Must-fix (errors)**: outright mistakes.
> - **Should-fix (impact)**: changes that materially improve it.
> - **Polish (optional)**: minor refinements.
> - **AI tells found**: list each, or "none".
> Keep it specific. Quote the text. No filler.
>
> RESUME TEXT:
> ```
> <paste full extracted resume text here>
> ```

## Notes

- This skill only reviews. It does not edit. After relaying the report, ask if the
  user wants the issues fixed (and whether to update `user-knowledge/`).
- If the resume is one of the candidate's own (in `output/`), the same rubric
  applies.
