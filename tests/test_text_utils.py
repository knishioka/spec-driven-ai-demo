"""Tests for text_utils module."""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from demoapp.text_utils import to_snake_case, to_kebab_case


def test_to_snake_case_with_spaces():
    """Test converting text with spaces."""
    assert to_snake_case("hello world") == "hello_world"


def test_to_snake_case_with_hyphens():
    """Test converting text with hyphens."""
    assert to_snake_case("hello-world") == "hello_world"


def test_to_snake_case_already_snake():
    """Test text that is already snake_case."""
    assert to_snake_case("hello_world") == "hello_world"


def test_to_kebab_case_camelcase():
    """Test converting camelCase to kebab-case."""
    assert to_kebab_case("userName") == "user-name"


def test_to_kebab_case_pascalcase():
    """Test converting PascalCase to kebab-case."""
    assert to_kebab_case("UserName") == "user-name"


def test_to_kebab_case_special_chars():
    """Test removing special characters during conversion."""
    assert to_kebab_case("user!Name@123") == "username123"


def test_to_kebab_case_consecutive_capitals():
    """Test handling consecutive capitals."""
    assert to_kebab_case("XMLParser") == "xml-parser"


def test_to_kebab_case_empty_string():
    """Test handling empty string."""
    assert to_kebab_case("") == ""
