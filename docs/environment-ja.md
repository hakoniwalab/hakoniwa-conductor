# 動作環境

[English](environment.md)

| Release | OS | CPU | 状態 |
| --- | --- | --- | --- |
| v1.0.0 | Ubuntu 24.04 | x86_64 | 初回公開対象 |
| v1.0.0 | macOS | arm64 | 公開ZIP対象 |

Linux x86_64 ZIPはDockerの`linux/amd64`環境で生成します。Apple Silicon上の生成ではエミュレーションを利用するためビルド時間は長くなりますが、成果物のCPU契約はx86_64です。

配布ZIPはConductor固有の実行ファイルと公開Generatorを収録し、Core、Endpoint、RPC、Bridgeの共有ライブラリを重複同梱しません。それらはBusiness PackのローカルFoundationへインストールします。システムの`/usr`へ利用者が手作業でインストールする運用は前提にしません。

実際のポート、ホスト名、Dockerの到達方法はRecipeに依存します。ホストとDocker間ではOS固有のIPをユーザー設定へ埋め込まず、Business Packが定義する到達名とポート契約を使用してください。
