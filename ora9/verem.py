class Verem:
    def __init__(self):
        """Inicializálja az üres veremet."""
        self.elemek = []

    def __str__(self):
        """Az objektum szöveges reprezentációja."""
        return "[" + " ".join(map(str, self.elemek))

    def ures(self):
        """Megnézi, hogy a verem üres-e."""
        return len(self.elemek) == 0

    def betesz(self, elem):
        """Új elemet tesz a verembe."""
        self.elemek.append(elem)

    def meret(self):
        """Visszaadja a verem méretét."""
        return len(self.elemek)

    def kivesz(self):
        """Eltávolítja és visszaadja a verem tetején lévő elemet. Ha üres, None-t ad vissza."""
        if self.ures():
            return None
        return self.elemek.pop()


# Példa használat
v = Verem()     
print(v)        # [
print(v.ures()) # True
v.betesz(1)
v.betesz(4)
v.betesz(5)
print(v)        # [1 4 5
print(v.meret()) # 3
print(v.ures())  # False
x = v.kivesz()
print(x)        # 5
print(v)        # [1 4
v.kivesz()
v.kivesz()      # most már üres
x = v.kivesz()
print(x)        # None
