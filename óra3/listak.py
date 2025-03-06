a=[1,2,3,4,5]
b=[100,1,2,3,4]

#foreach ciklus pythonban
for n in a:
    print(n)

#list,str... nevet sosem szabad adni semmi objektunak,mert az eredeti objektumot elveszitjuk az összes metódusával...
#házi a lista metódusainak kigooglezása

li=[1,2,3,4,5,6,7,8]
print(2 in li) #kiirja hogy az ellem a listában van e booleannal

li.pop() #kiszedi vagy a beirt szamu indexu elemet,vagy ha üres akkor a legutolsó ellemet

li.insert(2,7) #beszurja a hetest a 2es pozira es az ott levo elemtol kezdve obbra tolja a listat

a.extend(b) #a ellemei utan b osszes ellemet egyenkent beszurja,mig az append egyben berakna a b-t mint egy listát

a.index(3) #visszadja a kért érték első előfordulási indexét a listában

a.remove(3) #törli az első ilyen ellemet

a.reverse() #megforditja az ellemet sorrendjét

#Házi hogy próbáljuk kia sortedet valamilyen stringgel.

max(li)

min(li)

sum(li)

li1=[2,2,2,2]

sum1=1
for n in li1:
    sum1=n*sum1

print(sum1)