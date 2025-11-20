import pytest
from tasks import add


@pytest.mark.parametrize(
    ["a", "b", "expected"],
    [
        (1, 2, 3),
        (2.5, 3.5, 6.0),
        ("Hello, ", "World!", "Hello, World!"),
        ([1, 2], [3, 4], [1, 2, 3, 4]),
    ],
)
def test_add(a, b, expected):
    result = add.delay(a, b)
    assert result.get(timeout=10) == expected
