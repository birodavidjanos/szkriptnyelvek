import math

class Ellipse:
    def __init__(self, a, b):
        """Inicializálja az ellipszist a főtengelyek hosszával."""
        self.a = a  
        self.b = b  

    def area(self):
        """Az ellipszis területének kiszámítása."""
        return math.pi * self.a * self.b

    def __str__(self):
        """Az objektum szöveges reprezentációja."""
        return f"Ellipse(a={self.a}, b={self.b}, area={self.area():.2f})"


class Sphere:
    def __init__(self, r):
        """Inicializálja a gömböt a sugarával."""
        self.r = r

    def volume(self):
        """A gömb térfogatának kiszámítása."""
        return (4/3) * math.pi * self.r**3

    def __str__(self):
        """Az objektum szöveges reprezentációja."""
        return f"Sphere(r={self.r}, volume={self.volume():.2f})"

    
    def __lt__(self, other):
        return self.volume() < other.volume()

    def __le__(self, other):
        return self.volume() <= other.volume()

    def __gt__(self, other):
        return self.volume() > other.volume()

    def __ge__(self, other):
        return self.volume() >= other.volume()



e = Ellipse(5, 3)
print(e)  

s1 = Sphere(3)
s2 = Sphere(5)

print(s1)  
print(s2)

print(s1 < s2)  
print(s1 <= s2) 
print(s1 > s2)  
print(s1 >= s2) 