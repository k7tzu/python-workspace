def enumere(tab):
    """
    >>> enumere([])
    {}
    >>> enumere([1, 2, 3])
    {1: [0], 2: [1], 3: [2]}
    >>> enumere([1, 1, 2, 3, 2, 1])
    {1: [0, 1, 5], 2: [2, 4], 3: [3]}
    """
    d = {}
    for i in range(len(tab)):
        if tab[i] not in d:
            d[tab[i]] = [i]
        else:
            d[tab[i]].append(i)
    return d

if __name__ == '__main__':
    import doctest
    doctest.testmod()