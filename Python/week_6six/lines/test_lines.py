from lines import count_lines

def test_valid_files():
    assert count_lines("names.py") == 4
    assert count_lines("students.py") == 10
    assert count_lines("customes.py") == 15

