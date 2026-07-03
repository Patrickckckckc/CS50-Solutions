from response import validate


def test_invalid_input():
    assert validate("alan@@@harvard.edu") == False
    assert validate("josepatrickwackerbauer@gmail..com") == False


def test_valid_input():
    assert validate("malan@harvard.edu") == True
    assert validate("josepatrickwackerbauer@gmail.com") == True
