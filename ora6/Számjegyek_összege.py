def main():
    szam=2**1000
    szam=str(szam)
    hossz=len(szam)
    osszeg=0
    for i in range(0,hossz):
        osszeg+=int(szam[i])

    print(osszeg)

if __name__=='__main__':
    main()

    