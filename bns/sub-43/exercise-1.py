def couples_consecutifs(tab):
    """
    >>> couples_consecutifs([1, 4, 3, 5])
    []
    >>> couples_consecutifs([1, 4, 5, 3])
    [(4, 5)]
    >>> couples_consecutifs([1, 1, 2, 4])
    [(1, 2)]
    >>> couples_consecutifs([7, 1, 2, 5, 3, 4])
    [(1, 2), (3, 4)]
    >>> couples_consecutifs([5, 1, 2, 3, 8, -5, -4, 7])
    [(1, 2), (2, 3), (-5, -4)]
    """
    result = []
    for i in range(len(tab)-1):
        if tab[i+1] - tab[i] == 1:
            result.append((tab[i], tab[i+1]))
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()