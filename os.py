import os

def create_python_file(filename):
    if os.path.isfile(filename):
        print(f"Hiba: A(z) '{filename}' fájl már létezik.")
        return

    with open(filename, "w") as file:
        file.write("#!/usr/bin/env python3\n\n\n")
        file.write("def main():\n")
        file.write("    print('Py3')\n\n")
        file.write("##############################################################################\n\n")
        file.write('if __name__ == "__main__":\n')
        file.write("    main()\n")
    
    print(f"A(z) '{filename}' fájl sikeresen létrehozva.")

def menu():
    print("---------------------------")
    print("Create an empty source file")
    print("---------------------------")
    print("1) Python [py]")
    print("2) C      [c]")
    print("q) quit")
    print("> ", end="")
    return input()

def main():
    while True:
        choice = menu()
        if choice == "1":
            create_python_file("alap.py")
        elif choice == "2":
            print("C file támogatás még nincs megvalósítva.")
        elif choice.lower() == "q":
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás, próbáld újra.")

if __name__ == "__main__":
    main()
