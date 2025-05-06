import pytest
from string_utils import mix_up

@pytest.mark.parametrize("a, b, expected", [
    ("mix", "pod", "pox mid"),
    ("dog", "dinner", "dig donner"),
    ("gnash", "sport", "spash gnort"),
    ("pezzy", "firm", "fizzy perm"),
])
def test_mix_up(a: str, b: str, expected: str) -> None:
   
    assert mix_up(a, b) == expected