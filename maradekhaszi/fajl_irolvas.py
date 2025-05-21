import csv

def main():
    adatok=[("Győr",23,"napos"),("Pécs",21,"esik"),("Zápszony",10,"napos")]

    lista=[]
    for adat in adatok:
        if int(adat[1])>11:
            lista.append(adat)

    print(lista)

    with open("időjárás.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(lista)

    #esik
    for adat in adatok:
        if adat[2]=="esik":
            print(adat[0],end=" ")

    #atlag
    print()
    sum=0
    atlag=0
    for adat in adatok:
        sum+=adat[1]
    atlag=sum/len(adatok)
    print(atlag)

main()