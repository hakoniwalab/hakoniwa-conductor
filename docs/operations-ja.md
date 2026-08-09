# 運用

[English](operations.md)

標準ライフサイクルは次のとおりです。

1. `doctor`: OS、CPU、Foundation、Release、設定、ポートを確認する。
2. `configure`: ユーザー設定を検証し、Recipeの作業領域へ生成する。
3. `start`: Server、Client、ExMonitor、AssetをRecipe指定順に起動する。
4. `status`: PIDだけでなく、接続・同期・RDの成功ログを確認する。
5. `terminate`: 各ランタイムの通常終了経路を呼び出す。
6. `cleanup`: 記録されたプロセスと使用ポートが解放されたことを確認する。

AIや自動化ツールも、Recipeが指定するsessionまたはPIDだけを管理します。無関係なプロセスを含む広範な`pkill`や`kill -9`を通常停止として使用しません。

異常時は、上書きされる`latest`証跡領域に設定、ログ、判定結果を残します。無制限にrun-idディレクトリを増やさず、保存が必要な失敗だけをメンテナーが退避します。
