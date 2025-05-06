class MyQueue:
    def __init__(self):
        """Inicializálja az üres sor két veremmel."""
        self.stack_in = []
        self.stack_out = []

    def append(self, elem):
        """Új elemet ad a sor végére."""
        self.stack_in.append(elem)

    def popleft(self):
        """Eltávolítja és visszaadja a sor elején lévő elemet. Ha üres, None-t ad vissza."""
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

        return self.stack_out.pop() if self.stack_out else None

    def is_empty(self):
        """Megnézi, hogy a sor üres-e."""
        return not self.stack_in and not self.stack_out

    def size(self):
        """Visszaadja a sor méretét."""
        return len(self.stack_in) + len(self.stack_out)

    def __str__(self):
        """Az objektum szöveges reprezentációja."""
        return "[" + " ".join(map(str, reversed(self.stack_out))) + " " + " ".join(map(str, self.stack_in)) + "]"


# Példa használat
q = MyQueue()
print(q)        # [

print(q.is_empty()) # True
q.append(1)
q.append(4)
q.append(5)
print(q)        # [1 4 5

print(q.size())  # 3
print(q.is_empty())  # False

x = q.popleft()
print(x)        # 1
print(q)        # [4 5

q.popleft()
q.popleft()     # most már üres
x = q.popleft()
print(x)        # None (üres sorból próbálunk kivenni)
