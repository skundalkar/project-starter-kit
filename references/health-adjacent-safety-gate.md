# Project Starter Kit: Health-Adjacent Safety Gate

## Purpose

Use this gate for products that touch health, wellness, symptoms, bodies, food, sleep, mood, accessibility, safety, legal, financial, or other high-trust domains where wording, recommendations, data handling, or certainty could create harm.

The gate helps keep a consumer product useful without making unsupported claims.

## Trigger Conditions

- Product uses health, wellness, body, symptom, safety, legal, financial, or accessibility context.
- Product stores sensitive personal data or user notes.
- Product recommends an action that could be mistaken for professional advice.
- Product copy includes words like diagnose, treat, prevent, safe, risk, severity, clinical, guaranteed, optimal, compliant, or approved.
- Product relies on AI, scores, classifications, or confidence labels in a high-trust domain.

## Claim Classification

Classify important claims before implementation:

| Claim | Classification | Allowed In MVP? | Safer Wording | Evidence Needed |
| --- | --- | --- | --- | --- |
|  | Preference support / education / professional advice / diagnosis / treatment / guarantee |  |  |  |

Use these classifications:

- Preference support: based on user-entered preferences or notes.
- General education: sourced, non-personal informational content.
- Professional advice: requires expert review or regulated workflow.
- Diagnosis or treatment: out of scope unless explicitly designed and reviewed for that domain.
- Guarantee: avoid unless legally and evidentially supported.

## Data And Privacy Checks

Record:

- sensitive data collected
- why each sensitive field is needed
- local vs cloud storage
- deletion/reset behavior
- export behavior, if any
- source/evidence visibility
- uncertainty language
- forbidden claims or labels

## Required Output

Add a "Safety, Claims, And Privacy" section to `project-brief.md` or `build-brief.md`:

```text
Sensitive context:
Allowed claim types:
Forbidden claim types:
Safer wording rules:
Data minimization:
Deletion/reset requirements:
Uncertainty language:
Review required before launch:
```

## Pass Criteria

The gate passes when:

- unsupported high-trust claims are removed or rewritten
- sensitive data is minimized and controllable
- user-facing copy separates preference support from professional advice
- uncertainty is visible where recommendations may be wrong
- review requirements are recorded before production or public launch
