# Configuration and generator

[日本語](configuration-ja.md)

Conductor separates user input from generated runtime configuration.

```text
user-facing EU configuration
        |
        | validate / resolve
        v
Conductor generator
        |
        +-- execution-unit.json
        +-- Bridge and Endpoint configuration
        +-- Conductor Server and Client configuration
        `-- RD and Runtime Context configuration (RD mode only)
```

Users specify node topology, EU placement, timing, and transfer policy intent. Endpoint IDs, connection direction, and detailed Control Plane files are generated when they follow mechanically from the topology.

The public input contract is [`schemas/eu-input-v1.schema.json`](../schemas/eu-input-v1.schema.json).
A Recipe may declare that regeneration requires a private product while
committing the schema-valid input and generated artifacts for inspection and
execution.

Business Pack writes generated files under `work/recipes/<recipe-id>/config/`. Generated files are not edited directly. Relative paths resolve against the output directory rather than an implicit current working directory. See [Compatibility](compatibility.md) for binary and generator matching.
