# Project Starter Kit: Spec Kit Start Protocol

## Purpose

Use this protocol after Project Starter Kit has completed discovery, prototype challenge, and build brief generation.

This protocol prepares the current project folder for Spec Kit and eventual implementation.

## Spec Kit Context

Spec Kit is GitHub's open source toolkit for Spec-Driven Development.

Official references:

- GitHub repository: https://github.com/github/spec-kit
- Documentation: https://github.github.io/spec-kit/

In this workflow:

```text
Project Starter Kit
-> product discovery, Product Design Gate, prototype challenge, project brief, build brief

Spec Kit
-> specification, technical plan, tasks, implementation, analysis
```

Use Spec Kit after Project Starter Kit has produced the local starter artifacts.

Do not guess Spec Kit command syntax. Inspect the local environment and available commands. If Spec Kit is unavailable, consult the official repo/docs or explain exactly what setup is needed.

## Repo & Continuity Gate

Before Spec Kit handoff, run `repo-continuity-gate.md`. Record project scale, local Git status, commit count, remote status, push status, and repo URL when available.

For `private_project`, `collaborative_project`, or `production_path`, GitHub remote setup is required before implementation unless the user explicitly defers it. If deferred, record the decision and repeat the warning before milestone completion.

## Required Local Artifacts

Before starting, confirm these files exist in the current project folder:

- `project-brief.md`
- `prototype-pass.md`
- `build-brief.md`

If any are missing, stop and return to Project Starter Kit discovery or artifact generation.

## Source Of Truth

Use the local Project Starter Kit artifacts as the source of truth:

- `project-brief.md` defines product direction, user, promise, MVP boundary, and non-goals.
- `prototype-pass.md` defines Product Design Gate decisions, operating-model choices, feasibility findings, and product decisions changed by prototype/walkthrough work.
- `build-brief.md` defines the implementation handoff.

Do not restart product discovery unless the files are contradictory, incomplete, or impossible to implement.

Do not let Spec Kit, review frameworks, or implementation convenience change the approved product name, MVP scope, product promise, or core UX direction without asking the user.

## User Confirmation

Ask after repository status is explicit:

"Do you want to create or confirm a private GitHub repo and start the Spec Kit handoff for this project?"

If yes, ask or confirm:

- project name
- repository name
- private or public repository
- GitHub remote preference, if needed

## Repository Setup

1. Create or confirm the local project folder.
2. Create or confirm the Git repository.
3. Create the private GitHub repository if requested.
4. Keep the generated Project Starter Kit artifacts in the repo.
5. Commit documentation and starter artifacts before any application code.
6. Push periodically if a remote is configured. If no remote exists, record the user-approved deferral and explain what remote setup is needed.
7. Before implementation and milestone completion, report whether the latest commit is pushed.

## Git History Preference

Preserve the real sequence of work.

Default branch-to-main preference:

- Do not squash feature branch commits into one commit unless the user explicitly asks.
- Prefer merge commits when merging feature branches into `main`.
- Use a non-fast-forward merge where practical, for example `git merge --no-ff <branch>`.
- The goal is for `main` to reflect the actual number and order of meaningful commits from the branch.

If a hosting platform or repository policy requires a different merge strategy, explain the tradeoff and ask the user before merging.

## Commit Discipline

- Commit documentation first.
- Keep generated specs, technical plans, tasks, and implementation changes cleanly separated where practical.
- Commit each meaningful feature separately.
- Keep data/model commits separate from UI/application feature commits.
- Do not squash branch commits into one commit unless the user explicitly asks.

## Spec Kit Setup

1. Check whether Spec Kit is available in the environment.
2. If unavailable, inspect official setup instructions or explain what setup is needed.
3. Initialize Spec Kit for the project.
4. Use these files as the source material:
   - `project-brief.md`
   - `prototype-pass.md`
   - `build-brief.md`
5. Create or update the project constitution/principles using the product goals, quality expectations, commit discipline, data/trust requirements, UX standards, and MVP boundaries from the starter artifacts.

## Spec Kit Generation Flow

