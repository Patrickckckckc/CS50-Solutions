from um import count


def test_um():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks, um...") == 2

def test_words_um():
    assert count("Um, thanks for the album") == 1


