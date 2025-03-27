#lista rendezése halmazba ajd duplikációk eltávolítása
lista=[5, 2, 3, 5, 1, 4, -200, 5, 1, 3, 2, 2, 5]
halmaz=set(lista)
print(sorted(halmaz))

#halmazműveletek

#listabol set
a=["alma","banan","citrom"]
a=set(a)

#üres halmaz
b=set()
#tipus
type(b)
#hozzáadás
b.add("narancs")
b.add("banan")
#hossz
print(len(b))

#unió-uj halmazt ad vissza [alma banan citrom narancs]
a.union(b) 
#metszet-közös ellem [banan]
a.intersection(b)
#a-b [citrom alma]
a.difference(b)

#törlés
a.remove("banan")

#nincsenek halmazban duplikátumok, és nem is indexelhető,de azért jó mert nincsenek benne duplikátumok

'''
    Dictionaryk
Kulcs érték párokkal rendelkező szótár.
len(d)=hossza
d['b'] visszaadja a "b" kulcs értékét
d['b']='BETA' átirja a b kulcs értékét BETA-ra
d.get('x', "NOT FOUND") -visszaadjax értékét,ha nincs benne akkor pedig a NOT FOUND-ot

'''
d={
    'a':"alfa",
    'b':"BETA",
    'g':"gamma",
    'o':"omega",
    'd':"delta"
}

#szép kiiratás
for k in sorted(d.keys()):
    print(k,"->",d[k])

for k,v in sorted(d.items()):
    print(k,"->",v)    