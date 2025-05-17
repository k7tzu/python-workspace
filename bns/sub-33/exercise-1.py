def insertion_abr(a, cle):
    """
    >>> insertion_abr(abr1, 4)
    ((None, 0, None), 1, (None, 2, (None, 3, (None, 4, None))))
    >>> insertion_abr(abr1, -5)
    (((None, -5, None), 0, None), 1, (None, 2, (None, 3, None)))
    >>> insertion_abr(abr1, 2)
    ((None, 0, None), 1, (None, 2, (None, 3, None)))
    """
    if a is None:
        return (None, cle, None)
    elif cle > a[1]:
        return (a[0], a[1], insertion_abr(a[2], cle))
    elif cle < a[1]:
        return (insertion_abr(a[0], cle), a[1], a[2])
    return a

n0 = (None, 0, None)
n3 = (None, 3, None)
n2 = (None, 2, n3)
abr1 = (n0, 1, n2)

if __name__ == '__main__':
    import doctest
    doctest.testmod()