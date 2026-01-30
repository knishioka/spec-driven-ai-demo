# シナリオ 03: URL-safe slug生成

**所要時間**: 7-10分
**難易度**: やや複雑
**目的**: 技術的検討を含む仕様化プロセスの体験

## Step 1: /issue-draft への入力

```
記事タイトルからURL用のslugを生成する関数を追加したい
```

### 期待される質問と推奨回答

**Q1: どのような入力を想定していますか？**
```
ブログ記事のタイトル。日本語も含まれる可能性がある
```

**Q2: Unicode（日本語など）はどう扱いますか？**
```
最初のバージョンでは英数字のみ対応。日本語はスキップする方向で
```

**Q3: スペースや特殊文字はどうしますか？**
```
スペースはハイフンに変換、特殊文字は削除
```

**Q4: 大文字小文字はどうしますか？**
```
すべて小文字に統一
```

### 生成されるファイル

- `ISSUE_TITLE.txt`: "Add slugify() function for URL-safe slugs"
- `ISSUE_DRAFT.md`: AC付き + 技術的検討メモ

## Step 2: /spec で仕様生成

```bash
/spec
```

### spec.md に含まれる主要要素

- **Why**:
  - ブログシステムでのURL生成
  - SEO-friendlyなパーマリンク作成
  - ファイル名としても利用可能

- **Acceptance Criteria**:
  - AC1: 英数字のみを保持、小文字に変換
  - AC2: スペース → ハイフン
  - AC3: 連続するハイフンは1つにまとめる
  - AC4: 先頭・末尾のハイフンは削除
  - AC5: 空文字や記号のみの場合は空文字を返す

- **Non-goals**:
  - Unicode文字の音訳（transliteration）
  - カスタムセパレータ
  - 最大長制限
  - 予約語チェック

- **Constraints**:
  - 英数字以外は削除（Unicode非対応を明示）
  - ハイフンのみを区切り文字として使用

## Step 3: /plan で実装計画

```bash
/plan
```

### plan.md の主要内容

**このPRでやること**:
- `src/demoapp/text_utils.py` に `slugify(text)` 関数追加
- 以下の処理を実装:
  1. 小文字化
  2. 英数字以外をスペースに変換
  3. スペースをハイフンに変換
  4. 連続ハイフンの統合
  5. 先頭・末尾ハイフン削除
- `tests/test_text_utils.py` に8-10件のテストケース追加

**このPRでやらないこと**:
- Unicode正規化・音訳（別Issue: "Add Unicode support to slugify"）
- 最大長制限（別Issue: "Add max_length to slugify"）
- カスタムセパレータ対応
- 既存関数の変更

**影響範囲**:
- 新規関数のため既存コードへの影響なし

**検証方法**:
```bash
make test
python -c "from demoapp.text_utils import slugify; print(slugify('Hello World!'))"
python -c "from demoapp.text_utils import slugify; print(slugify('  Multiple   Spaces  '))"
python -c "from demoapp.text_utils import slugify; print(slugify('日本語タイトル'))"
```

**リスク**:
- 英数字のみ対応のため、日本語タイトルは空文字になる
- 将来的にUnicode対応が必要になる可能性

**ロールバック**:
- 関数とテストを削除するだけで元に戻せる

## Step 4: /ship で実装

```bash
/ship
```

### 実装される内容

**src/demoapp/text_utils.py**:
```python
import re

def slugify(text: str) -> str:
    """Convert text to URL-safe slug.

    Converts text to lowercase, removes non-alphanumeric characters,
    and replaces spaces with hyphens.

    Args:
        text: Input text

    Returns:
        URL-safe slug (lowercase, alphanumeric + hyphens)

    Examples:
        >>> slugify('Hello World!')
        'hello-world'
        >>> slugify('  Multiple   Spaces  ')
        'multiple-spaces'
        >>> slugify('Special @#$ Characters')
        'special-characters'
        >>> slugify('日本語')
        ''

    Note:
        Currently supports ASCII alphanumeric only.
        Unicode characters are removed.
    """
    if not text:
        return ""

    # Convert to lowercase
    text = text.lower()

    # Replace non-alphanumeric with spaces
    text = re.sub(r'[^a-z0-9]+', ' ', text)

    # Replace spaces with hyphens
    text = text.strip().replace(' ', '-')

    # Remove consecutive hyphens
    text = re.sub(r'-+', '-', text)

    # Remove leading/trailing hyphens
    return text.strip('-')
```

**tests/test_text_utils.py**:
```python
from demoapp.text_utils import slugify

def test_slugify_basic():
    assert slugify('Hello World') == 'hello-world'

def test_slugify_special_chars():
    assert slugify('Hello World!') == 'hello-world'

def test_slugify_multiple_spaces():
    assert slugify('  Multiple   Spaces  ') == 'multiple-spaces'

def test_slugify_special_characters():
    assert slugify('Special @#$ Characters') == 'special-characters'

def test_slugify_numbers():
    assert slugify('Article 123') == 'article-123'

def test_slugify_consecutive_hyphens():
    assert slugify('Hello---World') == 'hello-world'

def test_slugify_unicode():
    # Non-ASCII characters are removed
    assert slugify('日本語') == ''

def test_slugify_mixed_unicode():
    assert slugify('Hello 日本語 World') == 'hello-world'

def test_slugify_empty():
    assert slugify('') == ''

def test_slugify_symbols_only():
    assert slugify('@#$%') == ''
```

### PR_DRAFT.md のVerificationセクション

```markdown
## Verification

### Automated Tests
- [x] `make test` - ✅ 13 passed in 0.02s (10 new tests added)

### Manual Testing
- [x] `python -c "from demoapp.text_utils import slugify; print(slugify('Hello World!'))"` - ✅ Returns "hello-world"
- [x] `python -c "from demoapp.text_utils import slugify; print(slugify('  Multiple   Spaces  '))"` - ✅ Returns "multiple-spaces"
- [x] `python -c "from demoapp.text_utils import slugify; print(slugify('日本語タイトル'))"` - ✅ Returns "" (expected: Unicode not supported)
- [x] `python -c "from demoapp.text_utils import slugify; print(slugify('Article 123'))"` - ✅ Returns "article-123"

## Risk & Rollback
**Risk**: Unicode characters are removed, so non-ASCII titles produce empty slugs. Future enhancement needed for international content.
**Rollback**: Remove slugify() function and its tests - no impact on existing code.

## Future Work
- Issue #X: Add Unicode normalization and transliteration to slugify()
- Issue #Y: Add max_length parameter to slugify()
```

## 期待される成果

- **コード**: 35行程度（関数本体+詳細docstring）
- **テスト**: 10件のテストケース（正常系8件、エッジケース2件）
- **所要時間**: 7-10分
- **変更ファイル**: 2ファイル

## デモポイント

1. **技術的判断の明示化**: Unicode非対応を仕様として明記
2. **将来の拡張**: Non-goalsに書いたものが将来のIssue候補に
3. **複雑な要件の分解**: 5つのACに分解して検証可能に
4. **実用的な例**: ブログシステムという明確なユースケース
5. **リスクの透明性**: PR_DRAFT.mdでUnicode制限を明記

## デモ時の追加説明ポイント

- **なぜUnicode非対応？**: 最初のバージョンで複雑にしすぎない（YAGNI原則）
- **どうやって拡張？**: Non-goalsを別Issueとして起票→同じワークフロー適用
- **実際のプロジェクトでは？**: Unicode対応は `unidecode` ライブラリを使うなど
