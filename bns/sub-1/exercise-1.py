def voisins_entrants(adj, x):
    """
    >>> voisins_entrants(adj_1, 0)
    [2, 3]
    """
    result = []
    for i in range(len(adj)):
        if x in adj[i]:
            result.append(i)
    return result

adj_1 = [[1, 2], [2], [0], [0]]

if __name__ == '__main__':
    import doctest
    doctest.testmod()