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

### ワークフロー

このリポジトリには2種類のワークフローがあります：

#### 実務用（2コマンド）- 推奨

```bash
/create-issue    # Issue草案→Spec（ISSUE_WITH_SPEC.md）を一気に作成
/resolve-issue   # Issue→Plan→実装→テスト→PR下書き
```

**所要時間**: 5-10分
**用途**: 実際の開発で使う効率的なワークフロー

#### 学習用（4コマンド）- プロセス理解

```bash
/issue-draft     # Issue草案作成
/spec            # spec.md生成
/plan            # plan.md生成
/ship            # 実装→テスト→PR下書き
```

**所要時間**: 5-10分（同じ）
**用途**: 仕様書駆動開発のプロセスを段階的に理解

### デモ手順

**実務用ワークフロー（推奨）**:
1. `/create-issue` - 質問に答えて ISSUE_WITH_SPEC.md 生成
2. Issue をGitHubに投稿（または手元で確認）
3. `/resolve-issue` - plan.md確認後、実装→PR下書き生成

**学習用ワークフロー**:
1. `/issue-draft` - Issue草案作成
2. `/spec` - 仕様明確化
3. `/plan` - 実装範囲決定
4. `/ship` - 実装と検証

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
├── examples/          # デモシナリオ集（入力例・期待される流れ）
│   ├── README.md
│   ├── 01-kebab-case.md
│   ├── 02-truncate-text.md
│   └── 03-slugify.md
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

## デモシナリオ

[`examples/`](examples/) ディレクトリに詳細なデモシナリオを用意しています：

| シナリオ | 所要時間 | 難易度 | 推奨用途 |
|---------|---------|--------|----------|
| [01-kebab-case](examples/01-kebab-case.md) | 3-5分 | 簡単 | 短時間で全体の流れを見せる |
| [02-truncate-text](examples/02-truncate-text.md) | 5-7分 | 中程度 | ビジネスロジック仕様化を体験 |
| [03-slugify](examples/03-slugify.md) | 7-10分 | やや複雑 | 技術的検討を含む完全な流れ |

各シナリオには以下が含まれます：
- `/issue-draft` への入力例
- 期待される質問と推奨回答
- 生成される仕様書・計画のポイント
- 実装コード例
- デモで強調すべきポイント

### クイックスタート: kebab-case変換（3-5分）

```bash
# Step 1: Issue草案作成
/issue-draft
> "テキストをkebab-caseに変換する関数が欲しい"
→ 質問で深掘り（入力形式、特殊文字等）→ ISSUE_DRAFT.md 生成

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

詳細は [examples/01-kebab-case.md](examples/01-kebab-case.md) を参照。
