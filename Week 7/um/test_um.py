import pytest
from um import count

@pytest.mark.parametrize("text_input, expected_output", [
    ("Hello, Um, World", 1),
    ("Without that world :)", 0),
    ("I, Um, Perosonally, UM, so, um, tired", 3),
    ("um", 1),
    ("255.2565654.22.2", 0),
    ("Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?", 2)
])

def test_convert(text_input, expected_output) -> None:
    assert count(text_input) == expected_output
