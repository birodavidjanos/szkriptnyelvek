import pytest
from list_utils import match_ends, front_x

@pytest.mark.parametrize("words, expected", [
    (['aba', 'xyz', 'aa', 'x', 'bbb'], 3),
    (['', 'x', 'xy', 'xyx', 'xx'], 2),
    (['aaa', 'be', 'abc', 'hello'], 1),
])
def test_match_ends(words: list[str], expected: int) -> None:
    """A match_ends függvény helyes működését ellenőrzi különböző bemenetekkel."""
    assert match_ends(words) == expected

@pytest.mark.parametrize("words, expected", [
    (['bbb', 'ccc', 'axx', 'xzz', 'xaa'], ['xaa', 'xzz', 'axx', 'bbb', 'ccc']),
    (['ccc', 'bbb', 'aaa', 'xcc', 'xaa'], ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']),
    (['mix', 'xyz', 'apple', 'xanadu', 'aardvark'], ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']),
])
def test_front_x(words: list[str], expected: list[str]) -> None:
    """A front_x függvény helyes működését ellenőrzi különböző bemenetekkel."""
    assert front_x(words) == expected
