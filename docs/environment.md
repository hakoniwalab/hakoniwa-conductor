# Supported environment

[日本語](environment-ja.md)

| Release | OS | CPU | Status |
| --- | --- | --- | --- |
| v1.1.0 | Ubuntu 24.04 | x86_64 | public ZIP target |
| v1.1.0 | macOS | arm64 | public ZIP target |
| v1.0.0 | Ubuntu 24.04 | x86_64 | initial public target |
| v1.0.0 | macOS | arm64 | public ZIP target |

The Linux archive is built in Docker with `linux/amd64`. Emulation on Apple Silicon is slower, but the artifact contract remains x86-64.

The ZIP contains Conductor-specific executables and public generators. Core, Endpoint, RPC, and Bridge shared libraries belong to the local Foundation managed by Business Pack. Manual installation into system `/usr` directories is not the supported workflow.

Ports, host names, and container routes depend on the Recipe. Use the host reachability contract declared by Business Pack instead of embedding OS-specific host IP addresses.
