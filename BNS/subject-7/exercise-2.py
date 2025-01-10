def tri_insertion(tab):
    '''
    Trie le tableau tab par ordre croissant
    en appliquant l'algorithme de tri par insertion.
    
    >>> tab = [98, 12, 104, 23, 131, 9]
    >>> tri_insertion(tab)
    >>> tab
    [9, 12, 23, 98, 104, 131]
    
    >>> tab = [3, 2, 1]
    >>> tri_insertion(tab)
    >>> tab
    [1, 2, 3]
    
    >>> tab = []
    >>> tri_insertion(tab)
    >>> tab
    []
    
    >>> tab = [5]
    >>> tri_insertion(tab)
    >>> tab
    [5]
    '''
    n = len(tab)
    for i in range(1, n):
        valeur_insertion = tab[i]
        # La variable j sert à déterminer où placer la valeur
        j = i
        # Décaler les valeurs vers la droite tant que la bonne position n'est pas trouvée
        while j > 0 and valeur_insertion < tab[j - 1]:
            tab[j] = tab[j - 1]
            j -= 1
        tab[j] = valeur_insertion

if __name__ == "__main__":
    import doctest
    doctest.testmod()
