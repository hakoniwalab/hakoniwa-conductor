# Python時刻同期サンプル

Hakoniwa Conductorの最小動作確認サンプルです。異なるClientノード上の
2つのPython箱庭アセットが、1つのConductor Serverにより協調された箱庭時刻を
表示します。Runtime Delegationは使用しません。

```text
                     Conductor Server
                      /             \
             Conductor Client A   Conductor Client B
                      |             |
             hello-asset-a       hello-asset-b
```

## 公開設定の位置付け

- `config/input/`: Generatorへ渡す人間向け入力です。
- `config/generated/`: v1.0.0 Generatorで生成し、動作確認する固定Fixtureです。
- `asset/hello_asset.py`: ローカルCoreへ登録し、箱庭時刻をJSON Linesで表示します。
- `expected/success.yaml`: smoke testの成功条件です。

最初の動作確認ではGeneratorを実行しません。生成済み設定をそのまま使用します。
設定を変更する場合だけ、対応するGeneratorで再生成してください。

実行環境の準備、起動順、状態確認、正常終了はHakoniwa Business Packの
`hakoniwa-conductor-python-time-sync` Recipeを正本とします。

## 成功時に確認できるログ

```json
{"asset":"hello-asset-a","event":"TICK","tick":20,"sim_time_usec":200000}
{"asset":"hello-asset-b","event":"TICK","tick":20,"sim_time_usec":200000}
```

`smoke`は両アセットが同じ必須tickへ到達し、そのtickの箱庭時刻が一致すること、
時刻が逆行しないこと、検証中に全プロセスが生存していることを確認します。
