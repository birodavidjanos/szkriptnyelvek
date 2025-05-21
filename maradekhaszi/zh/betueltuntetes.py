import sys

def main():
    if len(sys.argv) != 3:
        print("Hibás bemenet! Használat: python script.py <szó> <cserebetűk>")
        return
    
    szo = list(sys.argv[1])  # String listává alakítása
    betuk = sys.argv[2]      # Betűk, amelyeket ki kell cserélni "*"-ra
    
    for i in range(len(szo)):
        if szo[i] in betuk:
            szo[i] = "*"  # Cseréljük ki a karaktert "*"-ra
    
    print("".join(szo))  # Visszaalakítás stringgé és kiírás

main()
