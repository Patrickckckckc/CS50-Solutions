import pytest
from twttr import shorten


def test_shorten_uppercase():
    assert shorten("SUPERMAN") == "SPRMN"

def test_shorten_lowercase():
    assert shorten("superman") == "sprmn"

def test_shorten_spaces():
    assert shorten("Clark Kent is Superman") == "Clrk Knt s Sprmn"

def test_shorten_punctuation():
    assert shorten("Man,*+") == "Mn,*+"

def test_shorten_numbers():
    assert shorten("1235") == "1235"
