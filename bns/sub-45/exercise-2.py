def est_cyclique(plan):
    """
    >>> est_cyclique({'A':'E','F':'A','C':'D','E':'B','B':'F','D':'C'})
    False
    >>> est_cyclique({'A':'E','F':'C','C':'D','E':'B','B':'F','D':'A'})
    True
    >>> est_cyclique({'A':'B','F':'C','C':'D','E':'A','B':'F','D':'E'})
    True
    >>> est_cyclique({'A':'B','F':'A','C':'D','E':'C','B':'F','D':'E'})
    False
    """
    expediteur = 'A'
    destinataire = plan[expediteur]
    nb_destinataires = 1

    while destinataire != expediteur:
        destinataire = plan[destinataire]
        nb_destinataires += 1

    return nb_destinataires == len(plan)

if __name__ == '__main__':
    import doctest
    doctest.testmod()