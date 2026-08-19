# Project Starter Kit: Behavioral Delta Review

## Purpose

Use this review when a request changes an existing system. Show how the current system is likely to change before treating the requirement as understood.

A scope statement such as "process the full file" does not resolve unit of work, granularity, timing/order, state, controls, outputs, or completion/failure behavior.

## Required Review

Examine each applicable dimension:

| Dimension | Current behavior | Likely behavior after requested change | Intended behavior | Decision needed |
| --- | --- | --- | --- | --- |
| Scope | | | | |
| Unit of work | | | | |
| Granularity | | | | |
| Timing/order | | | | |
| State | | | | |
| Controls | | | | |
| Outputs | | | | |
| Completion/failure | | | | |

## Current-System Impact Preview

Before approval or implementation, show:

- behavior that remains unchanged
- behavior that changes automatically if the request is implemented literally
- hidden dimensions the request does not resolve
- likely regressions or misleading success states
- decisions required from the user

Update the behavioral contract only after these differences are explicit.

## Meeting-Copilot Example

Request: "Upload and process the full transcript as if the meeting were live."

- Scope: the full file.
- Unit of work: one timestamped segment, not the whole file.
- Granularity: bounded chronological segments.
- Timing/order: process sequentially without exposing future transcript text.
- State: carry forward meeting state after every segment.
- Controls: pause, resume, inspect, and retry a failed segment.
- Outputs: timestamped replay trace plus final synthesis.
- Completion/failure: prove coverage; report gaps or malformed segments instead of silently skipping them.

Full-file coverage may be correct while whole-file processing, timing, state, or cadence remains wrong. The current-system impact preview must expose that distinction before implementation.
