def renverse(pile):
    """
    >>> renverse([1, 2, 3, 4, 5])
    [5, 4, 3, 2, 1]
    """
    pile_inverse = []
    while pile != []:
        pile_inverse.append(pile.pop())
    return pile_inverse

def positifs(pile):
    """
    >>> positifs([-1, 0, 5, -3, 4, -6, 10, 9, -8])
    [0, 5, 4, 10, 9]
    >>> positifs([-2])
    []
    """
    pile_positifs = []
    while pile != []:
        value = pile.pop()
        if value >= 0:
            pile_positifs.append(value)
    return renverse(pile_positifs)

if __name__ == '__main__':
    import doctest
    doctest.testmod()