1. Generate the Spec Kit specification.
2. Stop and ask the user to approve the specification.
3. After approval, generate the technical plan.
4. Stop and ask the user to approve the technical plan.
5. After plan approval, run the Intermediate Specialist Review Quality Gate when triggered.
6. After approved review changes are applied, generate tasks.
7. Begin implementation only after tasks exist.
8. Run Spec Kit analysis/checks, if available, to compare starter artifacts, generated spec, plan, tasks, and implementation.

## Intermediate Specialist Review Quality Gate

Use this gate after technical plan approval and before task generation when the
project has high-risk data, AI, trust/safety, analytics, UX, platform, workflow,
or architecture assumptions.

Trigger examples:

- the plan depends on a data source, baseline, model, classifier, external API, or
  provider constraint that could invalidate the product
- user-facing trust, safety, legal, financial, medical, identity, or account-level
  conclusions are involved
- visual/dashboard/workflow choices materially affect decision quality
- multiple technical paths remain plausible and task generation would prematurely
  harden the wrong one
- the user asks for more eyes, a second opinion, specialist review, or different
  perspectives

Recommended review lenses:

- Product/MVP review: user value, MVP boundary, scope creep, missing decisions
- Data/analytics review: baselines, scoring, leakage, data completeness, replay validity
- Technical architecture review: interfaces, contracts, testability, implementation risks
- Trust/safety review: evidence, confidence, false positives, account-level language
- UX/dashboard review: scanability, comparison quality, drilldown usefulness

Quality gate procedure:

1. Run only the review lenses that match the triggers.
2. Prefer independent specialist/subagent review when available and useful; otherwise
   apply the review lenses manually.
3. Consolidate findings into a dated review report such as
   `docs/reviews/YYYY-MM-DD-spec-plan-review.md`.
4. Identify accepted findings, deferred findings, and scope changes requiring user approval.
5. Apply only accepted changes to Spec Kit artifacts as addenda or explicit updates.
6. Commit the review report and artifact updates separately from implementation code.
7. Proceed to task generation only after the revised plan remains approved.

Do not let reviewers change the approved product name, promise, MVP boundary, or core
UX direction without user approval.

## Local Verification During Implementation

If implementation includes a UI, run the product locally before asking the user to verify it.

Expected behavior:

- Start the local dev server or equivalent.
- Provide the localhost URL to the user.
- Test the main user sequence yourself before treating the feature as done.
- Test functionality behind visible UI elements, not only whether the page renders.
- For upload, form, generation, navigation, or save flows, verify that the visible result appears in the app.
- Do not commit final UI/application changes until the key flow has been locally checked or you clearly report why it could not be checked.

## Future Agent Orientation

After Spec Kit artifacts exist, make their locations clear in project status updates and handoffs.

Future agents should be told to read:

- the starter artifacts: `project-brief.md`, `prototype-pass.md`, and `build-brief.md`, especially Product Design Gate decisions inside `prototype-pass.md`
- the active Spec Kit `spec.md`
- the active Spec Kit `plan.md`
- the active Spec Kit `tasks.md`
- any spec, plan, or task addenda

This protocol stores the operating rules directly, so a separate repo-local `AGENTS.md` file is not required by default.

## Triggered Review Frameworks

Triggered tools may be used as challenge, discipline, and learning aids.

For gstack, Superpowers, Compound Engineering, and triggered tool reporting, follow `triggered-tools-protocol.md`.

Triggered tools must not change approved product scope without user approval.

Optional does not mean passive: if a trigger condition appears, use the tool, use the
review lens manually, or explain why it was skipped.

## Maintenance Rule

During implementation:

- If approved product behavior changes, add a dated spec addendum instead of silently rewriting the approval baseline.
- If new work appears, append tasks under `Added During Implementation`.
- If the technical approach changes materially, update or add a plan addendum.
- Keep product decisions traceable.
- For each meaningful feature or product decision, add a short note in `docs/solutions/` explaining what was used, why, what artifact resulted, and what decision changed.
- Commit documentation and process updates separately from application code when practical.

## Core Rule

Spec Kit structures execution. It must not override the Project Starter Kit artifacts unless the user explicitly approves a scope change.
