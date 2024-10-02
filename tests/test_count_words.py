import pytest
from lib.count_words import count_words


def test_normal_string():
    string = "How many words are in this sentence"
    result = count_words(string)
    assert result == 7

def test_weird_spaces_string():
    string = "        Bongo            Drums   "
    result = count_words(string)
    assert result == 2

def test_empty_string():
    string = ""
    result = count_words(string)
    assert result == 0
