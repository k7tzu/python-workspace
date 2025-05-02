def ligne_suivante(ligne):
    """
    >>> ligne_suivante([1, 3, 3, 1])
    [1, 4, 6, 4, 1]
    """
    ligne_suiv = [1]
    for i in range(len(ligne)-1):
        ligne_suiv.append(ligne[i] + ligne[i+1])
    ligne_suiv.append(1)
    return ligne_suiv

def pascal(n):
    """
    >>> pascal(2)
    [[1], [1, 1], [1, 2, 1]]
    >>> pascal(3)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    """
    triangle = [[1]]
    for k in range(n):
        ligne_k = ligne_suivante(triangle[k])
        triangle.append(ligne_k)
    return triangle

if __name__ == '__main__':
    import doctest
    doctest.testmod()