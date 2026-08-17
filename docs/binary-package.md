# Binary package

[日本語](binary-package-ja.md)

## v1.1.0 filenames

Download the ZIP and checksum matching the target operating system and CPU.

```text
hakoniwa-conductor-v1.1.0-linux-x86_64.zip
hakoniwa-conductor-v1.1.0-linux-x86_64.zip.sha256
hakoniwa-conductor-v1.1.0-macos-arm64.zip
hakoniwa-conductor-v1.1.0-macos-arm64.zip.sha256
```

## Verification and extraction

Linux:

```bash
sha256sum -c hakoniwa-conductor-v1.1.0-linux-x86_64.zip.sha256
unzip hakoniwa-conductor-v1.1.0-linux-x86_64.zip
```

macOS:

```bash
shasum -a 256 -c hakoniwa-conductor-v1.1.0-macos-arm64.zip.sha256
unzip hakoniwa-conductor-v1.1.0-macos-arm64.zip
```

The extracted top-level directory has the same name as the ZIP without its extension. Check `VERSION` and `metadata/build-contract.txt` against the Hakoniwa Business Pack Foundation you intend to use.

## Contents

v1.1.0 contains:

- `bin/`: Conductor binaries, the RD sample executable, and configuration generators;
- `docs/`: public user documentation;
- `metadata/`: platform, actual Foundation revisions used by the build, package inventory, and dependency inspection results;
- README, VERSION, licenses, and third-party notices.

Foundation shared libraries, user configuration, and generated runtime configuration are not bundled. Use the binaries with the compatible local Foundation managed by Hakoniwa Business Pack.

## Sample execution boundary

Extracting the ZIP alone is not sufficient to start a sample topology. Conductor requires configuration for its processes, Endpoints, RPC, PDUs, and execution ownership.

The corresponding Hakoniwa Business Pack Conductor Recipe is the source of truth for sample execution commands. It defines, as one contract:

- ZIP placement;
- required Foundation contract;
- user configuration and generation;
- startup order and success evidence;
- graceful shutdown and cleanup verification.

The v1.1.0 ZIP names above are fixed. If a Recipe expects another name, correct the Recipe instead of renaming the ZIP.
