def moyenne(notes):
    """
    >>> moyenne([(8, 2), (12, 0), (13.5, 1), (5, 0.5)])
    9.142857142857142
    >>> moyenne([(3, 0), (5, 0)])
    """
    notes_sum = 0
    coef_sum = 0
    for note, coef in notes:
        notes_sum += note * coef
        coef_sum += coef

    if coef_sum == 0:
        return None
    
    return notes_sum / coef_sum

if __name__ == "__main__":
    import doctest
    doctest.testmod()