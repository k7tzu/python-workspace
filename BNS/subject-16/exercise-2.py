def echange(tab, i, j):
    '''Echange les éléments d'indice i et j dans le tableau tab.'''
    temp = tab[i]
    tab[i] = tab[j]
    tab[j] = temp

def tri_bulles(tab):
    '''Trie le tableau tab dans l'ordre croissant
    par la méthode du tri à bulles.
    
    >>> tri_bulles(tab)
    >>> tab
    []
    >>> tri_bulles(tab2)
    >>> tab2
    [1, 2, 3, 3, 6, 7, 9]
    >>> tri_bulles(tab3)
    >>> tab3
    [3, 4, 7, 9]
    '''
    n = len(tab)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if tab[j] > tab[j + 1]:
                echange(tab, j, j + 1)

tab = []
tab2 = [9, 3, 7, 2, 3, 1, 6]
tab3 = [9, 7, 4, 3]

if __name__ == "__main__":
    import doctest
    doctest.testmod()