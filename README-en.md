# Hakoniwa Conductor

[日本語](README.md)

Hakoniwa Conductor is the Hakoniwa Control Plane implementation for managing execution responsibility and causal boundaries in distributed simulation.

The public edition provides binaries, configuration generators, and user documentation for academic research, education, non-commercial research and development, peer review, and reproducibility studies. Configuration examples, sample applications, and the Hakoniwa Business Pack Recipe will be published incrementally. The Conductor and Runtime Delegation (RD) implementation source code is not published.

The smallest runnable example is the [Python time-synchronization sample](samples/python-time-sync/README.md), which coordinates two Python Hakoniwa assets. Its generated configuration is checked in, so the first smoke test does not require running a generator.

## Entry point

Environment setup, Foundation dependencies, Recipes, execution, and validation are managed through the [Hakoniwa Business Pack](https://github.com/hakoniwalab/hakoniwa-business-pack).

```text
Hakoniwa Business Pack
        |
        | Foundation / Recipe
        v
Hakoniwa Conductor binaries and generators
        |
        | generated runtime configuration
        v
Distributed Hakoniwa assets
```

Start with [Getting started](docs/getting-started.md). The [documentation index](docs/index.md) shows the complete public document set.

The first binary release is `v1.0.0`. Its artifacts are `hakoniwa-conductor-v1.0.0-linux-x86_64.zip` and `hakoniwa-conductor-v1.0.0-macos-arm64.zip`. See [Binary package](docs/binary-package.md) for package contents and placement.

## Shortest supported path

1. Check the [supported environment](docs/environment.md).
2. Prepare the Conductor Foundation through Hakoniwa Business Pack.
3. Download the ZIP and SHA-256 file for your OS and CPU from Releases.
4. Verify and extract it as described in [Binary package](docs/binary-package.md).
5. When the corresponding Business Pack Recipe is available, run its doctor, configuration generation, and smoke test operations.
6. Use the Recipe's stop operation and verify that processes and ports are released.

This repository does not duplicate build commands for individual Foundation components. Business Pack owns dependency construction and reuse decisions.

## Publication boundary

Published:

- Usage of the Conductor and RD binaries
- User-facing configuration schemas and examples
- Detailed-configuration generator binaries
- Reviewed configuration examples and sample applications as they become available
- Environment, operation, and validation instructions for macOS and Ubuntu
- Functional and product-positioning comparison with Conductor Light

Not published:

- Conductor implementation source code
- RD implementation source code or internal algorithms
- Implementation details of commercial features

## Design authority

[hakoniwa-design-docs](https://github.com/hakoniwalab/hakoniwa-design-docs) is the design source of truth for implementation-independent concepts and semantics such as EU, Owner, Epoch, Commit Point, Runtime Delegation, and bounded drift.

This repository documents which parts Hakoniwa Conductor implements and how users configure, execute, and validate them.

## Relationship to Conductor Light

Conductor Light implements a subset of the execution-responsibility semantics while emphasizing dynamic Asset participation and flexible integration with systems such as Web and ROS.

The products are not described as a simple higher/lower edition hierarchy. Choose Hakoniwa Conductor when Owner, Epoch, Commit Point, and RD semantics are required. Choose Conductor Light when lightweight execution control and flexible external integration are the priority. See [Comparison with Conductor Light](docs/comparison-light.md).

## License

This repository uses a dual-license model according to the intended use.

- Free non-commercial use: [Japanese](LICENSE-NC-ja.md) / [English](LICENSE-NC.md)
- Commercial use: a separate agreement with Hakoniwa Lab LLC is required. See the [Hakoniwa Conductor PRO commercial license](LICENSE-PRO-ja.md).

Files and third-party components carrying their own license notices remain subject to those terms.
