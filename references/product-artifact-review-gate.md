# Project Starter Kit: Product Artifact Review Gate

## Purpose

Use this gate after a concrete product artifact exists and the user's reaction reveals new questions.

Artifacts include UI mocks, dashboards, charts, reports, generated documents, workflow screens, prototypes, sample outputs, and implemented pages.

The gate captures artifact-driven discovery: seeing output creates questions, those questions expose hidden assumptions, and those assumptions should update specs, tasks, docs, or the next prototype before more coding.

## Trigger Conditions

Run this gate when any of these appear:

- the user says the artifact is confusing, misleading, too much, not useful, or not what was discussed
- the user asks what a number, score, percentage, label, chart, or section means
- the user asks what action they should take after seeing the artifact
- the user notices counts do not reconcile
- the artifact claims more data/source coverage than it has
- a visual output creates new questions that were not obvious in abstract discussion
- a dashboard/report/monitor noun seems to be hiding a deeper product model

## Review Lenses

Apply only the lenses that match the trigger:

| Lens | Use When | Questions |
| --- | --- | --- |
| Product intent | The artifact may not answer the real job. | What is the user trying to infer? Does this artifact answer it? |
| UI interpretation | The screen may be visually misleading. | What would a first-time user infer in 10 seconds? |
| Metric semantics | Counts, scores, percentages, or baselines are unclear. | What is the denominator? What is the time window? Do numbers reconcile? |
| Data/source honesty | Source coverage is incomplete, sampled, filtered, or unknown. | What claims are unsupported by the available data? |
| Actionability | The user asks what to do next. | Should they observe, inspect, validate, escalate/review, or ignore as one-off? |
| Documentation capture | The discussion creates new logic. | What needs to become spec, tasks, manual, or schema examples? |

## Artifact Review Procedure

1. Name the artifact being reviewed.
2. Reconstruct the user's intended inference.
3. List what the artifact makes clear.
4. List what it makes confusing or misleading.
5. Reconcile all key numbers with visible denominators and time windows.
6. Check source-coverage language against actual source coverage.
7. Identify exposed assumptions.
8. Decide whether specialist sidecar review is needed using `async-orchestration-gate.md`.
9. Convert accepted findings into spec/tasks/docs before implementation changes.
10. State the next action clearly: continue design, update artifact, update spec/tasks, implement, or wait for user approval.

## Standards

An artifact passes review only when:

- a user can tell what is happening
- a user can tell why it matters
- the main object of attention is clear
- signal, evidence, explanation, and optional action are separated
- key numbers include denominators and units
- time windows are explicit
- source coverage is honest
- labels do not imply unsupported certainty
- the artifact exposes a clear next step or clearly states that it is informational only

## Privacy Rule

Case studies and reusable examples must be synthetic unless the user explicitly approves real project details.

Preserve reasoning structure, not factual identity. Replace project names, platform names, community names, user names, source paths, screenshots, URLs, and real records with neutral placeholders.

## Synthetic Case: Community Health Incident Monitor

Initial user noun: "dashboard."

Artifact review discovered that the real product was an incident review console. The user did not simply need charts; they needed to know which community was abnormal, whether it was sustained, which thread/comment/participant explained it, and what to inspect next.

Weak metric:

```text
Risk score: 54
```

Better metric:

```text
12 flagged interactions / 188 observed interactions,
above Community A's baseline for 35 minutes.
```

Weak evidence:

```text
Top thread: 100%
```

Better evidence:

```text
Primary thread cluster: 6 of 12 flagged interactions.
Comment Cluster B: 4 of those 6.
Participant 17: 2 flagged / 3 observed participant interactions.
```

Weak baseline:

```text
Use today's average.
```

Better baseline:

```text
Use a stable historical baseline with a holdout gap.
Use provisional cold-start baselines only with caveats.
Do not train the baseline on active incident windows.
```

## Output Format

Use a concise review report:

```text
Artifact reviewed:
User inference:
Clear:
Confusing:
Metric/source issues:
Assumptions exposed:
Recommended changes:
Spec/task/doc updates:
Next step:
```

If specialist reviews were used, include:

```text
Review lens:
Agent or reviewer:
Finding:
Accepted / deferred:
Artifact updated:
```
