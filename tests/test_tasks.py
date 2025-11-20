import pytest
from tasks import add
from _types import AddableT


@pytest.mark.parametrize(
    ["a", "b", "expected"],
    [
        (1, 2, 3),
        (2.5, 3.5, 6.0),
        ("Hello, ", "World!", "Hello, World!"),
        ([1, 2], [3, 4], [1, 2, 3, 4]),
    ],
)
def test_add(a: AddableT, b: AddableT, expected: AddableT):
    result = add.delay(a, b)
    assert result.get(timeout=10) == expected
