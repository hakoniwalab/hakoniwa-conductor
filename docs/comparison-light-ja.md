# Conductor Lightとの比較

[English](comparison-light.md)

Conductor Lightは、Hakoniwa Conductorの実行責任管理機能のサブセットです。ただし、単なる下位版ではありません。Assetの動的な参加・離脱や、Web・ROSを含む外部システムとの柔軟な連携を重視する、目的の異なる実装です。

## 実行責任とシミュレーション意味論

| 機能・概念 | Conductor Light | Hakoniwa Conductor | 補足 |
| --- | :---: | :---: | --- |
| 分散時刻同期 | 対応 | 対応 | 有界ドリフトの定義はdesign-docsを参照 |
| 時刻同期誤差の計測・データ出力 | 未対応 | 未対応 | 基準時刻と観測時刻の差を数値データとして取得する機能。UIやグラフによる可視化は含まない |
| Assetの動的参加・離脱 | 対応 | 対象外 | Hakoniwa Conductorでは製品の責務として扱わない |
| シミュレーション開始・停止・リセット | 対応 | 対応 | 操作APIと状態契約は実装ごとに異なる |
| EUのOwner管理 | 対象外 | 対応 | Ownerはdesign-docsの定義に従う |
| Epoch管理 | 対象外 | 対応 | Epochはdesign-docsの定義に従う |
| Commit Point | 対象外 | 対応 | 物理的な開始同期点ではない |
| Runtime Delegation | 対象外 | 対応 | 実行責任を安全に切り替える |

## 目的と外部連携

| 観点 | Conductor Light | Hakoniwa Conductor |
| --- | --- | --- |
| 主目的 | 軽量な実行制御と外部システム連携 | 実行責任と因果境界の管理 |
| 構成モデル | 動的で柔軟な接続を重視 | EU、Owner、Epochに基づく管理構成 |
| Web連携 | 重点領域。実装済みと計画を分けて公開する | Remote API等を介した管理連携 |
| ROS連携 | 重点領域。実装済みと計画を分けて公開する | 箱庭側の実行責任管理を中心とする |
| 適する用途 | UI、ROS、試作、軽量統合 | 分散実行、責任移譲、因果管理 |

## 選択の目安

Conductor Lightが適する場合:

- Assetの動的な参加・離脱を重視する
- WebやROSとの柔軟な接続を重視する
- Owner、Epoch、Commit Point、RDが不要である

Hakoniwa Conductorが適する場合:

- EUごとの実行責任を明示したい
- Ownerの切替をEpochとして管理したい
- Commit Pointで責任と因果境界を確定したい
- Runtime Delegationを利用したい
