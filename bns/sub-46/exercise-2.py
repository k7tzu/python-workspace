pieces = [1, 2, 5, 10, 20, 50, 100, 200]

def rendu_monnaie(somme_due, somme_versee):
    """
    >>> rendu_monnaie(700, 700)
    []
    >>> rendu_monnaie(102, 500)
    [200, 100, 50, 20, 20, 5, 2, 1]
    """
    rendu = []
    a_rendre = somme_versee - somme_due
    i = len(pieces) - 1
    while a_rendre > 0:
        while pieces[i] > a_rendre:
            i = i - 1
        rendu.append(pieces[i])
        a_rendre = a_rendre - pieces[i]
    return rendu

if __name__ == '__main__':
    import doctest
    doctest.testmod()