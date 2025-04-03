#Normalize függvényem
def normalize(szo):
    return ''.join(szo.split()).lower()

#Triviális megoldás
def anagrammatriv(szo1, szo2):
    if sorted(normalize(szo1)) == sorted(normalize(szo2)):
        return print(szo1+" , "+szo2+" -> A két szó anagramma!")
    else:
        return print(szo1+" , "+szo2+" -> A két szó nem anagramma!")
    
#Nem triviális megoldás
def anagrammanemtriv(szo1, szo2):
    szo1 = normalize(szo1)
    szo2 = normalize(szo2)

    if len(szo1) != len(szo2):
        print("A két szó semmiféleképpen sem anagramma")
        return

    # Betűk számlálása szótár segítségével
    szotar1 = {}
    for betu in szo1:
        if betu in szotar1:
            szotar1[betu] += 1
        else:
            szotar1[betu] = 1

    szotar2 = {}
    for betu in szo2:
        if betu in szotar2:
            szotar2[betu] += 1
        else:
            szotar2[betu] = 1

    #Kiiratás
    print("Szó 1 betűi és gyakorisága:", szotar1)
    print("Szó 2 betűi és gyakorisága:", szotar2)
    if szotar1 == szotar2:
        print("A két szó anagramma!")
    else:
        print("A két szó nem anagramma.")

def main():
    anagrammatriv("szia", "aszi")
    anagrammanemtriv("szia", "kaki")

if __name__ == '__main__':
    main()
