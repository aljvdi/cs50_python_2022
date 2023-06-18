from bank import value


def test_main() -> None:
    assert value('Hello') == 0
    assert value('How are you') == 20
    assert value('Hi') == 20
    assert value('F U') == 100