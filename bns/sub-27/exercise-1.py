def verifie(tab):
    """
    >>> verifie([0, 5, 8, 8, 9])
    True
    >>> verifie([8, 12, 4])
    False
    >>> verifie([-1, 4])
    True
    >>> verifie([])
    True
    >>> verifie([5])
    True
    """
    for i in range(len(tab)-1):
        if tab[i] > tab[i+1]:
            return False
    return True

if __name__ == '__main__':
    import doctest
    doctest.testmod()