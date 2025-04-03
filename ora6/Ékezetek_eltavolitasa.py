TEXT = """A katalán zászló, a Senyera színeit fogja viselni a következő idény során a spanyol élvonalban szereplő FC Barcelona labdarúgócsapata.

A Marca című sportnapilap hétfői internetes kiadása szerint az együttes játékosai az idegenbeli mérkőzéseken húzzák majd magukra a sárga-piros csíkozású mezt - első ízben a klub történelme során.

A döntés várhatóan nem marad politikai visszhang nélkül Spanyolországban, tekintettel a katalán önállósodási törekvésekre."""

ékezetek = "áéíóöőúüűÁÉÍÓÖŐÚÜŰ"
nemÉkezet = "aeiooouuuAEIOOOUUU"

szotar = {}

szavak=TEXT.split()


for szo in szavak:
    új_szo=""
    for betu in szo:
        if betu in ékezetek:
            új_szo += nemÉkezet[ékezetek.index(betu)]
        else:
            új_szo += betu
    szotar[szo]=új_szo
    
for k,v in szotar.items():
    print(k,"->",v)   




'''
for karakter in TEXT:
    if karakter in ékezetek:
        új_TEXT += nemÉkezet[ékezetek.index(karakter)]
    else:
        új_TEXT += karakter

print(új_TEXT)
'''