# Compatibility

[日本語](compatibility-ja.md)

The v1.1.0 and v1.0.0 contracts provide Ubuntu 24.04 x86-64 and macOS arm64 ZIPs combined with the Foundation revisions and Python PDU version recorded in `metadata/build-contract.txt`, prepared through the corresponding Hakoniwa Business Pack Recipe.

Compatibility is identified by `VERSION` together with the build contract, not by the tag name alone. Business Pack rebuilds only missing or incompatible Foundation components.

An incompatible Foundation ABI, configuration schema, or generator output change requires migration notes. Untested combinations are not described as supported.
