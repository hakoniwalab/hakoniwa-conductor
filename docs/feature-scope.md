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
| Time-synchronization error measurement and data output | Not supported | No numeric data contract is provided for evaluating the difference between reference and observed time |

Status values distinguish Supported, Experimental, Planned, Out of scope, and Not supported. Data output means a numeric data contract that allows synchronization error to be evaluated. The current version provides neither this data output nor UI or graph visualization.
