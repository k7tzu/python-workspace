def effectif_notes(notes_eval):
    """
    >>> eff
    [2, 0, 1, 0, 1, 4, 2, 1, 0, 5, 1]
    """
    result = [0] * 11
    for note in notes_eval:
        result[note] += 1
    return result

def notes_triees(eff):
    """
    >>> notes_triees(eff)
    [0, 0, 2, 4, 5, 5, 5, 5, 6, 6, 7, 9, 9, 9, 9, 9, 10]
    """
    resultat = []
    for i in range(11):
        for _ in range(eff[i]):
            resultat.append(i)
    return resultat

notes_eval = [2, 0, 5, 9, 6, 9, 10, 5, 7, 9, 9, 5, 0, 9, 6, 5, 4]
eff = effectif_notes(notes_eval)

if __name__ == '__main__':
    import doctest
    doctest.testmod()