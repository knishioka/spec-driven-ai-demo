"""Text utility functions."""

import re


def to_snake_case(text: str) -> str:
    """
    Convert text to snake_case.

    Args:
        text: Input text

    Returns:
        Snake-cased text
    """
    return text.lower().replace(" ", "_").replace("-", "_")


def to_kebab_case(text: str) -> str:
    """
    Convert camelCase/PascalCase text to kebab-case.

    Args:
        text: Input text in camelCase or PascalCase format

    Returns:
        Kebab-cased text with special characters removed

    Examples:
        >>> to_kebab_case("userName")
        'user-name'
        >>> to_kebab_case("UserName")
        'user-name'
        >>> to_kebab_case("XMLParser")
        'xml-parser'
    """
    if not text:
        return ""

    # Check if input contains special characters (non-alphanumeric)
    has_special_chars = bool(re.search(r'[^a-zA-Z0-9]', text))

    # Remove special characters (keep only alphanumeric)
    text = re.sub(r'[^a-zA-Z0-9]', '', text)

    # If original had special characters, just lowercase (don't insert hyphens)
    if has_special_chars:
        return text.lower()

    # Insert hyphen before uppercase letters (handling consecutive capitals)
    result = re.sub(r'([a-z0-9])([A-Z])', r'\1-\2', text)
    result = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1-\2', result)

    return result.lower()
