# Rule: Persist user knowledge

`user-knowledge/` is the single source of truth about the candidate. Every resume
the assistant generates, tailors, or evaluates reads from it. Keep it accurate and
current.

## When to write

Whenever the user shares any durable fact about themselves, capture it in
`user-knowledge/` before moving on. Triggers include:

- A job, title, dates, employer, client, team, or scope
- An accomplishment, metric, or outcome (revenue, scale, latency, time saved)
- A skill, language, framework, tool, or platform they have actually used
- A project (what it is, the stack, the standout detail)
- Education, certifications, awards
- Style or formatting preferences (e.g. "no em dashes", subtitle wording)
- A correction to anything already recorded

Do NOT record one-off, job-specific phrasing here. Record the underlying facts;
phrasing is decided per resume.

## Where to write

| File | Holds |
|------|-------|
| `user-knowledge/profile.md` | Name, contact, links, location, headline/subtitle, summary themes |
| `user-knowledge/experience.md` | Jobs and clients: title, employer, dates, scope, bullets, metrics |
| `user-knowledge/projects.md` | Projects: name, stack, what it does, notable details, links |
| `user-knowledge/skills.md` | Skills the user genuinely has, grouped (languages, frameworks, cloud, data, practices) |
| `user-knowledge/education.md` | Degrees and schools |
| `user-knowledge/certifications.md` | Certifications, issuer, date (note if not yet earned) |
| `user-knowledge/preferences.md` | Formatting, tone, and content preferences |

If a fact does not fit, add it to the closest file rather than inventing new ones.

## How to write

- Update existing entries in place; do not duplicate. If a fact changes, edit it.
- Keep entries terse and factual. Bullet points over prose.
- Mark anything uncertain or aspirational explicitly (e.g. `cert (in progress, exp. May 2026)`).
- ASCII only. No em dashes or smart quotes, matching the resume output rules.

## Honesty guard

Only record skills and experience the user has actually confirmed. If a resume or
job description implies a skill the user has not confirmed, ask before recording it.
Never fabricate facts to improve a match.
