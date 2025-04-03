def kiralyno_rajzolas(kiralyno_lista):
    meret = 8
    print("+-----------------+")
    
    for sor in range(meret):
        sor_str = "|"
        for oszlop in range(meret):
            if kiralyno_lista[oszlop] == sor:
                sor_str += " Q"
            else:
                sor_str += " ."
        sor_str += " |"
        print(sor_str)
    
    print("+-----------------+")

def main():
    kiralyno_lista = [0, 4, 7, 5, 2, 6, 1, 3]
    kiralyno_rajzolas(kiralyno_lista)

if __name__ == "__main__":
    main()
