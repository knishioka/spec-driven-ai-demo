# Spec-Driven AI Demo

Issue→Skill→PRテンプレのデモ用リポジトリ

## 目的

- GitHub Issueから自動的にPRを作成するワークフローのデモ
- Claude CodeとSkillsを使った開発プロセスの実践
- 最小限の構成で、スムーズなデモを実現

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
├── src/demoapp/       # アプリケーションコード
├── tests/             # テストコード
├── Makefile           # タスクランナー
├── pyproject.toml     # Python設定
├── README.md          # このファイル
└── CLAUDE.md          # 開発ルール
```

## テスト

```bash
make test
```

数秒で完了する最小限のテストセット。
