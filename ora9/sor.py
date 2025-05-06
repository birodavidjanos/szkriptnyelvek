class Sor:
    def __init__(self):
        """Inicializálja az üres sort."""
        self.elemek = []

    def __str__(self):
        """Az objektum szöveges reprezentációja."""
        return "[" + " ".join(map(str, self.elemek))

    def ures(self):
        """Megnézi, hogy a sor üres-e."""
        return len(self.elemek) == 0

    def betesz(self, elem):
        """Új elemet tesz a sor végére."""
        self.elemek.append(elem)

    def meret(self):
        """Visszaadja a sor méretét."""
        return len(self.elemek)

    def kivesz(self):
        """Eltávolítja és visszaadja a sor elején lévő elemet. Ha üres, None-t ad vissza."""
        if self.ures():
            return None
        return self.elemek.pop(0)


# Példa használat
s = Sor()
print(s)
print(s.ures())
s.betesz(1)
s.betesz(4)
s.betesz(5)
print(s)
print(s.meret())
print(s.ures())
x = s.kivesz()
print(x)
print(s)
s.kivesz()
s.kivesz()
x = s.kivesz()
print(x)
