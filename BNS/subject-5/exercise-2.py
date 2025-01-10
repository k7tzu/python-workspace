def est_un_ordre(tab):
    '''
    Renvoie True si tab est de longueur n et contient tous les
    entiers de 1 à n, False sinon

    >>> est_un_ordre([1, 6, 2, 8, 3, 7])
    False
    >>> est_un_ordre([5, 4, 3, 6, 7, 2, 1, 8, 9])
    True

    '''
    n = len(tab)
    # les entiers vus lors du parcours
    vus = []

    for x in tab:
        if x < 1 or x > n or x in vus:
            return False
        vus.append(x)
    return True

def nombre_points_rupture(ordre):
    '''
    Renvoie le nombre de point de rupture de ordre qui représente
    un ordre de gènes de chromosome

    >>> nombre_points_rupture([5, 4, 3, 6, 7, 2, 1, 8, 9])
    4
    >>> nombre_points_rupture([1, 2, 3, 4, 5])
    0
    >>> nombre_points_rupture([1, 6, 2, 8, 3, 7, 4, 5])
    7
    >>> nombre_points_rupture([2, 1, 3, 4])
    2
    '''
    # on vérifie que ordre est un ordre de gènes
    assert est_un_ordre(ordre)
    n = len(ordre)
    nb = 0
    if ordre[0] != 1: # le premier n'est pas 1
        nb = nb + 1
    i = 0
    while i < n - 1:
        if ordre[i + 1] - ordre[i] not in [-1, 1]: # l'écart n'est pas 1
            nb = nb + 1
        i = i + 1    
    if ordre[i] != n: # le dernier n'est pas n
        nb = nb + 1
    return nb

if __name__ == "__main__":
    import doctest
    doctest.testmod()