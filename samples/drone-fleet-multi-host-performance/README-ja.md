# マルチホスト・ドローン性能検証向け設定

Hakoniwa Business Packの`drone-fleet-multi-host` RecipeがExperiment Cの
performance／temporal validationで使用する、公開済みの生成設定です。

- `config/input/eu-input.json`は公開入力契約です。
- `config/generated/`はHakoniwa Conductor v1.1.0向け生成済みRuntime Fixtureです。
- Serverは`srv-01`、Clientは`cli-01`で、ClientからServerへTCP接続します。
- `delta_time_usec=1000`、`real_sleep_msec=1`、
  `simtime_publish_mode=delta_boundary`、
  `simtime_publish_interval_usec=10000`を固定します。
- UAV数とDrone process数はConductor topologyを変更しないため、このFixtureを共有します。

生成ツールは非公開Hakoniwa Conductor PROが所有します。一般ユーザーとBusiness Packは
生成ツールを実行せず、この公開Fixtureを検証してRecipe workspaceへコピーします。
