#init
class Arbre:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def set_left(self, undertree):
        self.left = undertree

    def set_right(self, undertree):
        self.right = undertree

    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right

#arbre n°4
a = Arbre(5)
a.left = Arbre(2)
a.right = Arbre(7)
a.left.left = Arbre(0)
a.left.right = Arbre(3)
a.right.left = Arbre(6)
a.right.right = Arbre(8)

#arbre n°5
b = Arbre(3)
b.left = Arbre(2)
b.right = Arbre(5)
b.left.left = Arbre(1)
b.left.right = Arbre(9)
b.right.left = Arbre(4)
b.right.right = Arbre(6)

# parcours infixe (Don't ask y LMAO)
def infixe(arbre, s = None):
    if s is None:
        s = []
    if arbre is None:
        return
    infixe(arbre.left, s)
    s.append(arbre.data)
    infixe(arbre.right, s)
    return s

# Check if ABR or not
def est_abr(arbre):
    parcours = infixe(arbre)
    return parcours == sorted(parcours)

print(est_abr(a))
print(est_abr(b))