"""Tests for text_utils module."""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from demoapp.text_utils import to_snake_case


def test_to_snake_case_with_spaces():
    """Test converting text with spaces."""
    assert to_snake_case("hello world") == "hello_world"


def test_to_snake_case_with_hyphens():
    """Test converting text with hyphens."""
    assert to_snake_case("hello-world") == "hello_world"


def test_to_snake_case_already_snake():
    """Test text that is already snake_case."""
    assert to_snake_case("hello_world") == "hello_world"
