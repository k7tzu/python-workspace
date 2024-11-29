class Pile:
    def __init__(self):
        self.L = []
    def estVide(self):
        return self.L == []
    def depiler(self):
        assert not self.estVide()
        self.L.pop()
    def empiler(self, x):
        self.L.append(x)

p = Pile()
for i in range(5):
    p.empiler(2*i)
print(p.L)
a=p.depiler()
print(a)
print(p.L)
print(p.estVide())