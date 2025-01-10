def depouille(urne):
    """
    >>> depouille(['A', 'B', 'A'])
    {'A': 2, 'B': 1}
    >>> depouille([])
    {}
    >>> depouille(['A', 'A', 'A', 'B', 'C', 'B', 'C', 'B', 'C', 'B'])
    {'A': 3, 'B': 4, 'C': 3}
    """
    resultat = {}
    for bulletin in urne:
        if bulletin in resultat:
            resultat[bulletin] += 1
        else:
            resultat[bulletin] = 1
    return resultat

def vainqueurs(election):
    """
    >>> vainqueurs({'A': 3, 'B': 4, 'C': 3})
    ['B']
    >>> vainqueurs({'A': 2, 'B': 2, 'C': 1})
    ['A', 'B']
    """
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax:
            nmax = election[candidat]
    liste_finale = [nom for nom in election if election[nom] == nmax]
    return liste_finale

if __name__ == "__main__":
    import doctest
    doctest.testmod()
