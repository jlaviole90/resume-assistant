---
name: interview-prep
description: Generate likely interview questions and grounded talking points (including STAR stories) for a specific job, using the candidate's documented experience. Use when the user asks to prepare for an interview, practice questions, or build talking points for a role.
---

# Interview Prep

Produces interview preparation for a specific role, grounded in the candidate's real
experience from `user-knowledge/` (never invented).

## Workflow

1. **Gather inputs.** Get the JD (and company name if known). Read
   `user-knowledge/`. If a tailored resume for this role exists in `output/`, use it
   for consistency with what was submitted.

2. **Derive likely questions** across these buckets, weighted by the JD:
   - Behavioral (ownership, conflict, ambiguity, failure, leadership)
   - Role-specific technical / domain questions implied by the JD's requirements
   - Project deep-dives on the candidate's most relevant work
   - "Why this company / why this role" and reverse questions to ask them

3. **Build grounded answers.**
   - For behavioral questions, draft concise **STAR** outlines (Situation, Task,
     Action, Result) using real entries from `user-knowledge/`. Prefer stories with
     measurable results.
   - For technical questions, give talking points and the candidate's genuine
     experience to anchor on. Flag any area that is a real gap so they can prepare
     honestly rather than bluff.

4. **Output** a tight prep doc:
   - **Likely questions** grouped by bucket
   - **STAR stories** (2 to 5 reusable ones mapped to common prompts)
   - **Why-them / why-you** talking points
   - **Questions to ask the interviewer**
   - **Gaps to prepare for** (honest weak spots and how to address them)

## Principles

- Ground everything in real experience. Do not fabricate stories or results.
- Be honest about gaps; the goal is genuine readiness, not a script to bluff with.
- Pairs well with `resume-fitment` (its hard-gaps output feeds the "gaps to prepare
  for" section).
