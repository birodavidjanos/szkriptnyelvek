import csv

def main():
    adatok = [("Győr", 23, "napos"), ("Pécs", 21, "esik"), ("Zápszony", 10, "napos")]
    
    # Szűrt lista létrehozása
    lista = [adat for adat in adatok if int(adat[1]) > 11]

    # CSV fájlba írás
    with open("időjárás.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Város", "Hőmérséklet", "Időjárás"])  # Fejléc
        writer.writerows(lista)  # Adatok beírása

    print("Az adatok sikeresen kiírva az 'időjárás.csv' fájlba.")

main()

import csv

def main():
    adatok = [("Győr", 23, "napos"), ("Pécs", 21, "esik"), ("Zápszony", 10, "napos")]
    
    # Szűrt lista létrehozása
    lista = [adat for adat in adatok if int(adat[1]) > 11]

    # CSV fájlba írás
    with open("időjárás.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Város", "Hőmérséklet", "Időjárás"])  # Fejléc
        writer.writerows(lista)  # Adatok beírása

    print("Az adatok sikeresen kiírva az 'időjárás.csv' fájlba.")

main()

import csv

def main():
    adatok = [("Győr", 23, "napos"), ("Pécs", 21, "esik"), ("Zápszony", 10, "napos")]
    
    # Szűrt lista létrehozása
    lista = [adat for adat in adatok if int(adat[1]) > 11]

    # CSV fájlba írás
    with open("időjárás.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Város", "Hőmérséklet", "Időjárás"])  # Fejléc
        writer.writerows(lista)  # Adatok beírása

    print("Az adatok sikeresen kiírva az 'időjárás.csv' fájlba.")

main()

import csv

def main():
    adatok = [("Győr", 23, "napos"), ("Pécs", 21, "esik"), ("Zápszony", 10, "napos")]
    
    # Szűrt lista létrehozása
    lista = [adat for adat in adatok if int(adat[1]) > 11]

    # CSV fájlba írás
    with open("időjárás.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Város", "Hőmérséklet", "Időjárás"])  # Fejléc
        writer.writerows(lista)  # Adatok beírása

    print("Az adatok sikeresen kiírva az 'időjárás.csv' fájlba.")

main()







https://github.com/BAndris4/Szkriptnyelvek/

