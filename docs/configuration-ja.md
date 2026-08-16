# 設定とGenerator

[English](configuration.md)

Conductorの設定は、ユーザー入力と生成された実行時設定を分離します。

```text
ユーザー向けEU設定
        |
        | validate / resolve
        v
Conductor Generator
        |
        +-- execution-unit.json
        +-- Bridge / Endpoint設定
        +-- Conductor Server / Client設定
        `-- RD / Runtime Context設定（RD構成のみ）
```

ユーザーはノード構成、EU配置、時刻パラメータ、転送ポリシー等を指定します。Endpoint ID、接続方向、Control Plane用の詳細設定など、構成から一意に導出できる値はGeneratorが設定します。

生成先はBusiness Pack Recipeの`work/recipes/<recipe-id>/config/`配下とし、生成物を直接編集しません。入力変更後は再生成し、validateが成功した生成物だけを実行に使用します。相対パスの基準はGeneratorの出力ディレクトリで固定し、カレントディレクトリへ暗黙依存させません。

入力スキーマ、既定値、生成ファイル一覧は公開サンプルと同時に提供します。バイナリとGeneratorの互換性は[互換性](compatibility-ja.md)で管理します。

公開入力契約は[`schemas/eu-input-v1.schema.json`](../schemas/eu-input-v1.schema.json)です。
Recipeは、再生成に非公開製品が必要であることを明記したうえで、schema準拠の入力と
生成済み設定をコミットし、第三者による確認と実行を可能にできます。
