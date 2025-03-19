def main():
    negyzetosszeg=0
    osszegnegyzet=0
    for i in range(1,101):
        negyzetosszeg+=i**2
        osszegnegyzet+=i
    osszegnegyzet=osszegnegyzet**2
    print("Az első száz természetes szám összegének a négyzete és az első száz természetes szám négyzetösszege közti különbség: ",osszegnegyzet-negyzetosszeg)

if __name__ == "__main__":
    main()