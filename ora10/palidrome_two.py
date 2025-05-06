def is_palindrome(n: int) -> bool:
    
    return str(n) == str(n)[::-1]

def is_binary_palindrome(n: int) -> bool:
    bin_repr: str = bin(n)[2:]  # bináris formátum, '0b' nélkül
    return bin_repr == bin_repr[::-1]

# A megfelelő számok összegének kiszámítása
total: int = sum(n for n in range(1, 1_000_000) if is_palindrome(n) and is_binary_palindrome(n))

print(total)  # A keresett összeg
