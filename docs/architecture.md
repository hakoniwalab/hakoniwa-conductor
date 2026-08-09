# Hakoniwa Conductor Architecture

[日本語](architecture-ja.md)

## User-visible structure

```text
Remote API / operation policy
             |
             v
          Conductor
             |
             | Owner / Epoch / Commit Point
             v
       RD control components
             |
             v
Bridge / Endpoint ---------------- Hakoniwa Assets
      Control Plane boundary          Data Plane
```

- **Conductor** manages EU execution-responsibility transitions and establishes Epoch and Commit Point semantics.
- **RD components** realize the responsibility transition between distributed execution entities.
- **Remote API** is the external operation and integration boundary for the Control Plane.
- **Bridge and Endpoint** connect Control Plane decisions to Data Plane delivery and lifetime semantics.
- **Hakoniwa Assets** execute simulation logic and contain one or more EU instances.

## Configuration generation

Users describe EUs, placement, connections, PDUs, and Conductor defaults in a user-facing configuration. Generators produce the detailed runtime inputs for each component.

```text
user configuration
        |
        | validate / generate
        v
execution-unit definition
        |
        +-- Conductor configuration
        +-- Bridge configuration
        +-- Endpoint configuration
        +-- RPC / Remote API configuration
        `-- RD control configuration
```

Generated files are runtime inputs and should not normally be edited directly. The user configuration and generator versions are matched to the binary release.

Environment setup and execution use the Hakoniwa Business Pack. A local Foundation provides shared dependencies, while a Recipe defines requirements, generation, startup, validation, and graceful termination.
