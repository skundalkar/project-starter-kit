# Project Starter Kit: Validation Gate

## Purpose

Use this gate before build handoff when the product's value, user behavior, safety, language, onboarding, trust, or retention assumptions are unproven.

## Trigger Conditions

- User asks to build, implement, create a repo, continue toward Spec Kit, or turn the idea into a real product.
- Product has a synthetic persona or scenario but no customer evidence.
- Product depends on user data entry, habit formation, sensitive data, AI trust, workflow change, repeated use, or behavior change.
- Review identifies missing validation, onboarding risk, retention risk, confusing labels, trust issues, or customer-value uncertainty.

## Required Output

Add a "Validation Plan" section to `prototype-pass.md` or `build-brief.md`:

- Target users:
- Riskiest assumption:
- Validation question:
- Test method:
- Script:
- Success threshold:
- Invalidation signal:
- What changes if validation fails:

Also add a risk-surface validation table to `build-brief.md`:

```text
Risk surface | Likely failure | Proof method | Fixture/scenario | Observable pass | False-positive success to prevent | Owner/stage
```

Use only applicable surfaces: behavioral semantics, temporal/order, data/source honesty, external boundary, auth/billing/permissions, retries/idempotency, UI interpretation/accessibility, safety/privacy, and deployment/delivery state.

## Minimum Validation Slice

For each MVP, define one validation slice:

```text
User:
Scenario:
Artifact shown:
Task:
Expected signal:
Pass threshold:
Fail threshold:
Decision changed if fail:
```

## Guidance

Prefer validating the riskiest product assumption before validating polish. For workflow or UI products, use a concrete artifact such as cards, a wireframe, a sample output, a fake-door flow, or a concierge walkthrough.

Use behavior-first, outside-to-inside BDD:

1. Start with a user-visible scenario, fixture, and outcome.
2. Define the product/service contracts needed to make that outcome true.
3. Add component and unit checks for the internal decisions behind those contracts.
4. Verify the operating layer itself when orchestration, sequencing, retries, uploads, integrations, or runtime boundaries are part of the product.

A component or manual-command success is not proof that the full operating flow works. Record false-positive success states that could make the build appear correct while the user-visible behavior is wrong.

Useful validation questions:

- Can the target user recognize the problem without a long explanation?
- Can they complete the first task with the proposed artifact?
- Does the output improve confidence, speed, quality, safety, creativity, or decision clarity?
- What setup burden makes the value not worth it?
- What words, labels, or claims feel confusing, judgmental, unsafe, or untrustworthy?
- What would make the user come back a second or third time?

## Generic Example

```text
User: target consumer in the first-use segment
Scenario: common daily situation where the current workaround is frustrating
Artifact shown: 3 recommendation cards from a synthetic data set
Task: choose one option and explain why
Pass threshold: 4 of 5 users can name the recommended option and one useful reason within 60 seconds
Fail threshold: users ignore the explanation, reject the setup burden, distrust the output, or want a different job solved
Decision changed if fail: simplify onboarding, narrow the first-use case, or reposition the MVP around the behavior users actually value
```
