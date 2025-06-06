def recherche(a,tab):
    for i in range(len(tab)):
        if tab[i] == a:
            return i
    return False


def insere(tab, a):
    """
    Insère l'élément a (int) dans le tableau tab (list)
    trié par ordre croissant à sa place et renvoie le
    nouveau tableau.
    """
    tab_a = [ a ] + tab # nouveau tableau contenant a 
                        # suivi des éléments de tab
    i = 0
    while i < len(tab_a) - 1 and a > tab_a[i+1]: 
        tab_a[i] = tab_a[i+1] 
        tab_a[i+1] = a
        i = i + 1 
    return tab_a


