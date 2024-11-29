from tree import a

def prefixe(tree):
    if tree is None:
        return
    print(tree.data, end='-')
    prefixe(tree.left)
    prefixe(tree.right)

prefixe(a)