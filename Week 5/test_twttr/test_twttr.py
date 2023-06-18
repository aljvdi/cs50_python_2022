from twttr import shorten

def test_default() -> None:
    assert shorten("Hi i'm alex") == "H 'm lx"
    assert shorten("$!") == "$!"
    assert shorten("Nothing") == "Nthng"

def test_capital_number() -> None:
    assert shorten("JuST TEsT") == "JST TsT"
    assert shorten("1234") == "1234"


def main():
    test_default()