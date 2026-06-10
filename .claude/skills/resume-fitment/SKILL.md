---
name: resume-fitment
description: Judge how well the candidate and their resume fit a given job description, with a requirement-by-requirement match, an honest verdict, actionable improvements, and hard skill gaps that wording cannot fix. Use when the user provides a job description and asks how well they fit, whether to apply, or for a fit/gap analysis.
---

# Resume Fitment

Assesses fit between the candidate and a specific job description. Honest and
actionable: separates fixable presentation gaps from real, hard skill gaps.

## Workflow

1. **Gather inputs.** Get the JD. Use `user-knowledge/` as the candidate's source
   of truth; if a current resume PDF is referenced, read it too for what is actually
   being presented.

2. **Parse the JD** into:
   - Must-haves (required qualifications)
   - Nice-to-haves (preferred)
   - Implicit signals (domain, seniority, scale, culture)

3. **Map evidence.** For each requirement, find concrete evidence in the
   candidate's knowledge/resume. Mark each: met, partial, or gap.

4. **Judge honestly.** Do not inflate. A "partial" on a stated minimum qualification
   is a real risk; say so. Distinguish:
   - **Fixable gaps**: real experience that is just missing or buried in the resume
     (fix by surfacing/rewording).
   - **Hard gaps**: skills/experience the candidate genuinely lacks (cannot be
     fixed by wording; only by learning or by not applying).

5. **Report** using this structure:
   - **Verdict**: strong / moderate / stretch / poor fit, in one or two sentences,
     and whether it is worth applying.
   - **Fit table**: requirement -> evidence -> met/partial/gap.
   - **Actionable improvements**: specific resume/profile changes that raise the
     match (skills to surface, bullets to reframe, JD terms to mirror honestly).
   - **Hard gaps**: the genuine shortfalls, stated plainly, with whether each is a
     likely screen-out.

6. **Offer next step.** If fit is reasonable, offer to run `resume-tailor` for this
   JD. If improvements require facts not yet recorded, ask and update
   `user-knowledge/`.

## Principles

- Be candid. The point is to save the user from low-odds applications and to focus
  effort where it pays off.
- Never recommend fabricating a qualification. Surfacing real-but-buried
  experience is encouraged; inventing it is not.
