def megh(words):
    MELY_MGHK = 'aáoóuú'
    MAGAS_MGHK = 'eéiíöőüű'


    for szo in words:
        mely=0
        magas=0
        for betu in MELY_MGHK:
            for szobetu in szo:
                if betu==szobetu:
                    mely+=1
        for betu1 in MAGAS_MGHK:
            for szobetu in szo:
                if betu1==szobetu:
                    magas+=1
        if mely>0 and magas>0:
            print(szo,"-->vegyes" )
        elif magas>0:
            print(szo,"-->magas" )
        elif mely>0:
            print(szo,"-->mély" )
        elif mely==0 and magas==0:
            print(szo+"-->semmilyen" )

def main():
    MELY_MGHK = 'aáoóuú'
    MAGAS_MGHK = 'eéiíöőüű'
    words = ["ablak", "erkély", "kisvasút", "magas", "mély","Pffff"]
    megh(words)


if __name__ == "__main__":
    main()