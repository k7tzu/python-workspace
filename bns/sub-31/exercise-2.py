def parcours(adj, x, acc):
    if x not in acc:
        acc.append(x)
        for y in adj[x]:
            parcours(adj, y, acc)

def accessibles(adj, x):
    """
    >>> accessibles([[1, 2], [0, 3], [0], [1], [5], [4]], 0)
    [0, 1, 3, 2]
    >>> accessibles([[1, 2], [0, 3], [0], [1], [5], [4]], 4)
    [4, 5]
    """
    acc = []
    parcours(adj, x, acc)
    return acc

if __name__ == '__main__':
    import doctest
    doctest.testmod()