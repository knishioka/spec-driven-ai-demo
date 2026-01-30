"""Text utility functions."""


def to_snake_case(text: str) -> str:
    """
    Convert text to snake_case.

    Args:
        text: Input text

    Returns:
        Snake-cased text
    """
    return text.lower().replace(" ", "_").replace("-", "_")
