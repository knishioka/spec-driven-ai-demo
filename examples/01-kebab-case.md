# シナリオ 01: kebab-case変換

**所要時間**: 3-5分
**難易度**: 簡単
**目的**: 最小限のシナリオで全体の流れを体験

## Step 1: /issue-draft への入力

```
テキストをkebab-caseに変換する関数が欲しい
```

### 期待される質問と推奨回答

**Q1: どのような入力形式を想定していますか？**
```
snake_caseやcamelCaseなど、一般的な形式
```

**Q2: 特殊文字や数字の扱いはどうしますか？**
```
英数字のみ対応で十分。特殊文字は無視する方向で
```

**Q3: 空文字やNoneの場合はどうしますか？**
```
空文字を返す
```

### 生成されるファイル

- `ISSUE_TITLE.txt`: "Add to_kebab_case() function"
- `ISSUE_DRAFT.md`: AC付きのIssue本文

## Step 2: /spec で仕様生成

```bash
/spec
```

### spec.md に含まれる主要要素

- **Why**: URL slug生成やファイル名作成での利用
- **AC1**: `hello_world` → `hello-world`
- **AC2**: `HelloWorld` → `hello-world`
- **AC3**: 空文字 → 空文字
- **Non-goals**: Unicode対応、特殊文字の保持

## Step 3: /plan で実装計画

```bash
/plan
```

### plan.md の主要内容

**やること**:
- `src/demoapp/text_utils.py` に `to_kebab_case()` 追加
- `tests/test_text_utils.py` にテストケース3件追加

**やらないこと**:
- 既存関数の変更
- 複雑な正規表現による高度な変換
- Unicode正規化

**検証方法**:
```bash
make test
python -c "from demoapp.text_utils import to_kebab_case; print(to_kebab_case('hello_world'))"
```

## Step 4: /ship で実装

```bash
/ship
```

### 実装される内容

**src/demoapp/text_utils.py**:
```python
def to_kebab_case(text: str) -> str:
    """Convert text to kebab-case.

    Args:
        text: Input string (snake_case, camelCase, etc.)

    Returns:
        kebab-case string

    Examples:
        >>> to_kebab_case('hello_world')
        'hello-world'
        >>> to_kebab_case('HelloWorld')
        'hello-world'
    """
    if not text:
        return ""
    # Convert to lowercase and replace underscores with hyphens
    result = text.lower().replace('_', '-')
    # Handle camelCase by inserting hyphens before uppercase letters
    import re
    result = re.sub(r'([a-z])([A-Z])', r'\1-\2', text).lower()
    return result.replace('_', '-')
```

**tests/test_text_utils.py**:
```python
def test_to_kebab_case_from_snake():
    assert to_kebab_case('hello_world') == 'hello-world'

def test_to_kebab_case_from_camel():
    assert to_kebab_case('HelloWorld') == 'hello-world'

def test_to_kebab_case_empty():
    assert to_kebab_case('') == ''
```

### PR_DRAFT.md のVerificationセクション

```markdown
## Verification

### Automated Tests
- [x] `make test` - ✅ 6 passed in 0.01s (3 new tests added)

### Manual Testing
- [x] `python -c "from demoapp.text_utils import to_kebab_case; print(to_kebab_case('hello_world'))"` - ✅ Returns "hello-world"
- [x] `python -c "from demoapp.text_utils import to_kebab_case; print(to_kebab_case('HelloWorld'))"` - ✅ Returns "hello-world"
```

## 期待される成果

- **コード**: 15行程度の関数
- **テスト**: 3件のテストケース
- **所要時間**: 3-5分
- **変更ファイル**: 2ファイル（実装+テスト）

## デモポイント

1. **曖昧な入力から明確な仕様へ**: "関数が欲しい" → AC3件の仕様
2. **スコープの明確化**: Unicode非対応を明示的にNon-goalsに
3. **検証の透明性**: 実際に実行したコマンドと結果を記録
