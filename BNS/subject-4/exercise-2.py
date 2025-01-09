def distance_carre(point1, point2):
    """
    Calcule et renvoie la distance au carre entre
    deux points.

    >>> distance_carre((1, 0), (5, 3))
    25
    >>> distance_carre((1, 0), (0, 1))
    2
    """
    return (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2

def point_le_plus_proche(depart, tab):
    """
    Renvoie les coordonnées du premier point du tableau tab se
    trouvant à la plus courte distance du point depart.

    >>> point_le_plus_proche((0, 0), [(7, 9), (2, 5), (5, 2)])
    (2, 5)
    >>> point_le_plus_proche((5, 2), [(7, 9), (2, 5), (5, 2)])
    (5, 2)
    """
    min_point = tab[0]
    min_dist = ...
    for i in range(1, len(tab)):
        if distance_carre(tab[i], depart) < ...:
            min_point = ...
            min_dist = ...
    return min_point

if __name__ == "__main__":
    import doctest
    doctest.testmod()