def depouille(urne):
    """
    >>> depouille([ 'A', 'B', 'A' ])
    {'A': 2, 'B': 1}
    >>> depouille([])
    {}
    """
    resultat = {}
    for bulletin in urne:
        if bulletin in resultat:
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin] = 1
    return resultat

def vainqueurs(election):
    """
    >>> election
    {'A': 3, 'B': 4, 'C': 3}
    >>> vainqueurs(election)
    ['B']
    >>> vainqueurs({ 'A' : 2, 'B' : 2, 'C' : 1})
    ['A', 'B']
    """
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax:
            nmax = election[candidat]
    liste_finale = [nom for nom in election if election[nom] == nmax]
    return liste_finale

urne = ['A', 'A', 'A', 'B', 'C', 'B', 'C', 'B', 'C', 'B']
election = depouille(['A', 'A', 'A', 'B', 'C', 'B', 'C', 'B', 'C', 'B'])

if __name__ == '__main__':
    import doctest
    doctest.testmod()