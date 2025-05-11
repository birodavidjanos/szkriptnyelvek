from itertools import combinations
import time


def prod(iterable):
    """Szorzat számítása."""
    result = 1
    for num in iterable:
        result *= num
    return result

def find_lotto_numbers():
    start_time = time.time()

    numbers = range(1, 46)  # 1-től 45-ig
    for combo in combinations(numbers, 6):  # Összes 6 elemű kombináció
        if sum(combo) == 90 and prod(combo) == 996300:  # Szűrés
            print("Nyerőszámok:", combo)
            break

    print(f"Futási idő: {time.time() - start_time:.4f} mp")



find_lotto_numbers()
