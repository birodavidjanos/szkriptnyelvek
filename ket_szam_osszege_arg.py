import sys

def sum_from_args():
    if len(sys.argv) != 3:  # Az első elem a fájlnév, ezért 3 elem kell
        print("Hiba! Két egész számot kell megadni parancssori argumentumként.")
        return
    
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        print("Összeg:", a + b)
    except ValueError:
        print("Hiba! Kérlek, egész számokat adj meg.")

# Ha ezt a fájlt futtatjuk parancssorból, akkor működik:
# python script.py 5 10  → Kiírja: Összeg: 15
if __name__ == "__main__":
    sum_from_args()
