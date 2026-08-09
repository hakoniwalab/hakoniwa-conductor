# はじめに

[English](getting-started.md)

Hakoniwa Conductorの一般利用者向け導線は、Hakoniwa Business Packを入口とします。本書は個々の依存リポジトリを直接clone・build・installする手順ではありません。

## 準備するもの

- [動作環境](environment-ja.md)を満たすホスト
- Hakoniwa Business Pack
- 対象プラットフォームのConductor Release ZIP
- ZIPと同時に公開されたSHA-256チェックサム
- 利用目的に適用されるライセンスへの同意

## 実行までの流れ

```text
Business Pack doctor
        |
        v
Foundationの不足・不整合を解決
        |
        v
Release ZIPをRecipeのwork領域へ配置
        |
        v
ユーザー設定をvalidate / generate
        |
        v
Recipeを起動して成功条件を確認
        |
        v
Recipeの停止操作と後処理確認
```

ZIPの確認と展開は[バイナリパッケージ](binary-package-ja.md)に記載します。具体的な配置先、設定例、起動コマンド、成功ログはBusiness PackのConductor Recipeに記載します。Recipeが要求するFoundationと現在のReceiptが一致する場合、依存コンポーネントは再ビルドせずに再利用されます。

> v1.0.0公開時点では、Conductor Recipeと公開サンプル設定は後続提供です。ZIP単体を展開しても実行構成は生成されません。

## Release ZIPの確認

v1.0.0の配布物は次の名前です。OSとCPUに一致するZIPを選択します。

```text
hakoniwa-conductor-v1.0.0-linux-x86_64.zip
hakoniwa-conductor-v1.0.0-linux-x86_64.zip.sha256
hakoniwa-conductor-v1.0.0-macos-arm64.zip
hakoniwa-conductor-v1.0.0-macos-arm64.zip.sha256
```

チェックサムを確認してから展開してください。ZIP内の`VERSION`、`metadata/build-contract.txt`、`metadata/install-files.txt`で、バージョン、Foundationの固定revision、収録ファイルを確認できます。

プロセスが存在するだけでは成功とはみなしません。Recipeに記載された接続完了、時刻同期、RD切替等の観測点を確認します。終了にはRecipeが指定する通常終了経路を使い、終了後に関連プロセスと使用ポートが残っていないことを確認します。
