from implementation import Tree

a = Tree(9)
a.left = Tree(8)
a.right = Tree(7)
a.left.left = Tree(6)
a.left.right = Tree(2)
a.right.right = Tree(5)
a.left.right.left = Tree(1)
a.right.right.left = Tree(4)
a.right.right.right = Tree(3)