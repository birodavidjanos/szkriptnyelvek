import sys

def draw_x(n):
    for i in range(n):
        row = [" "] * n
        row[i] = "x"
        row[n - 1 - i] = "x"
        print("".join(row))

def main():
    if len(sys.argv) < 2:
        return  # Nem írunk ki semmit, ha nincs paraméter
    
    try:
        n = int(sys.argv[1])
    except ValueError:
        return  # Nem egész szám esetén nem írunk ki semmit
    
    if n < 1:
        return  # Ha 1-nél kisebb számot adtak meg, nem írunk ki semmit

    draw_x(n)

if __name__ == "__main__":
    main()
