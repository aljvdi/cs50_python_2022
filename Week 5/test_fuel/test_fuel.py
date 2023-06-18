from fuel import convert, gauge
from pytest import raises

def test_convert() -> None:
    with raises(ZeroDivisionError):
        convert('4/0')
    with raises(ValueError):
        convert('one/4')
    assert convert('1/4') == 25
    assert convert('3/4') == 75

def test_gauge() -> None:
    assert gauge(25) == '25%'
    assert gauge(0) == 'E'
    assert gauge(100) == 'F'
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'

if __name__ == "__main__":
    test_convert()
    test_gauge()