from enum import Enum
from typing import Optional

class Hangrend(Enum):
    """A magyar hangrend kategóriái."""
    MELYE = "mély"
    MAGAS = "magas"
    VEGYES = "vegyes"
    SEMMI = "semmilyen"

MELY_MGHK = "aáoóuú"
MAGAS_MGHK = "eéiíöőüű"

def hangrend(szo: str) -> Hangrend:
    """Eldönti egy magyar szó hangrendjét."""
    mely = any(char in MELY_MGHK for char in szo)
    magas = any(char in MAGAS_MGHK for char in szo)

    if mely and magas:
        return Hangrend.VEGYES
    elif mely:
        return Hangrend.MELYE
    elif magas:
        return Hangrend.MAGAS
    else:
        return Hangrend.SEMMI

# Példa használat
words = ["ablak", "erkély", "kisvasút", "magas", "mély", "Pfffffff"]
for word in words:
    print(f"{word} → {hangrend(word).value}")
