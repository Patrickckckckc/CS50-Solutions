from plates import is_valid


# FOUR OR MORE TESTS
def test_long():
    assert is_valid("safkjsfajkfjasbfa") == False
    assert is_valid("a") == False
    assert is_valid("CS50") == True


def test_just_numbers():
    assert is_valid("123456") == False


def test_just_letters():
    assert is_valid("HELLO") == True
    assert is_valid("GOOD") == True


def test_numbers():
    assert is_valid("50CS") == False
    assert is_valid("CS05") == False
    assert is_valid("CS1000") == True
    assert is_valid("CS000C") == False
