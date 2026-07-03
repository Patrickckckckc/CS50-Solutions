from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("HELLO") == 0


def test_h():
    assert value("h") == 20
    assert value("HI") == 20
    assert value("hey baby girl") == 20


def test_not_h():
    assert value("Greetings") == 100
    assert value("good afternoon") == 100

