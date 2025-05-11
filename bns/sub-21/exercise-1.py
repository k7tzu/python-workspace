def indices_maxi(tab):
    """
    >>> indices_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8])
    (9, [3, 8])
    >>> indices_maxi([7])
    (7, [0])
    """
    maxi = tab[0]
    indices = []
    for i in range(len(tab)):
        if tab[i] > maxi:
            maxi = tab[i]
            indices = [i]
        elif tab[i] == maxi:
            indices.append(i)
    return (maxi, indices)

if __name__ == '__main__':
    import doctest
    doctest.testmod()