# Hakoniwa Conductor

[English](README-en.md)

Hakoniwa Conductorは、分散シミュレーションにおける実行責任と因果境界を管理する箱庭のControl Plane実装です。

本公開版は、学術研究、教育、非商用研究開発、論文の追試および再現性検証で利用できるバイナリ、設定Generatorと利用ドキュメントを提供します。設定例、サンプルアプリケーションおよびHakoniwa Business Pack Recipeは段階的に公開します。

無償版は**バイナリ配布のみ**です。Conductor本体およびRuntime Delegation（RD）のソースコードは公開しません。商用利用向けには、契約条件に基づいてソースコード、ドキュメント、バイナリ等を提供する「箱庭コンダクタPRO」を別途提供します。

## 利用の入口

環境構築、依存コンポーネント、ローカルFoundation、Recipe、実行および検証は、[Hakoniwa Business Pack](https://github.com/hakoniwalab/hakoniwa-business-pack)を入口として管理します。

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

初めて利用する場合は、[はじめに](docs/getting-started-ja.md)から進めてください。公開文書の全体像は[公開ドキュメント一覧](docs/index-ja.md)にあります。

初回バイナリReleaseは `v1.0.0` です。成果物は `hakoniwa-conductor-v1.0.0-linux-x86_64.zip` と `hakoniwa-conductor-v1.0.0-macos-arm64.zip` です。収録物と配置方法は[バイナリパッケージ](docs/binary-package-ja.md)を参照してください。

## 最短の利用経路

1. [動作環境](docs/environment-ja.md)を確認する。
2. Hakoniwa Business PackでConductor用Foundationを準備する。
3. Releaseから対象OS・CPUのZIPとSHA-256ファイルを取得する。
4. [バイナリパッケージ](docs/binary-package-ja.md)に従ってZIPを確認・展開する。
5. 対応するBusiness Pack Recipeが公開済みなら、その`doctor`、設定生成、スモークテストを順に実行する。
6. Recipeの停止操作で正常終了し、プロセスとポートの解放を確認する。

個別Foundationのビルドコマンドはこのリポジトリへ複製しません。再利用判定と依存関係の構築はBusiness Packを正とします。

## 公開範囲

公開するもの:

- ConductorとRDバイナリの利用方法
- ユーザー向け設定スキーマと設定例
- 詳細設定の自動生成バイナリ
- 公開境界を確認済みの設定例およびサンプルアプリケーション（段階的に追加）
- MacおよびUbuntuの環境・運用・検証手順
- Conductor Lightとの機能および目的の違い

公開しないもの:

- Conductor本体のソースコード
- RDのソースコードおよび内部アルゴリズム
- 商用機能の実装詳細

## 設計上の位置付け

EU、Owner、Epoch、Commit Point、Runtime Delegation、有界ドリフトなど、箱庭全体の用語と実装非依存の意味論は、[hakoniwa-design-docs](https://github.com/hakoniwalab/hakoniwa-design-docs)を設計上の正本とします。

このリポジトリでは、それらの概念をHakoniwa Conductorがどこまで実現し、どのように設定・実行・検証するかを説明します。

## Conductor Lightとの関係

Conductor Lightは、Hakoniwa Conductorの実行責任管理機能のサブセットを持つ一方、Assetの動的な参加・離脱や、Web・ROSを含む外部システムとの柔軟な連携を重視します。

両者は単純な上位・下位関係ではありません。実行責任、Epoch、Commit Point、RDを必要とする場合はHakoniwa Conductorを、軽量な実行制御と柔軟な外部連携を重視する場合はConductor Lightを選択します。詳細は[Conductor Lightとの比較](docs/comparison-light-ja.md)を参照してください。

## ライセンス

本リポジトリは利用目的に応じたデュアルライセンス方式で提供します。

| 利用区分 | 提供形態 | 主な利用範囲 | 適用条件 |
| --- | --- | --- | --- |
| 箱庭コンダクタ 無償版 | バイナリのみ | 個人利用、学術研究、教育、非商用研究開発、査読、追試、再現性検証、ベンチマーク | [日本語](LICENSE-NC-ja.md) / [English](LICENSE-NC.md) |
| 箱庭コンダクタPRO | ソースコード、ドキュメント、バイナリ等を契約に基づき提供 | 商用製品・サービス、部門内部利用、受託開発、コンサルティング、システムインテグレーションその他の商用利用 | 合同会社箱庭ラボとの別途契約が必要です。[商用ライセンス（日本語）](LICENSE-PRO-ja.md) |

無償版では、研究結果、計測結果、ベンチマーク結果、図表および論文を公表できます。一方、バイナリのリバースエンジニアリング、逆コンパイル、逆アセンブル、改変および派生物の作成は禁止されています。公開リポジトリの閲覧、clone、downloadのみをもって商用利用権が付与されるものではありません。

個別のライセンス表示が付されたファイルおよび第三者コンポーネントには、それぞれの条件が適用されます。
