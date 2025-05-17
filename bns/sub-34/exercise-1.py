def tri_selection(tab):
    """
    >>> tri_selection(tab)
    [-9, 1, 6, 12, 52]
    """
    for i in range(len(tab)):
        mini = i
        for k in range(i+1, len(tab)):
            if tab[k] < tab[mini]:
                mini = k
        tab[mini], tab[i] = tab[i], tab[mini]
    return tab

tab = [1, 52, 6, -9, 12]

if __name__ == '__main__':
    import doctest
    doctest.testmod()