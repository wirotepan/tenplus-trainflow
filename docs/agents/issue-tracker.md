# Issue tracker: flow-core

Issues, PRDs and tickets for this repo live in **flow-core**, DCS's own tracker, under the Project
**Cost Center Management** (`code: CCM`, `projectId: 6a5d8087cc4fa26dd9b4816d`). Task Keys are
`CCM-1`, `CCM-2`, …

All operations go through the `flow-core` MCP server (`mcp__flow-core__*`). There is no CLI.
GitHub Issues on `dcsolution-th/cost-center-mananamgent-dcs` is **not** used — do not create issues
there. GitHub still hosts the code and pull requests; only the *ticket* surface moved.

## Prerequisites

The `flow-core` MCP server must be connected and its PAT valid. Required PAT scopes:
`tasks:read`, `tasks:write`, `projects:write` (project creation only).

If a call returns an auth error, the PAT is stale — restart the MCP server rather than retrying.
In headless / cron / background runs the MCP server may not be connected at all. If it isn't,
**stop and report** rather than silently falling back to GitHub Issues.

## Conventions

- **Create an issue**: `create_task` with `projectId: "6a5d8087cc4fa26dd9b4816d"`, `title`, and a
  `description` holding the full body. Pass `labels` at creation time when triage state is already
  known.
- **Read an issue**: `get_task` with the Task's ObjectId. To resolve a Task Key first, use
  `list_tasks` with `key: "CCM-42"`. Comments come back with the Task; use `list_comments` if you
  need them separately.
- **List issues**: `list_tasks` with `projectId: "6a5d8087cc4fa26dd9b4816d"`, plus `status`,
  `label`, `epicId` or `q` filters. Cursor-paginated — follow `cursor` until exhausted rather than
  assuming one page is the whole set.
- **Comment on an issue**: `add_comment` with the Task's ObjectId.
- **Apply / remove labels**: `update_task` with `addLabels` / `removeLabels`. Never use the bare
  `labels` field for a triage change — it **replaces the entire label array** and will silently drop
  labels set by other skills.
- **Close**: `move_task_status` to `Done` (completed) or `Canceled` (won't fix), then `add_comment`
  with the reason.
- **Group work**: `create_epic` under the Project, then set `epicId` on member Tasks. Use Epics for
  what GitHub-shaped skills call a milestone.
- **Sub-tasks**: `create_task` with `parentId` set to the parent Task's ObjectId.
- **Relations**: `link_tasks` with `type` of `Blocks`, `Relates` or `Duplicate`. For `Blocks`,
  `fromTaskId` is the **blocker** and `toTaskId` is the **blocked** Task.

Task ObjectIds are opaque Mongo ObjectIds, not the human-facing Key. Skills that quote a ticket to
the user should quote the Key (`CCM-42`); calls need the ObjectId.

## Status lanes

`Backlog` · `Todo` · `InProgress` · `InReview` · `Done` · `Canceled`

Transitions are free — any lane can move to any other. Status answers *"where is this in the
flow"*; labels answer *"what kind of attention does it need"*. See `triage-labels.md` for how the
two combine.

## Pull requests as a triage surface

**No.** flow-core has no PR concept, and this is a private product repo with no external
contributors. Code review happens on GitHub PRs; those PRs reference their Task Key
(e.g. `CCM-42`) in the title or body, but they never enter the triage queue themselves.

## When a skill says "publish to the issue tracker"

Create a flow-core Task under Project `CCM` with `create_task`.

## When a skill says "fetch the relevant ticket"

`list_tasks` with `key: "CCM-<n>"` to resolve the ObjectId, then `get_task` and `list_comments`.

## Wayfinding operations

Used by `/wayfinder`. The **map** is a single Task; tickets are its **sub-tasks**.

- **Map**: a Task labelled `wayfinder:map`, whose `description` holds the Notes /
  Decisions-so-far / Fog body.
- **Child ticket**: a Task created with `parentId` set to the map Task's ObjectId, labelled
  `wayfinder:<type>` (`research` / `prototype` / `grilling` / `task`).
- **Blocking**: `link_tasks` with `type: "Blocks"` — blocker as `fromTaskId`, blocked as
  `toTaskId`. Cycles are rejected by the server. A ticket is unblocked when every blocker sits in
  `Done` or `Canceled`.
- **Frontier query**: `list_tasks` with `parentId: "<map ObjectId>"`, drop Tasks in `Done` /
  `Canceled`, drop Tasks with a blocker still open, drop Tasks that already have assignees. First
  in order wins.
- **Claim**: `update_task` with `assigneeIds: ["<your User ObjectId>"]`. Note the literal `"me"`
  shorthand works only as a *filter* on `list_tasks` — writes need the real ObjectId. Resolve it
  once per session (`list_tasks` with `assigneeId: "me"` on any Task you already own) and reuse it.
  `assigneeIds` **replaces** the whole assignee set; `[]` unassigns everyone.
- **Resolve**: `add_comment` with the answer, `move_task_status` to `Done`, then append a context
  pointer to the map Task's Decisions-so-far via `update_task`.
