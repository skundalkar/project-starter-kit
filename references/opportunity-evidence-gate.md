# Project Starter Kit: Opportunity & Evidence Gate

## Contents

- Purpose and lead-agent stance
- Gate sequence
- Gate outcomes and artifact recording
- Research sample versus build fixture
- Handoff to Product Design
- Illustrative ATS matching example
- Pass criteria

## Purpose

Run this gate after the user's opening idea and before product strategy, Product Design, workflow definition, requirements, or specification.

Treat a one-sentence idea as a hypothesis about user value and feasibility, never as enough input to begin requirements or build work. Use evidence to identify credible directions before design effort hardens the wrong product.

## Lead-Agent Stance

Act as an evidence-led product guide, not a passive requirements scribe.

- Surface the assumptions hidden inside the idea.
- Test the assumptions that could change whether the product should exist or how it should operate.
- Explain the consequence if each material assumption is wrong.
- Recommend a direction based on the evidence available.
- Invite explicit user decisions at reversible direction points.
- Never make an irreversible user-value, trust, or product-direction judgment silently.

Ask one or two sharp questions at a time when user context is needed, but continue safe public research in parallel when it will inform the decision.

## Gate Sequence

### 1. Frame The Hypothesis

Capture:

- the user's one-sentence idea
- intended user and trigger situation, if known
- the outcome the user appears to want
- the proposed product noun or mechanism
- assumptions about value, data, access, trust, workflow, and willingness to change behavior
- which assumptions would invalidate or materially reshape the idea

Do not translate the noun into features or requirements yet.

### 2. Inventory Evidence Sources

Identify all four source classes even when a class is empty:

1. public
2. paid or licensed
3. internal or user-provided
4. missing or not yet obtainable

For each material source, record:

| Source | Class | Access | License/permission | Cost | Provenance | Freshness | Coverage | Structural shape | Quality/uncertainty | Privacy/trust limits |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Structural shape must name the useful entities, fields, relationships, identifiers, granularity, and formats rather than merely saying that "data exists."

Do not treat discoverability as permission. Separate technical access from contractual, licensing, privacy, and user-trust authority.

### 3. Inspect Comparables Only For Directional Decisions

Inspect comparable products, services, or operating models only when their behavior could change a credible product direction.

Prefer current public sources, including official product pages, public documentation, app-store material, credible case studies, and mature adjacent workflows. Treat marketing claims as positioning evidence, not proof of traction or effectiveness.

Compare operating choices such as:

- who initiates the workflow
- whether the product searches, ranks, alerts, explains, routes, or executes
- where human judgment enters
- what evidence is visible
- what trust, onboarding, or permission burden exists
- what the product makes easy, heavy, risky, or misleading

Record only the patterns that changed, ruled out, or confirmed a direction. Do not run a separate later competitor feature survey.

### 4. Obtain A Small Research Sample When Appropriate

When feasibility depends on data shape or quality, obtain and profile a small representative sample that is legal, permitted, proportionate, and traceable.

Record:

- source and retrieval date
- access and use terms
- sampling method and size
- entities, fields, relationships, identifiers, granularity, and formats observed
- freshness, coverage, missingness, noise, bias, and uncertainty
- privacy or trust constraints
- what the sample supports
- what it does not support

Do not download a huge dataset, purchase paid data, request broad production access, or ingest unnecessary personal data merely to explore feasibility. If no sample is appropriate, explain why and identify the smallest targeted spike that could resolve the question.

### 5. Return 2-3 Credible Options

Base options on the researched evidence, not generic brainstorming.

For each option, record:

| Option | Operating model | Evidence basis | Benefits | Constraints | Material assumptions | First wedge | Decision needed |
| --- | --- | --- | --- | --- | --- | --- | --- |

Then state:

- recommended option and why
- consequence of choosing it
- strongest alternative and when it would be better
- evidence gap that could reverse the recommendation
- explicit user decision needed

Keep the number of options to 2-3. If only one direction is credible, show the rejected directions and the evidence that ruled them out.

## Gate Outcomes

End with exactly one primary outcome:

1. **Proceed with chosen direction** — record the selected operating model, evidence basis, first wedge, constraints, and user approval.
2. **Targeted research spike** — name the unresolved decision, evidence needed, bounded method, cost or access limit, owner, and stop condition.
3. **Narrow or reframe** — state which user, situation, outcome, data dependency, or product claim changed and why.
4. **Stop or defer** — record the blocking evidence, conditions for reconsideration, and any irreversible spend or access action avoided.

Do not silently convert an ambiguous outcome into product strategy.

## Artifact Recording

Keep the three starter artifacts as the only product sources of truth.

- Record the opportunity hypothesis, source inventory summary, evidence limits, option decision, and selected wedge in `project-brief.md`.
- Record sample details, focused evidence gaps, design-consumption notes, and evidence-driven prototype changes in `prototype-pass.md`.
- Carry approved source constraints, data boundaries, stable fixture needs, and unresolved spikes into `build-brief.md`.
- Record the gate decision and supporting evidence in the existing Decision Ledger. Do not create a separate research report or gate ledger by default.

