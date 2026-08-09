# Hakoniwa Conductor アーキテクチャ

[English](architecture.md)

## 利用者から見える構成

```text
Remote API / operation policy
             |
             v
          Conductor
             |
             | Owner / Epoch / Commit Point
             v
       RD control components
             |
             v
Bridge / Endpoint ---------------- Hakoniwa Assets
      Control Plane boundary          Data Plane
```

- **Conductor**: EUの実行責任遷移を管理し、EpochとCommit Pointを確定します。
- **RD components**: Conductorが決定した実行責任の切替を、分散した実行主体との間で成立させます。
- **Remote API**: 外部の運用・制御システムからControl Planeを操作する境界です。
- **Bridge／Endpoint**: Control Planeの決定とData Planeの通信・寿命セマンティクスを接続します。
- **Hakoniwa Asset**: シミュレーション処理を実行し、一つ以上のEU実体を保持します。

## 設定生成

ユーザーは、EU、配置、接続、PDU、Conductorの既定値などをユーザー向け設定に記述します。Generatorは、実行時に各コンポーネントが読む詳細設定を生成します。

```text
user configuration
        |
        | validate / generate
        v
execution-unit definition
        |
        +-- Conductor configuration
        +-- Bridge configuration
        +-- Endpoint configuration
        +-- RPC / Remote API configuration
        `-- RD control configuration
```

生成物は実行時の入力であり、原則として直接編集しません。ユーザー向け設定とGeneratorのバージョンを、使用するバイナリと対応付けます。

## 実行環境

環境構築と実行はHakoniwa Business Packを入口とします。Foundationは共通依存をローカル領域へ導入し、Recipeは要求構成、設定生成、起動、検証、正常終了を定義します。
