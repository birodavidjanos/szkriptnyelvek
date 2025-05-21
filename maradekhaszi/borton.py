def main():


    hossz = 8  
    cellak = [0] * hossz  
    szotar = {'0': '1', '1': '0'}  
    print("Kezdeti állapot:", cellak)


    for i in range(1, hossz + 1):  
        for j in range(i - 1, hossz, i):  
            cellak[j] = int(szotar[str(cellak[j])])  

        print(f"{i}. lépés után:", cellak)  


    cellakszama=[]
    for i in range(0,hossz):
        if cellak[i]==1:
            cellakszama.append(i)

    print('A cellák szama: ',cellakszama)    


if __name__ == '__main__':
    main()
