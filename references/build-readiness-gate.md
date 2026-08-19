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
- The approved behavioral contract is present and unresolved behavioral deltas are explicit.
- The operating flow and execution-boundary map identify real, mocked, manual, and deferred behavior.
- Every critical risk surface has a fixture/scenario, observable pass condition, and false-positive success state to prevent.
- Acceptance scenarios are behavior-first and outside-to-inside: user-visible behavior first, then service/component contracts, then internal unit coverage.
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

Before declaring readiness, confirm that each approved behavior and critical risk can map to a Spec Kit task and verification task. Do not accept a plan that tests only internal components when the required behavior depends on an operating layer or external boundary.
