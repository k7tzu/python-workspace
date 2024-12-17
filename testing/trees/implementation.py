class Tree:
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

a = Tree(9)
a.left = Tree(8)
a.right = Tree(7)
a.left.left = Tree(6)
a.left.right = Tree(2)
a.right.right = Tree(5)
a.left.right.left = Tree(1)
a.right.right.left = Tree(4)
a.right.right.right = Tree(3)