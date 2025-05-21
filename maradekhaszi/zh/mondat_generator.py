import json
import random


def main():
    try:
        with open("szavak.json", "r", encoding="utf-8") as file:
            adatok = json.load(file)  # Helyes fájlbeolvasás
        print(adatok)
    except FileNotFoundError:
        print("Hiba: A 'szavak.json' fájl nem található.")
    except json.JSONDecodeError:
        print("Hiba: A fájl nem megfelelő JSON formátumú.")


    nevek=adatok["nevek"]
    igek=adatok["igek"]
    
    randomnev=random.randint(0,len(nevek)-1)
    randomige=random.randint(0,len(igek)-1)

    print(nevek[randomnev]+' '+igek[randomige]+'.')


if __name__ == '__main__':
    main()