# Getting started

[日本語](getting-started-ja.md)

The supported entry point for Hakoniwa Conductor users is Hakoniwa Business Pack. This is not a guide for cloning, building, and installing every dependency repository directly.

You need a host satisfying the [environment contract](environment.md), Hakoniwa Business Pack, a Conductor Release ZIP for the target platform, its SHA-256 checksum, and acceptance of the applicable license.

```text
Business Pack doctor
        |
        v
resolve the local Foundation
        |
        v
place the ZIP in the Recipe work area
        |
        v
validate and generate configuration
        |
        v
start, observe success, and terminate through the Recipe
```

For v1.0.0, select either `hakoniwa-conductor-v1.0.0-linux-x86_64.zip` or `hakoniwa-conductor-v1.0.0-macos-arm64.zip`, together with its `.sha256` file. Follow [Binary package](binary-package.md) to verify and extract it. Inspect `VERSION` and `metadata/` for dependency revisions and package contents.

> At the v1.0.0 publication point, the Conductor Recipe and public sample configuration are follow-up deliverables. Extracting the ZIP alone does not generate a runnable topology.

A running process alone is not success. Check the Recipe's connection, synchronization, or Runtime Delegation evidence, then verify process and port cleanup.
