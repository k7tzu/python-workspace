def recherche_indices_classement(elt, tab):
    """
    >>> recherche_indices_classement(3, [1, 3, 4, 2, 4, 6, 3, 0])
    ([0, 3, 7], [1, 6], [2, 4, 5])
    >>> recherche_indices_classement(3, [1, 4, 2, 4, 6, 0])
    ([0, 2, 5], [], [1, 3, 4])
    >>> recherche_indices_classement(3, [1, 1, 1, 1])
    ([0, 1, 2, 3], [], [])
    >>> recherche_indices_classement(3, [])
    ([], [], [])
    """
    result = ([], [], [])
    for i in range(len(tab)):
        if tab[i] < elt:
            result[0].append(i)
        elif tab[i] == elt:
            result[1].append(i)
        else:
            result[2].append(i)
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()