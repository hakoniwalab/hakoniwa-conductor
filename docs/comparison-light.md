# Comparison with Conductor Light

[日本語](comparison-light-ja.md)

Conductor Light implements a subset of the execution-responsibility semantics of Hakoniwa Conductor. It is not merely a lower edition. It has a different emphasis: dynamic Asset participation and flexible integration with external systems such as Web and ROS.

## Execution responsibility and simulation semantics

| Capability or concept | Conductor Light | Hakoniwa Conductor | Notes |
| --- | :---: | :---: | --- |
| Distributed time synchronization | Supported | Supported | See hakoniwa-design-docs for bounded-drift semantics |
| Time-difference diagnostic logs | Under review | Supported | Log output is not visualization |
| Time-difference visualization | Not supported | Not supported | Means a UI, graph, or dashboard |
| Dynamic Asset join and leave | Supported | Out of scope or constrained | The public Conductor contract will be finalized before release |
| Simulation start, stop, and reset | Supported | Supported | Operation APIs and state contracts differ |
| EU Owner management | Out of scope | Supported | Owner follows the design-docs definition |
| Epoch management | Out of scope | Supported | Epoch follows the design-docs definition |
| Commit Point | Out of scope | Supported | Not a physical start synchronization point |
| Runtime Delegation | Out of scope | Supported | Safely switches execution responsibility |

Items marked Under review or Out of scope or constrained will be finalized against both implementations and their tests before publication.

## Product purpose and integration

| Viewpoint | Conductor Light | Hakoniwa Conductor |
| --- | --- | --- |
| Primary purpose | Lightweight execution control and external integration | Execution-responsibility and causal-boundary management |
| Configuration model | Emphasizes dynamic and flexible connections | Managed configuration based on EU, Owner, and Epoch |
| Web integration | Focus area; published status distinguishes implemented from planned | Management integration through Remote API and related boundaries |
| ROS integration | Focus area; published status distinguishes implemented from planned | Primarily manages Hakoniwa-side execution responsibility |
| Suitable use | UI, ROS, prototyping, lightweight integration | Distributed execution, responsibility delegation, causality management |

Choose Conductor Light when dynamic participation and flexible Web or ROS integration are the priority and Owner, Epoch, Commit Point, and RD semantics are unnecessary. Choose Hakoniwa Conductor when those execution-responsibility semantics are required.
