import pytest
from working import convert


# NOTE: TBH, I gave this one to Chat GPT for optimisation, and I found a new way to write pytest
#       That was quite interesting :)

@pytest.mark.parametrize("time_input, expected_output", [
    ("9AM - 5PM", None),
    ("9 AM to 5 PM", "09:00 to 17:00"),
    ("9AM to 5PM", None),
    ("9:00 AM to 5:00 PM", "09:00 to 17:00"),
    ("10 PM to 8 AM", "22:00 to 08:00"),
    ("10:30 PM to 8:50 AM", "22:30 to 08:50"),
    ("8:60 AM to 4:60 PM", None)
])

def test_convert(time_input, expected_output) -> None:
    if expected_output is None:
        with pytest.raises(ValueError):
            convert(time_input)
    else:
        assert convert(time_input) == expected_output

