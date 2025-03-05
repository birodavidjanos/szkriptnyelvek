import sys

def sum_from_args():
    if len(sys.argv) != 3:  # Az első elem a fájlnév, ezért 3 elem kell,run->C:\Users\Intel\.vscode\hazi1>python3 ket_szam_osszege_arg.py 1 2
                            #dir listazza a fajlokat cmd-ben
        print("Hiba! Két egész számot kell megadni parancssori argumentumként.")
        return
    
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        print("Összeg:", a + b)
    except ValueError:
        print("Hiba! Kérlek, egész számokat adj meg.")


if __name__ == "__main__":
    sum_from_args()


