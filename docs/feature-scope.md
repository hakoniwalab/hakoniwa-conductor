# Hakoniwa Conductor Feature Scope

[日本語](feature-scope-ja.md)

Normative definitions are maintained by `hakoniwa-design-docs`. This page states the product implementation scope.

| Capability | Status | Notes |
| --- | --- | --- |
| Distributed time synchronization | Supported | Handles bounded drift under the stated design conditions |
| Simulation start, stop, and reset | Supported | Operated through a Business Pack Recipe |
| EU Owner management | Supported | Maintains uniqueness of execution responsibility |
| Epoch management | Supported | Identifies generations of execution responsibility |
| Commit Point | Supported | Semantic fixation of responsibility and causal boundaries |
| Runtime Delegation | Supported | Switches the Owner of an EU during execution |
| Time-difference diagnostic logs | Supported | Diagnostic logs are not a visualization feature |
| Time-difference visualization | Not supported | No UI, graph, or dashboard is provided |

Status values distinguish Supported, Experimental, Planned, Out of scope, and Not supported. Log output alone is never described as time-difference visualization.
