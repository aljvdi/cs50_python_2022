import pytest
from seasons import ConvertToDate

@pytest.mark.parametrize("dob_inp, expected_output", [
    ("1999-01-01", "Twelve million, eight hundred sixty-two thousand eighty minutes"),
    ("2005-06-21", "Nine million, four hundred fifty-nine thousand, three hundred sixty minutes"),
    ("200-WRONG-D3Y", None),
])

def test_convert(dob_inp, expected_output) -> None:
    if expected_output is None:
        with pytest.raises(SystemExit):
            ConvertToDate(dob_inp)
    else:
        assert ConvertToDate(dob_inp) == expected_output

