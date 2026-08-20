# Risk-Surface Validation

Choose proof based on how the approved behavior can fail. Use only applicable rows.

| Risk surface | Typical failure | Useful proof |
| --- | --- | --- |
| Behavioral semantics | A control or term does the wrong thing | Given/When/Then acceptance scenario with state assertions |
| Timing and order | Future data leaks in; steps run out of order | Timestamped fixture, replay trace, ordering assertions |
| State and persistence | Retry duplicates work; reload loses progress | Idempotency, resume, crash-window, and persistence tests |
| Data and source honesty | Output exceeds coverage or provenance | Reconciliation, denominator, provenance, and as-of checks |
| External boundary | Mock passes but real integration fails | Staging/sandbox call with safe evidence and failure-path test |
| Auth, billing, permissions | Capability works only in another surface | Real runtime preflight and denied/expired-path test |
| UI interpretation | Page renders but action or meaning is wrong | Browser flow, accessibility check, screenshot/visual review |
| Safety and privacy | Sensitive data or unsafe certainty leaks | Policy fixtures, redaction, deletion, confidence-language checks |
| Delivery state | Local work is mistaken for live behavior | Commit, remote, CI, deployment, health, and user-verification checks |

## Mandatory Red-Green Invariant

For every new or changed observable behavior:

```text
representative outside-in scenario
-> red for the intended missing behavior
-> verify the red failure message and environment
-> mechanistic red / verified-red / green slices
-> outside-in scenario green
-> broader regression and operating-layer proof
```

Do not write or change production implementation code before valid scenario-red evidence exists. Do not implement a mechanistic slice before its focused test is red for the intended reason. Treat an already-green new test as regression coverage, not as evidence that the test detects the change.

If the representative scenario cannot execute, mark implementation blocked. Do not replace the outside boundary with isolated unit tests merely to obtain green.

## Intended-Red Check

Before implementation, inspect the failing scenario:

- Confirm it traces a full run or operating flow from representative input to an outside-observable outcome.
- Confirm it reaches the behavior under test.
- Confirm the fixture and environment are valid.
- Confirm the assertion describes the approved outcome.
- Confirm the failure message points to missing or wrong behavior.
- Reject failures caused only by setup, syntax, dependency, permissions, or unavailable services.
- Record the command and concise failure excerpt before changing production implementation code.

## False-Green Check

Ask what could still be broken if this proof passes. Add operating-layer evidence when an isolated component can pass while the actual workflow fails.
