def maximum_tableau(tab):
    """
    >>> maximum_tableau([98, 12, 104, 23, 131, 9])
    131
    >>> maximum_tableau([-27, 24, -3, 15])
    24
    """
    maxi = tab[0]
    for i in range(len(tab)):
        if tab[i] > maxi:
            maxi = tab[i]
    return maxi

if __name__ == "__main__":
    import doctest
    doctest.testmod()