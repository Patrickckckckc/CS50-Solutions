from numb3rs import validate

def test_invalid_input():
    assert validate("192.168.001.1") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False

def test_valid_input():
    assert validate("255.255.255.255") == True
    assert validate("1.2.3.4") == True
    assert validate("127.0.0.1") == True
