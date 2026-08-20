# Build & Proof Trace

## Delivery Target

- Approved change:
- Source artifacts:
- Environment or delivery plane:

## Behavior And Risk Traceability

| Approved behavior or critical risk | Source | Implementation task | Acceptance scenario | Component/unit proof | Operating-layer proof | Evidence/status |
| --- | --- | --- | --- | --- | --- | --- |

## Outside-In Scenario Contract

| Behavior | Representative input/fixture | Full run or flow | Outside-observable outcome | Scenario test ID/path |
| --- | --- | --- | --- | --- |

## Scenario-Red Evidence Before Implementation

| Scenario | Red command | Expected missing-behavior failure | Observed failure excerpt | Fixture/environment valid | Valid red? | Implementation started only after valid scenario red |
| --- | --- | --- | --- | --- | --- | --- |

An already-green test is regression coverage, not valid scenario-red evidence. If the scenario cannot run or is red for the wrong reason, stop implementation and repair the test or environment.

## Mechanistic Red-Green Loop

| Sequence | Contract or internal decision | Focused test | Red command and observed reason | Valid red? | Smallest implementation slice | Green command and observed result | Scenario result after slice |
| --- | --- | --- | --- | --- | --- | --- | --- |

Continue mechanistic red/verified-red/green slices until the outside-in scenario is green.

## Final Scenario-Green Evidence

| Scenario | Green command | Observable result | Operating-layer boundary exercised | Broader regression result |
| --- | --- | --- | --- | --- |

## Proof Summary

- Focused checks:
- Broader checks:
- User-visible inspection:
- External/runtime proof:
- Scenario red before implementation:
- Final scenario green:
- Remaining unproved claims:
- Exact next action:
