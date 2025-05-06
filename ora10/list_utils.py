from typing import List

def match_ends(words: List[str]) -> int:
    """Megszámolja, hány olyan szó van, amely legalább két karakter hosszú és az első betűje megegyezik az utolsóval."""
    return sum(1 for word in words if len(word) >= 2 and word[0] == word[-1])

def front_x(words: List[str]) -> List[str]:
    """Rendezi a szavakat úgy, hogy az 'x'-szel kezdődők kerüljenek előre."""
    x_words = sorted([word for word in words if word.startswith('x')])
    other_words = sorted([word for word in words if not word.startswith('x')])
    return x_words + other_words
