# Spec-Driven AI Demo

仕様書駆動開発（Specification-Driven Development）の実践例を示すデモリポジトリ

## このデモでできること

**仕様書駆動開発のワークフローを5〜10分で体験**できます：

1. **曖昧な要望を構造化** - `/issue-draft`で質問を通じてIssue草案を作成
2. **仕様を明確化** - `/spec`でWhy/AC/Non-goalsを含むspec.mdを生成
3. **実装範囲を決定** - `/plan`で「このPRでやる/やらない」を明確化
4. **実装と検証** - `/ship`で実装→テスト→PR下書き作成を自動化

### 仕様書駆動開発とは

コードを書く前に「何を作るか」を明文化し、以下を実現する開発手法：

- **スコープの明確化** - やる/やらないを事前に合意
- **観測可能な成功条件** - テスト可能なAcceptance Criteriaを定義
- **最小限の変更** - 過剰な実装や関係ない修正を防ぐ
- **検証の透明性** - 実行コマンドと結果を記録

このデモでは、Claude Code Skillsを使ってこのプロセスを自動化・効率化します。

## 目的

- 仕様書駆動開発の実践プロセスを体験
- Claude CodeとSkillsを使った開発ワークフローの実演
- Issue→Spec→Plan→PR の一連の流れを最小構成で実現

## 使い方

### ローカル環境

```bash
# 依存関係をインストール
make install

# テストを実行
make test
```

### デモ手順（5〜10分で完結）

1. `/issue-draft` - 要望から Issue草案を作成（曖昧なら質問で深掘り）
2. `/spec` - Issue から spec.md を生成
3. `/plan` - spec.md から plan.md を生成（PR範囲を明確化）
4. `/ship` - 実装→テスト→PR_DRAFT.md 生成

### Claude Code on the Web

1. リポジトリをクローン
2. `make test` でテスト実行を確認
3. Issueを作成してスキルを実行

## 主要コマンド

| コマンド | 説明 |
|---------|------|
| `make test` | テスト実行（最重要） |
| `make install` | 開発依存関係のインストール |
| `make clean` | キャッシュファイルの削除 |

## プロジェクト構成

```
.
├── .claude/skills/    # デモ用Skills（issue-draft/spec/plan/ship）
├── src/demoapp/       # アプリケーションコード
├── tests/             # テストコード
├── Makefile           # タスクランナー
├── pyproject.toml     # Python設定
├── README.md          # このファイル
└── CLAUDE.md          # 開発ルール
```

## 生成されるファイル（.gitignore済み）

ワークフロー実行時、以下のファイルがプロジェクトルートに生成されます：

- `ISSUE_TITLE.txt` - Issue タイトル案
- `ISSUE_DRAFT.md` - GitHub Issue 本文（AC/Non-goals/Tasks付き）
- `spec.md` - 仕様書（Why/AC/Non-goals/Constraints）
- `plan.md` - 実装計画（やる/やらない、検証方法）
- `PR_DRAFT.md` - PR本文（実行結果付き）

### オプション: ファイルを整理する

デモファイルを整理したい場合：

```bash
mkdir spec-driven
# 生成されたファイルを移動
mv ISSUE_*.md spec.md plan.md PR_DRAFT.md spec-driven/
```

## テスト

```bash
make test
```

数秒で完了する最小限のテストセット。

## デモ実演例

### ケース: camelCase変換関数の追加

```bash
# Step 1: Issue草案作成
/issue-draft
> "テキストをcamelCaseに変換する関数を追加したい"
→ 質問で深掘り → ISSUE_DRAFT.md 生成

# Step 2: 仕様書生成
/spec
→ spec.md 生成（Why/AC/Non-goals明確化）

# Step 3: 実装計画
/plan
→ plan.md 生成（このPRでやる/やらないを宣言）

# Step 4: 実装と検証
/ship
→ 実装 → make test → PR_DRAFT.md 生成
```

**所要時間**: 5〜10分
**成果物**: 実装コード + テスト + 検証済みPR下書き
