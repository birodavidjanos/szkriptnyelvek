# D. mix_up
# Adott két bemeneti sztring, a és b. Adjunk vissza egyetlen sztringet,
# melyben a és b konkatenálva van úgy, hogy köztük egyetlen szóköz szerepel.
# Ezen túl cseréljük fel a két sztring első két karakterét az eredményben.
# Példa:
#   'mix', 'pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Feltételezhetjük, hogy a bemeneti sztringek hossza legalább 2.
def mix_up(a, b):
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
    print('donuts')
    # Minden egyes sor meghívja a donuts() fv.-t s összehasonlítja a visszaadott
    # értéket a várt eredménnyel.
    test(donuts(4), 'Fánkok száma: 4')
    test(donuts(9), 'Fánkok száma: 9')
    test(donuts(10), 'Fánkok száma: sok')
    test(donuts(99), 'Fánkok száma: sok')

    print()
    print('both_ends')
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')

    print()
    print('fix_start')
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print()
    print('mix_up')
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')

#############################################################################

if __name__ == '__main__':
    main()