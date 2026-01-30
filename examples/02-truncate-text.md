# シナリオ 02: テキスト切り詰め

**所要時間**: 5-7分
**難易度**: 中程度
**目的**: ビジネスロジックと複数ACの仕様化を体験

## Step 1: /issue-draft への入力

```
長いテキストを指定文字数で切り詰めて、省略記号をつける機能
```

### 期待される質問と推奨回答

**Q1: 省略記号は何を使いますか？**
```
"..." (3ドット) を使いたい
```

**Q2: 切り詰める長さは固定ですか、可変ですか？**
```
関数の引数で指定できるようにしたい
```

**Q3: 単語の途中で切れてもいいですか？**
```
最初のバージョンでは単純に文字数でカットで良い。単語境界考慮は将来的に
```

**Q4: テキストが短い場合はどうしますか？**
```
そのまま返す（省略記号不要）
```

### 生成されるファイル

- `ISSUE_TITLE.txt`: "Add truncate_text() function with ellipsis"
- `ISSUE_DRAFT.md`: AC4件とNon-goals明記

## Step 2: /spec で仕様生成

```bash
/spec
```

### spec.md に含まれる主要要素

- **Why**: UI表示での長文対応（カード、リスト、プレビュー等）
- **AC1**: 指定長を超える場合、切り詰め＋"..."
- **AC2**: 指定長以下の場合、そのまま返す
- **AC3**: 空文字は空文字を返す
- **AC4**: 負の長さを指定した場合はエラー
- **Non-goals**:
  - 単語境界での切り詰め
  - HTML タグの考慮
  - マルチバイト文字の特別扱い
- **Constraints**:
  - 省略記号 "..." は文字数に含める
  - 最大長3文字未満の場合は省略記号なしで切り詰め

## Step 3: /plan で実装計画

```bash
/plan
```

### plan.md の主要内容

**やること**:
- `src/demoapp/text_utils.py` に `truncate_text(text, max_length)` 追加
- `tests/test_text_utils.py` にテストケース5-6件追加
  - 長いテキスト切り詰め
  - 短いテキストそのまま
  - 空文字
  - エッジケース（max_length=0, 負数）

**やらないこと**:
- 単語境界での切り詰め（`smart_truncate()`は別Issue）
- HTMLタグの除去・保持
- カスタム省略記号

**検証方法**:
```bash
make test
python -c "from demoapp.text_utils import truncate_text; print(truncate_text('Hello World', 8))"
python -c "from demoapp.text_utils import truncate_text; print(truncate_text('Hi', 10))"
```

## Step 4: /ship で実装

```bash
/ship
```

### 実装される内容

**src/demoapp/text_utils.py**:
```python
def truncate_text(text: str, max_length: int) -> str:
    """Truncate text to max_length with ellipsis.

    Args:
        text: Input text
        max_length: Maximum length including ellipsis

    Returns:
        Truncated text with "..." if needed

    Raises:
        ValueError: If max_length is negative

    Examples:
        >>> truncate_text('Hello World', 8)
        'Hello...'
        >>> truncate_text('Hi', 10)
        'Hi'
        >>> truncate_text('', 5)
        ''
    """
    if max_length < 0:
        raise ValueError("max_length must be non-negative")

    if not text or len(text) <= max_length:
        return text

    # Reserve space for ellipsis if max_length >= 3
    if max_length < 3:
        return text[:max_length]

    return text[:max_length - 3] + "..."
```

**tests/test_text_utils.py**:
```python
import pytest
from demoapp.text_utils import truncate_text

def test_truncate_text_long():
    assert truncate_text('Hello World', 8) == 'Hello...'

def test_truncate_text_short():
    assert truncate_text('Hi', 10) == 'Hi'

def test_truncate_text_empty():
    assert truncate_text('', 5) == ''

def test_truncate_text_exact_length():
    assert truncate_text('Hello', 5) == 'Hello'

def test_truncate_text_very_short_limit():
    assert truncate_text('Hello', 2) == 'He'

def test_truncate_text_negative_length():
    with pytest.raises(ValueError):
        truncate_text('Hello', -1)
```

### PR_DRAFT.md のVerificationセクション

```markdown
## Verification

### Automated Tests
- [x] `make test` - ✅ 9 passed in 0.02s (6 new tests added)

### Manual Testing
- [x] `python -c "from demoapp.text_utils import truncate_text; print(truncate_text('Hello World', 8))"` - ✅ Returns "Hello..."
- [x] `python -c "from demoapp.text_utils import truncate_text; print(truncate_text('Hi', 10))"` - ✅ Returns "Hi"
- [x] `python -c "from demoapp.text_utils import truncate_text; print(truncate_text('Hello', -1))"` - ✅ Raises ValueError

## Risk & Rollback
**Risk**: Edge case handling for very short max_length might be unexpected to users.
**Rollback**: Remove truncate_text() function and its tests - no impact on existing code.
```

## 期待される成果

- **コード**: 25行程度の関数（docstring含む）
- **テスト**: 6件のテストケース（正常系4件、異常系2件）
- **所要時間**: 5-7分
- **変更ファイル**: 2ファイル

## デモポイント

1. **ビジネスコンテキスト**: "UI表示での長文対応"という明確なユースケース
2. **制約の明示**: "省略記号は文字数に含める"などの仕様詳細化
3. **Non-goalsの価値**: 単語境界対応を明示的に除外→将来のIssue化
4. **エッジケース**: 異常系テストまで含む完全な実装
