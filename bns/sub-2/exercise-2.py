def est_un_ordre(tab):
    """
    >>> est_un_ordre([1, 6, 2, 8, 3, 7])
    False
    >>> est_un_ordre([5, 4, 3, 6, 7, 2, 1, 8, 9])
    True
    """
    n = len(tab)
    vus = []

    for x in tab:
        if x < 1 or x > n or x in vus:
            return False
        vus.append(x)
    return True

def nombre_points_rupture(ordre):
    """
    >>> nombre_points_rupture([5, 4, 3, 6, 7, 2, 1, 8, 9])
    4
    >>> nombre_points_rupture([1, 2, 3, 4, 5])
    0
    >>> nombre_points_rupture([1, 6, 2, 8, 3, 7, 4, 5])
    7
    >>> nombre_points_rupture([2, 1, 3, 4])
    2
    """
    assert est_un_ordre(ordre)
    n = len(ordre)
    nb = 0
    if ordre[0] != 1:
        nb = nb + 1
    i = 0
    while i < n - 1:
        if ordre[i+1] - ordre[i] not in [-1, 1]:
            nb = nb + 1
        i = i + 1
    if ordre[i] != n:
        nb = nb + 1
    return nb


if __name__ == '__main__':
    import doctest
    doctest.testmod()