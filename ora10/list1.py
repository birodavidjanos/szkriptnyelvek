#!/usr/bin/env python3
# coding: utf-8

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# A magyar változatot készítette:
# Szathmáry László (jabba.laci@gmail.com)
# frissítés Python 3-ra: 2016.09.09.


# A. match_ends
# Bemenet: sztringek listája. Számoljuk meg, hogy a bemenetben
# hány olyan sztring van, melynek a hossza legalább 2 s az
# első karaktere egyezik az utolsó karakterével. A visszatérési
# érték ezen feltételeket kielégítő sztringek száma legyen.
# Megjegyzés: Pythonban inkrementálásra a ++ helyett a += operátort használjuk.
def match_ends(words):
    # TODO...
    return


# B. front_x
# Bemenet: sztringek listája. Egy olyan listával térjünk vissza,
# melyben a szavak rendezve vannak, viszont az 'x'-szel kezdődő szavak
# kerüljenek előre.
# Példa: ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] bemenet esetén
# az eredmény: ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].
# Tipp: használhatunk 2 listát is, melyeket külön-külön rendezünk, majd
#       egyesítjük őket.
def front_x(words):
    # TODO...
    return


# Egy egyszerű teszt fv. Kiírja az egyes fv.-ek visszaadott értékét, ill.
# azt is, hogy mit kellett volna visszaadniuk.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{p} got: {g}; expected: {e}'.format(p=prefix, g=got, e=expected))


# Ezt ne módosítsuk.
# A main() fv. meghívja a fenti fv.-eket különféle paraméterekkel,
# s a test() fv. segítségével megnézi, hogy az eredmények helyesek-e.
def main():
    print('match_ends')
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print()
    print('front_x')
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
         ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
         ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

#############################################################################

if __name__ == '__main__':
    main()