# 互換性

[English](compatibility.md)

| 項目 | v1.1.0契約 | v1.0.0契約 |
| --- | --- | --- |
| Conductor | v1.1.0 Linux x86_64 / macOS arm64 ZIP | v1.0.0 Linux x86_64 / macOS arm64 ZIP |
| OS | Ubuntu 24.04 / macOS arm64 | Ubuntu 24.04 / macOS arm64 |
| Foundation | ZIP内`metadata/build-contract.txt`に記録されたrevision | 同左 |
| Python PDU | 同ファイルに記録されたversion | 同左 |
| 環境構築 | Hakoniwa Business Packの対応Recipe | 同左 |

Releaseの正は、タグ名だけでなくZIP内の`VERSION`と`metadata/build-contract.txt`の組です。Business PackはReceiptと要求条件を比較し、不足または不整合があるFoundation componentだけを再構築します。

Foundation ABI、設定スキーマ、Generator出力のいずれかに非互換変更がある場合、Release Notesへ移行手順を記載します。未検証の組合せを「対応」とは表記しません。
