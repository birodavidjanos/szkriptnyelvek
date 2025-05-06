def mix_up(a: str, b: str) -> str:
    return f"{b[:2]}{a[2:]} {a[:2]}{b[2:]}"