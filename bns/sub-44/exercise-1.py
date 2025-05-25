def moyenne(notes):
    """
    >>> moyenne([(8, 2), (12, 0), (13.5, 1), (5, 0.5)])
    9.142857142857142
    >>> moyenne([(3, 0), (5, 0)]) # Cet appel renvoie None
    """
    somme_notes = 0
    somme_coefs = 0
    for note, coefficient in notes:
        somme_notes += note * coefficient
        somme_coefs += coefficient
    if somme_coefs == 0:
        return None
    return somme_notes / somme_coefs

if __name__ == '__main__':
    import doctest
    doctest.testmod()