Link to large supporting materials when needed; do not duplicate their contents across artifacts.

## Research Sample Versus Build Fixture

Keep these roles explicit:

| Research sample | Build fixture |
| --- | --- |
| Tests whether the opportunity is feasible or which direction is credible | Supports mocks, operating walkthroughs, acceptance scenarios, tests, and validation |
| May be messy, incomplete, time-bound, or licensed only for evaluation | Must be stable, minimal, reproducible, and preferably anonymized or synthetic |
| Carries source, access terms, retrieval date, sampling limits, and supported/unsupported claims | Carries version, schema, expected outcomes, edge states, privacy treatment, and provenance as real or explicitly mocked |
| Must not silently become production or test data | Must not imply real-world coverage when it is mocked or synthetic |

Promote data from a research sample into a build fixture only when permission, privacy treatment, stability, and representativeness are explicit.

## Handoff To Product Design

Pass the approved direction, first wedge, evidence basis, source constraints, sample limits, and open focused gaps to `product-design-gate.md`.

Product Design must turn that direction into visual or structural concepts, an interaction and operating flow, behavioral-contract implications, and a concrete prototype pass. It may reopen research only when a specific design or prototype observation exposes a new evidence gap. A reopened spike must name the decision it will resolve and update the existing gate record and Decision Ledger.

## Illustrative ATS Matching Example

This is a worked framing example, not researched evidence and not a direction to build an ATS.

**Opening hypothesis:** "Help recruiters match candidates to companies." Do not turn this sentence into ATS screens or matching requirements.

**Assumptions to challenge:** recruiters need company-level matching rather than role-level search; enough lawful candidate and company evidence exists; a score would improve decisions rather than create false certainty; recruiters can explain and override recommendations.

**Source inventory:**

- Public: company career pages, public company descriptions, occupational taxonomies, and public role descriptions. Likely entities include company, role, skill, location, seniority, and posted date; coverage and freshness vary.
- Paid/licensed: firmographic, labor-market, compensation, or job-feed data. Access may be contract- and purpose-limited; cost and redistribution rights must be confirmed before purchase.
- Internal: permissioned ATS candidate profiles, recruiter dispositions, role briefs, CRM company records, and outcome history. Likely entities include candidate, company, role, application, interaction, disposition, and timestamp; personal data, retention, bias, and provenance limits are material.
- Missing: verified skills, consistent rejection reasons, true candidate preferences, normalized company attributes, and evidence that past placements predict future fit without reinforcing historical bias.

**Small research sample:** profile a permissioned, traceable slice such as 20-50 de-identified candidate-role-company cases plus a small set of public role/company records. Record access terms, retrieval date, fields, missingness, label reliability, and bias. It may support a data-shape or workflow feasibility decision; it does not establish matching accuracy, fairness, or production coverage.

**Comparable operating-model question:** inspect patterns such as recruiter-led Boolean search, system-ranked recommendations, reusable talent pools, batch shortlist review, and evidence-first review only to learn which direction is credible. Record what each pattern changes about initiation, judgment, evidence visibility, permissions, and trust; do not copy its feature list.

**Credible operating-model options:**

1. Rules-and-filters shortlist: explainable and controllable, but depends on normalized fields and may miss non-obvious fit.
2. Weighted evidence ranking: surfaces ranked candidate-company-role pairs with reason codes, but needs defensible weights, uncertainty language, and bias review.
3. Recruiter evidence assistant: retrieves and summarizes supporting evidence without a single fit score; slower to scan, but preserves judgment when outcome labels are weak.

**Agent recommendation:** start with the recruiter evidence assistant when labels and preferences are incomplete, using a narrow role/company wedge and explicit evidence/override controls. Explain that jumping to a fit score would manufacture certainty from weak labels. Ask the user to choose this wedge, authorize a bounded spike on ranking evidence, narrow the audience, or defer.

**Fixture distinction:** the research slice decides whether a direction is credible. A later build fixture should be a stable, preferably synthetic or anonymized set of candidate/company/role records with expected evidence links, ranking or retrieval outcomes, edge cases, and must-not-happen bias/privacy cases.

## Pass Criteria

Pass only when:

- the idea remains framed as a tested hypothesis rather than premature requirements
- all four source classes were considered
- material sources have access, permission, cost, provenance, freshness, coverage, shape, quality, and privacy/trust limits recorded
- a small traceable research sample was profiled when it would materially reduce uncertainty, or the reason not to was recorded
- comparable operating models were inspected only to inform credible directions
- 2-3 evidence-grounded options and a recommendation were presented
- the user approved the direction or explicitly chose another gate outcome
- the evidence and decision are recorded in the existing starter artifacts and Decision Ledger
- research samples and later build fixtures are not conflated
