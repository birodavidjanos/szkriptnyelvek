def main():
    #1.
    szamok=list(range(19,106))
    szamok1=[szam*szam for szam in szamok if szam//21==0]
    print(szamok1)

    #2.
    adatok=["Adam,21","Bela,23","Cecil,21"]
    adatok1=[tuple(adat.split(",")) for adat in adatok]
    print(adatok1)

    #3.
    adatok=["Adam","5","2b","11"]
    adatok1=[adat for adat in adatok if adat.isdigit()]
    print(adatok1)

    #4.
    szotar = {3: "három", 5: "öt", 7: "hét"}
    lista = [f"{kulcs} betűvel kiírva: {ertek}" for kulcs, ertek in szotar.items()]
    print(lista)

    #5.
    szamok=list(range(0,61))
    lista=[szam for szam in szamok if szam%12==0 or str(szam)[-1]=="0"]
    print(lista)

    #6
    szotar={(1,2):"start",(2,2):"akadaly",(2,1):"akadaly",(0,2):"cel"}
    lista=[kulcs for kulcs,ertek in szotar.items() if ertek=="akadaly"]
    print(lista)
main()