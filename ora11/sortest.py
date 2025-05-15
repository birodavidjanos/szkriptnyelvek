import unittest

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

class TestSor(unittest.TestCase):
    def setUp(self):
        """Inicializálja a tesztpéldányt."""
        self.sor = Sor()

    def test_ures_sor(self):
        """Teszteli, hogy egy újonnan létrehozott sor üres-e."""
        self.assertTrue(self.sor.ures())
        self.assertEqual(self.sor.meret(), 0)

    def test_betesz(self):
        """Teszteli az elem hozzáadását a sorhoz."""
        self.sor.betesz(1)
        self.sor.betesz(4)
        self.assertFalse(self.sor.ures())
        self.assertEqual(self.sor.meret(), 2)

    def test_kivesz(self):
        """Teszteli az elem kivételét a sorból."""
        self.sor.betesz(1)
        self.sor.betesz(4)
        self.sor.betesz(5)
        self.assertEqual(self.sor.kivesz(), 1)
        self.assertEqual(self.sor.kivesz(), 4)
        self.assertEqual(self.sor.kivesz(), 5)
        self.assertTrue(self.sor.ures())

    def test_kivesz_ures_sorbol(self):
        """Teszteli, hogy üres sorból való kivétel None-t ad vissza."""
        self.assertIsNone(self.sor.kivesz())

if __name__ == "__main__":
    unittest.main()
