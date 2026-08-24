# Domain Docs

How the engineering skills should consume this repo's domain documentation when exploring the
codebase.

This repo is **single-context**: `apps/api`, `apps/web` and `packages/shared-types` share one
domain, one `prisma/schema.prisma`, and one `openapi.yaml`. There is no `CONTEXT-MAP.md`.

## Before exploring, read these

- **`CONTEXT.md`** at the repo root.
- **`docs/adr/`** — read ADRs that touch the area you're about to work in.

If any of these files don't exist, **proceed silently**. Don't flag their absence; don't suggest
creating them upfront. The `/domain-modeling` skill (reached via `/grill-with-docs` and
`/improve-codebase-architecture`) creates them lazily when terms or decisions actually get resolved.

Neither exists yet in this repo — that's expected.

## Existing docs worth reading

Until `CONTEXT.md` exists, these carry the domain language:

- `CLAUDE.md` — resume pointer, guardrails, decision log, MVP backlog
- `docs/01-requirements.md`, `docs/02-system-design.md`
- `packages/shared-types/` — SSOT for enums; the closest thing to a machine-readable glossary
- `prisma/schema.prisma` and `openapi.yaml` — the contract files

## File structure

```
/
├── CONTEXT.md
├── docs/adr/
│   ├── 0001-....md
│   └── 0002-....md
├── apps/
│   ├── api/
│   └── web/
└── packages/shared-types/
```

## Use the glossary's vocabulary

When your output names a domain concept (in a ticket title, a refactor proposal, a hypothesis, a
test name), use the term as defined in `CONTEXT.md`. Don't drift to synonyms the glossary explicitly
avoids.

If the concept you need isn't in the glossary yet, that's a signal — either you're inventing
language the project doesn't use (reconsider) or there's a real gap (note it for
`/domain-modeling`).

This is a Thai-domain product; several concepts have an established Thai term and an English one.
Record both in `CONTEXT.md` when the glossary is created, and prefer the term the existing code and
`CLAUDE.md` already use rather than introducing a third.

## Flag ADR conflicts

If your output contradicts an existing ADR, surface it explicitly rather than silently overriding:

> _Contradicts ADR-0007 (…) — but worth reopening because…_

`CLAUDE.md` also carries a **Decision log** section of already-settled calls. Treat entries there
as pre-ADR decisions: same rule — contradict them out loud, not silently.
