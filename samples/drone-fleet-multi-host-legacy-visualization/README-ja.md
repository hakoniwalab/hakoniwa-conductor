# マルチホスト・ドローン可視化向け互換設定

Hakoniwa Business Packのlegacy 256 UAV疎通確認で使用する、公開済みの生成設定です。

- Serverは`srv-01`、Clientは`cli-01`です。
- ClientからServerへTCP接続します。
- Conductor周期は`delta_time_usec=10000`、`max_delay_time_usec=20000`です。
- Client側Visual State PublisherのPDUをServer側へ転送します。

生成ツールは非公開Hakoniwa Conductor PROが所有します。一般ユーザーとBusiness Packは
生成ツールを実行せず、この公開Fixtureを利用します。
