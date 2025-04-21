def crible(n):
    """
    >>> crible(40)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    >>> crible(5)
    [2, 3]
    """
    premiers = []
    tab = [True] * n
    tab[0], tab[1] = False, False
    for i in range(n):
        if tab[i]:
            premiers.append(i)
            multiple = i
            while multiple < n:
                tab[multiple] = False
                multiple = multiple + i
    return premiers

if __name__ == '__main__':
    import doctest
    doctest.testmod()