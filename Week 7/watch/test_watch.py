import pytest
from watch import parse

@pytest.mark.parametrize("html_input, expected_output", [
    ('<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>', 'xvFZjo5PgG0'),
    ("<if>WRONG</if>", None),
    ('<iframe src="http://youtube.com/embed/xvFZjo5PgG0"></iframe>', 'xvFZjo5PgG0')
])

def test_parse(html_input, expected_output) -> None:
    if expected_output == None:
        assert parse(html_input) == None
    else:
        assert parse(html_input) == f'https://youtu.be/{expected_output}'
