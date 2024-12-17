from queue import Queue

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
    
    def get_data(self):
        return self.data
    
a = Arbre(4)
a.left = Arbre(3)
a.right = Arbre(1)
a.right.left = Arbre(2)
a.right.right = Arbre(7)
a.left.left = Arbre(6)
a.right.right.left = Arbre(9)

def BFS(arbre):
    if arbre is None:
        return []
    
    file = Queue()
    file.put(arbre)
    result = []

    while not file.empty():
        current = file.get()
        if current:
            result.append(current.data)
            file.put(current.left)
            file.put(current.right)
    return result

print(BFS(a))

def infixe(arbre):
    if arbre is None:
        return
    infixe(arbre.left)
    print(arbre.data, end='-')
    infixe(arbre.right)

infixe(a)

a = Arbre(4)
a.set_left(Arbre(3))
a.set_right(Arbre(1))
a.get_right().set_left(Arbre(2))
a.get_right().set_right(Arbre(7))
a.get_left().set_left(Arbre(6))
a.get_right().get_right().set_left(Arbre(9))

print(a.get_right().get_left().get_data())

a = (2, (8, (6, (), ()), (9, (), ())), (1, (7, (), ()), ()))