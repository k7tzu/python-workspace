def tri_selection(tab):
    """
    >>> tri_selection([1, 52, 6, -9, 12])
    [-9, 1, 6, 12, 52]
    """
    for i in range(len(tab)):
        min_index = i
        for j in range(i+1, len(tab)):
            if tab[j] < tab[min_index]:
                min_index = j
        tab[i], tab[min_index] = tab[min_index], tab[i]
    return tab

if __name__ == "__main__":
    import doctest
    doctest.testmod()