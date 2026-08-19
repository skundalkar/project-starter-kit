# Executable Handoff Protocol

## Boundary Checklist

Before handing off:

1. Confirm the current source of truth and read order.
2. Reconcile working tree, commit, remote, CI, deployment, and user-verification state.
3. Separate approved facts from assumptions and proposals.
4. Name incomplete work, failed checks, and unproved claims.
5. Resolve the next owner, first action, and stop/escalation condition.
6. Remove stale paths, commands, links, or status.

## Handoff Quality Test

The handoff is executable when the next owner can answer without prior chat history:

- What outcome are we pursuing?
- What is approved and must not drift?
- What files or artifacts should I read, and in what order?
- What has actually been completed and proven?
- What delivery plane is current?
- What is the first safe action?
- When must I stop or ask for authority?

## Contradictions

When sources disagree:

- quote or summarize both claims
- identify their dates/status/owners
- apply the explicit source-of-truth rule when one exists
- otherwise mark the conflict unresolved
- do not silently merge incompatible behavior
