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
