from seasons import valid, convert_minutes
import datetime
import pytest


def test_valid_format():  # YYYY-MM-DD
    assert valid("1999-01-01") == datetime.date(1999, 1, 1)
    assert valid("2020-04-10") == datetime.date(2020, 4, 10)
    assert valid("2026-02-05") == datetime.date(2026, 2, 5)


def test_invalid_format():
    with pytest.raises(ValueError, match="Invalid Date"):
        valid("January 1, 1999")

    with pytest.raises(ValueError, match="Invalid Date"):
        valid("2020-13-34")


def test_convert_minutes_valid():
    assert convert_minutes("2026-02-05") == "Zero minutes."
    assert (
        convert_minutes("1999-01-01")
        == "Fourteen million, two hundred and fifty-one thousand, six hundred and eighty minutes."
    )


def test_convert_minutes_invalid():
    with pytest.raises(ValueError, match="Date in the Future"):
        convert_minutes("2026-02-06")
