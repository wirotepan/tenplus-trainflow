# Triage Labels

The skills speak in terms of five canonical triage roles. This file maps those roles to the actual
label strings used in this repo's issue tracker (flow-core Project `CCM` — see
`issue-tracker.md`).

flow-core labels are free-form strings, so the canonical names are used verbatim. There is no
pre-existing label taxonomy to collide with.

| Label in mattpocock/skills | Label in our tracker | Status lane | Meaning                                  |
| -------------------------- | -------------------- | ----------- | ---------------------------------------- |
| `needs-triage`             | `needs-triage`       | `Backlog`   | Maintainer needs to evaluate this issue  |
| `needs-info`               | `needs-info`         | `Backlog`   | Waiting on reporter for more information |
| `ready-for-agent`          | `ready-for-agent`    | `Todo`      | Fully specified, ready for an AFK agent  |
| `ready-for-human`          | `ready-for-human`    | `Todo`      | Requires human implementation            |
| `wontfix`                  | `wontfix`            | `Canceled`  | Will not be actioned                     |

When a skill mentions a role (e.g. "apply the AFK-ready triage label"), use the corresponding label
string from this table.

## Labels and status are separate axes

The label says **what kind of attention the ticket needs**. The status lane says **where it is in
the flow**. A triage move sets both:

- Applying `ready-for-agent` → also `move_task_status` to `Todo`.
- Applying `wontfix` → also `move_task_status` to `Canceled`.

Once work actually starts, the status lane moves on (`InProgress` → `InReview` → `Done`) and the
triage label is removed — a ticket in flight is no longer waiting on triage.

## Applying labels safely

Use `update_task` with `addLabels` / `removeLabels`. **Never** set the bare `labels` array for a
triage change: it replaces every existing label wholesale and will drop non-triage labels
(`wayfinder:*`, module tags) that other skills rely on.

A ticket carries at most one triage label at a time. When moving between states, remove the old one
in the same `update_task` call:

```
update_task(taskId, addLabels: ["ready-for-agent"], removeLabels: ["needs-triage", "needs-info"])
```

Edit the right-hand columns to match whatever vocabulary you actually use.
