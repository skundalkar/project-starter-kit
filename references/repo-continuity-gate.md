# Project Starter Kit: Repo & Continuity Gate

## Purpose

Prevent project work from remaining silently local after it has become valuable.

This gate makes repository status explicit before Spec Kit, implementation, major
prototype work, and milestone completion.

## Project Scale

Classify the project scale as early as possible and update it when the work grows.

| Scale | Meaning | Repository expectation |
| --- | --- | --- |
| `scratch` | Throwaway exploration, no expected reuse | Git optional; no GitHub required |
| `local_prototype` | Useful local artifact or prototype | Local Git required before implementation |
| `private_project` | User wants to preserve, resume, or evolve the work | Local Git and private GitHub remote required before implementation |
| `collaborative_project` | Multiple agents, reviewers, or users may work on it | GitHub remote required before Spec Kit tasks or implementation |
| `production_path` | Deployable, customer-facing, sensitive, or long-lived work | GitHub remote, commit discipline, and milestone push checks required |

Default to `private_project` when the user says to build an app, dashboard, service,
tool, monitor, or any project expected to continue beyond the current conversation.

## Required Checks

Run and report these checks at the gate:

- `git status --short --branch`
- `git rev-list --count HEAD`
- `git log --oneline --max-count=3`
- `git remote -v`

If there is no Git repository, ask to initialize one before implementation.

If there is no GitHub remote and the project scale is `private_project`,
`collaborative_project`, or `production_path`, ask to create one. Default to private
visibility unless the user explicitly asks for public.

If the user declines a remote, record that decision in the starter artifacts or plan
and repeat the warning before milestone completion.

## Blocking Rule

Do not begin implementation for `private_project`, `collaborative_project`, or
`production_path` scale until repository status has been reported and the user has
either approved GitHub setup or explicitly deferred it.

Do not present a milestone as complete until the latest commit and push status are
reported.

## Repository Status Report

Use this format in status updates and final outputs:

```text
Repository status:
- Project scale:
- Local git repo:
- Current branch:
- Commit count:
- Latest commit:
- GitHub remote:
- Pushed to remote:
- Repo URL:
- Deferred decision, if any:
```

## Artifact Recording

Record repository status in `project-brief.md` once the project has a name and scale.
Record milestone push status in `build-brief.md`, Spec Kit plan/task updates, or a
solution note when implementation begins.

After shaping approval, create `project-index.md` from `templates/project-index.md` for `private_project`, `collaborative_project`, or `production_path`. The index is a Pyramid Index and entry point; it links to the three starter artifacts and later Spec Kit files without becoming a new source of truth.

## When To Rerun

Rerun this gate when:

- starter artifacts are approved
- Spec Kit handoff starts
- implementation starts
- the project receives its first meaningful commit
- a milestone is complete
- a user asks whether work is local or in GitHub
- a repo/folder is renamed
- raw data, generated artifacts, or large files are about to be committed
