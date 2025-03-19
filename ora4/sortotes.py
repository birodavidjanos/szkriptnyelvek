import sys
import random as r

UPTO = 100
LINE_LENGTH = 10  # Egy sor hossza

def main():
    for i in range(UPTO):
        print(r.randint(0, 9), end="")
        if (i + 1) % LINE_LENGTH == 0:  # Ha elérjük a 10 számjegyet
            print()  # Sortörés

if __name__ == "__main__":
    main()
