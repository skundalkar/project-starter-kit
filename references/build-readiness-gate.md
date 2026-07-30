# Project Starter Kit: Build Readiness Gate

## Purpose

Prevent ambiguous handoffs where artifacts are detailed but not actually ready for implementation.

## Trigger Conditions

- Starter artifacts exist and user asks to build, implement, create a repo, start Spec Kit, or continue.
- Review identifies missing test fixtures, unresolved approval, unclear repo status, unclear ranking rules, privacy/safety gaps, or unvalidated customer assumptions.
- The build brief contains draft language that could be mistaken for user approval.

## Required Status

Set one or more:

- Ready
- Needs User Approval
- Needs Repo Gate
- Needs Validation
- Needs Business/Acquisition Check
- Needs Spec Kit
- Not Buildable Yet

## Required Checks

- Product name and promise are stable.
- MVP boundary is explicit.
- Prototype pass is complete or explicitly skipped.
- Validation plan exists or is intentionally deferred.
- Business/acquisition hypotheses exist for consumer or commercial products.
- Acceptance criteria include at least one fixture and expected output.
- Edge states are listed.
- Privacy and safety requirements are explicit when sensitive data exists.
- Repo status is known.
- External-state actions, such as creating a GitHub repo, have explicit user approval.

## Output Format

```text
Build readiness:
- Status:
- Blocking issues:
- Deferred issues:
- Required next action:
- Who must approve:
```

## Handoff Rule

Do not stop with only "not build ready." State what must happen next:

- ask for approval
- initialize local Git
- create or confirm a private GitHub repo
- run validation
- update starter artifacts
- start Spec Kit handoff
- begin implementation after approvals

If implementation is approved but GitHub is deferred, record the deferral and repeat the risk before milestone completion.
