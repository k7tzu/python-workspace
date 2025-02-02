def tri(tab):
    '''tab est un tableau d'entiers contenant des 0 et des 1.
    La fonction trie ce tableau en plaçant tous les 0 à gauche

    >>> tri(tab)
    >>> tab
    [0, 0, 0, 0, 0, 1, 1, 1, 1]
    '''
    i = 0
    j = len(tab) -1
    while i < j:
        if tab[i] == 0:
            i = i + 1
        else:
            valeur = tab[j]
            tab[j] = tab[i]
            tab[i] = valeur
            j = j - 1

tab = [0,1,0,1,0,1,0,1,0]

if __name__ == "__main__":
    import doctest
    doctest.testmod()