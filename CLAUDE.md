# CLAUDE.md - 開発ルール

このリポジトリでAI支援開発を行う際の基本ルール。

## 原則

### 1 Issue = 1 PR

- 1つのIssueには1つのPRのみを対応させる
- PRは必ず対応するIssueを持つ（Issue番号をブランチ名に含める）
- 独立した変更は別々のIssueとPRに分割する

### 変更のスコープ

**禁止事項:**
- 大規模なリファクタリング（Issue範囲外の変更）
- 関係ないファイルの修正や整形
- Issue要件に含まれない「ついでの改善」

**推奨:**
- Issueで定義された要件のみに集中
- 最小限の変更で要件を満たす
- 追加の改善は別Issueとして起票

## 実行コマンド

開発時は必ず以下のコマンドでテストを実行:

```bash
make test
```

## PR作成

### PRテンプレート（今後導入予定）

PR本文には以下を必ず含める:

1. **Summary**: 変更の概要
2. **Related Issue**: 対応するIssue番号（`Closes #N`）
3. **Verification**: 検証方法

**Verification例:**

```bash
make test  # すべてのテストが通ることを確認
```

## スキル実行

今後、以下のようなスキルを追加予定:

- `/resolve-issue <n>`: Issue自動解決ワークフロー
- `/resolve-feedback`: PRレビューフィードバック対応

## 参考

- [GitHub Flow](https://docs.github.com/en/get-started/quickstart/github-flow)
- [INVEST原則](https://en.wikipedia.org/wiki/INVEST_(mnemonic))
