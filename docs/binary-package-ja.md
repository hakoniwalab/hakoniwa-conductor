# バイナリパッケージ

[English](binary-package.md)

## v1.1.0のファイル名

対象OSとCPUに一致するZIPとチェックサムを取得します。

```text
hakoniwa-conductor-v1.1.0-linux-x86_64.zip
hakoniwa-conductor-v1.1.0-linux-x86_64.zip.sha256
hakoniwa-conductor-v1.1.0-macos-arm64.zip
hakoniwa-conductor-v1.1.0-macos-arm64.zip.sha256
```

## 確認と展開

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

展開後のトップディレクトリ名は、ZIPの拡張子を除いた名前と同じです。`VERSION`と`metadata/build-contract.txt`を確認し、利用するHakoniwa Business Pack Foundationとの互換性を確認してください。

## 収録物

v1.1.0は次を収録します。

- `bin/`: Conductor、RDサンプル実行バイナリ、設定Generator
- `docs/`: 公開利用文書
- `metadata/`: 対象プラットフォーム、ビルドで実際に使用したFoundation revision、収録物と依存関係の検査結果
- README、VERSION、ライセンス、第三者ライセンス表示

Foundationの共有ライブラリ、ユーザー設定、生成済み実行設定は同梱しません。バイナリは、対応するHakoniwa Business PackのローカルFoundationと組み合わせて利用します。

## サンプル実行との境界

ZIPの展開だけでは、サンプル構成を起動できません。Conductorは複数プロセスの接続構成、Endpoint、RPC、PDU、実行責任を定義した設定を必要とするためです。

サンプル実行コマンドの正本はHakoniwa Business PackのConductor Recipeとします。Recipeには、次を一体として記載します。

- ZIPの配置先
- 必要なFoundation契約
- ユーザー設定と設定生成
- 起動順序と成功条件
- 通常終了と後処理確認

v1.1.0のZIP名は上記で固定されています。Recipeが別名を前提としている場合は、ZIPを改名せずRecipe側を修正してください。
