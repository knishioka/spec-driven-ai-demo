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

    # Keep separators used for slug-like input, remove everything else.
    text = re.sub(r"[^a-zA-Z0-9_-]", "", text)
    text = text.replace("_", "-")

    # Insert hyphen before uppercase letters (handling consecutive capitals).
    result = re.sub(r"([a-z0-9])([A-Z])", r"\1-\2", text)
    result = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1-\2', result)
    result = re.sub(r"-+", "-", result).strip("-")

    return result.lower()
