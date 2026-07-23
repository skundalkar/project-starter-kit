# Project Starter Kit: Framework Validation Notes

These notes validate the clean framework against two prior product-discovery examples without copying those examples into the kit.

## Validation Source A: Reorient

What the framework needed to support:

- a product born from a concrete high-stakes personal situation
- emotional state and practical action at the same time
- a product that is not merely chat, but produces named artifacts
- a situation that evolves over multiple interactions
- AI behavior, voice, trust, and guardrails
- MVP versus full product separation
- specialist review and acceptance criteria for a build agent

Coverage check:

- Product Meaning: covered by name, tagline, thesis, promise.
- User And Situation: covered by anchor situation, stakes, constraints, current workaround.
- Current State and Desired State: covered by transformation before and after.
- Core Method: covered by guided questioning, analysis, scripts, options, practice.
- Core Loop: covered by user describes situation, product clarifies, user reviews outputs, saves playbook.
- Product Artifacts: covered and strengthened by requiring named outputs.
- Experience Flow: covered by modes and journey.
- UI Direction: covered by interface shape and guided experience.
- Intelligence And Data: covered by entities, saved scenarios, structured outputs, AI behavior.
- Trust And Control: covered by review, evidence, approvals, uncertainty, safety boundaries.
- MVP Boundary: covered.
- Feasibility Challenge: adds a missing explicit pre-build stress test.
- Build Handoff: covered.

Finding:

The framework covers Reorient and improves the original process by making feasibility and user control explicit.

## Validation Source B: Living Space Studio

What the framework needed to support:

- a visual/spatial product rather than a conversational product
- camera/photo input and object detection assumptions
- visual approval problems caused by long markdown documents
- direct manipulation and UI behavior
- generated images as product value, not decorative output
- inventory, reusable objects, and persistent data
- platform constraints and feasibility issues discovered during implementation
- evolving MVP boundary after visual testing

Coverage check:

- Product Meaning: covered by name, category, thesis, naming checkpoint.
- User And Situation: covered by first room/space refresh use case.
- Current State and Desired State: covered by unable to visualize better layouts versus decision-ready refresh concepts.
- Core Method: covered by scan/upload, detect, review, generate, compare, choose.
- Core Loop: covered by user provides image, product returns concepts, user removes/edits objects, product updates recommendations.
- Product Artifacts: covered by room map, object outlines, inventory, design concepts, final plan.
- Experience Flow: covered by upload, review, concepts, inventory, final selection.
- UI Direction: needs explicit visual workflow/prototype guidance, now added.
- Intelligence And Data: covered by object detection, image generation, inventory, uncertainty, fallbacks.
- Trust And Control: covered by review/edit/remove boxes, approval, confidence, correction.
- MVP Boundary: covered, but the process needed stronger challenge before code.
- Feasibility Challenge: necessary and now explicit.
- Build Handoff: covered.

Finding:

The framework covers Living Space Studio only if UI Direction and Feasibility Challenge are first-class layers. Those layers should remain in the core map.

## Readiness Checklist Validation

The readiness checklist should be shorter than the framework map because it is user-facing.

Required items were validated against both examples:

- Working name or placeholder: needed in both.
- Category: needed to prevent scope drift.
- Primary user: needed in both.
- Anchor situation: essential in both.
- Current and desired state: essential in both.
- Product promise: essential in both.
- MVP loop: essential in both.
- Primary artifacts: essential in both.
- Explicit non-goals: essential in both.

Strongly recommended items were validated against both examples:

- First journey or screen sequence: important for build agents.
- Data entities: important for implementation.
- Trust and control: important for AI and user confidence.
- Feasibility risks: important before code.
- Visual artifacts: especially important for visual/spatial or complex workflow products.

Adjustment made:

- Added visual or workflow artifacts to readiness because long text-only approval created friction.
- Added feasibility risks before formal artifact generation because implementation discovered major assumption changes late.
