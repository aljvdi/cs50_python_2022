from plates import is_valid

def test_requested() -> None:
    assert is_valid('Test Not valid') == False
    assert is_valid('JT') == True
    assert is_valid('C') == False
    assert is_valid('C5') == False
    assert is_valid("A2") == False

def test_numeric() -> None:
    assert is_valid('AAA222') == True
    assert is_valid("&A5A22") == False
    assert is_valid("&.*22 ") == False
    assert is_valid("CS05") == False
    assert is_valid("PI3.14") == False
    assert is_valid("CS50P") == False
    assert is_valid("CS50") == True


def test_zeroInPlate() -> None:
    assert is_valid('AAA05') == False
    assert is_valid('CBS83') == True


def main():
    test_requested()
    test_numeric()

if __name__ == "__main__":
    main()