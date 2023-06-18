import pytest
from numb3rs import validate

@pytest.mark.parametrize("ip_input, expected_output", [
    ("127.0.0.1", True),
    ("10.0.0.1", True),
    ("123 test", False),
    ("1", False),
    ("255.2565654.22.2", False),
    ("127.300.1.1", False),
    ("127.162.cat.dog", False)
])

def test_convert(ip_input, expected_output) -> None:
    assert validate(ip_input) == expected_output


