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

### PRテンプレート

PR本文には以下を必ず含める:

1. **Summary**: 変更の概要
2. **Related Issue**: 対応するIssue番号（`Closes #N`）
3. **Verification**: 検証方法と実行結果

**Verification重要ルール:**
- チェックだけでなく「コマンド + 実行結果」を必ず記載
- 未実施のものはチェックしない（嘘の✅禁止）

**Verification例:**

```markdown
- [x] `make test` - ✅ 7 passed in 0.01s
- [x] Manual check: `python -c "..."` - ✅ Returns expected output
```

## スキル

### 実務用（2コマンド）

- `/create-issue`: 要望→質問→Issue with Spec（ISSUE_WITH_SPEC.md）
- `/resolve-issue`: Issue→Plan→実装→テスト→PR下書き（PR_DRAFT.md）

**推奨**: 実際の開発ではこちらを使用。

### 学習用（4コマンド）

- `/issue-draft`: 要望からIssue草案を作成（ISSUE_DRAFT.md）
- `/spec`: IssueからSpec文書を生成（spec.md）
- `/plan`: Specから実装計画を生成（plan.md）
- `/ship`: 実装→テスト→PR下書き生成（PR_DRAFT.md）

**用途**: プロセスを段階的に理解したい場合。

## 参考

- [GitHub Flow](https://docs.github.com/en/get-started/quickstart/github-flow)
- [INVEST原則](https://en.wikipedia.org/wiki/INVEST_(mnemonic))
