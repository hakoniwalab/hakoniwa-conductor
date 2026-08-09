# 概念と設計文書の境界

[English](concepts.md)

## 設計上の正本

箱庭全体の概念、用語、保証、非保証は、[hakoniwa-design-docs](https://github.com/hakoniwalab/hakoniwa-design-docs)を正本とします。

特に、次の用語をHakoniwa Conductor独自の意味で再定義しません。

- Hakoniwa Asset
- Execution Unit（EU）
- Owner／Non-Owner
- Epoch
- Commit Point
- Runtime Delegation（RD）
- Data Plane／Control Plane
- 有界ドリフト

## このリポジトリが説明すること

このリポジトリは、設計概念そのものではなく、Hakoniwa Conductorによる実現範囲を説明します。

- どの設計機能を提供するか
- ユーザーが何を設定するか
- どの設定をGeneratorが導出するか
- どのバイナリをどの順序で起動するか
- 何を観測すれば成功と判断できるか
- どの状況が製品の保証範囲外か

## 重要な責務境界

Conductorは数値計算、数値解法、配置最適化、RD発動ポリシーの最適性を決めません。Conductorの中心的な責務は、EUの実行責任遷移を管理し、EpochとCommit Pointを成立させることです。
