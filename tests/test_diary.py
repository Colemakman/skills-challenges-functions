import pytest
from lib.diary import make_snippet


def test_long_string():
    string = "How are you doing on this fine day"
    result = make_snippet(string)
    assert result == "How are you doing on ..."

def test_empty_string():
    string = ""
    result = make_snippet(string)
    assert result == ""

def test_short_string():
    string = "Hello world"
    result = make_snippet(string)
    assert result == "Hello world"

