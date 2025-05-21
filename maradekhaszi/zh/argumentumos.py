import sys

def main():
    hossz=len(sys.argv)
    szavak=[]
    szamok=[]

    if (hossz-1)%2>0:
        print("Páros számu argumentumokat adj meg")
    else:

        for i in range(1,hossz,2):
            szavak.append(sys.argv[i])

        for j in range(2,hossz,2):
            szamok.append(int(sys.argv[j]))

        
        for i in range(0,len(szavak)):
            if szamok[i]>=0 and szamok[i]<len(szavak[i]):
                print(szavak[i][szamok[i]],end="")

main()