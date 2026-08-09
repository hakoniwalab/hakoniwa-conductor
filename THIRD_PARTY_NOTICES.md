# Third-party notices

Hakoniwa Conductor binaries use or require the components listed below. The exact Foundation revisions and operating-system package versions used for a release are recorded in `metadata/build-contract.txt` and `metadata/dpkg-versions.txt` inside the release archive.

## Hakoniwa Foundation runtime dependencies

The following projects are not duplicated in the Conductor ZIP. Hakoniwa Business Pack installs them into the local Foundation used at runtime.

| Component | Project | License |
| --- | --- | --- |
| Hakoniwa Core Pro | https://github.com/hakoniwalab/hakoniwa-core-pro | MIT |
| Hakoniwa PDU Endpoint | https://github.com/hakoniwalab/hakoniwa-pdu-endpoint | MIT |
| Hakoniwa PDU RPC | https://github.com/hakoniwalab/hakoniwa-pdu-rpc | MIT |
| Hakoniwa PDU Bridge Core | https://github.com/hakoniwalab/hakoniwa-pdu-bridge-core | MIT |

Each Foundation installation retains the license material supplied by its project. The dependency list above does not replace those license files.

## nlohmann/json

Project: https://github.com/nlohmann/json

License: MIT

```text
MIT License

Copyright (c) 2013-2022 Niels Lohmann

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Ubuntu runtime libraries

The Linux build also links to standard libraries supplied by Ubuntu 24.04. Their resolved package versions are recorded in `metadata/dpkg-versions.txt`; the corresponding Ubuntu packages retain their own copyright and license files under `/usr/share/doc/<package>/copyright` in the runtime environment.
