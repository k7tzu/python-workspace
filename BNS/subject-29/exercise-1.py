def moyenne(notes):
    """
    >>> moyenne([(15.0,2), (9.0,1), (12.0,3)])
    12.5
    """
    sm_notes = 0
    sm_coeff = 0
    for elt in notes:
        note = elt[0]
        coeff = elt[1]
        sm_notes += coeff * note
        sm_coeff += coeff
    return sm_notes / sm_coeff

if __name__ == '__main__':
    import doctest
    doctest.testmod()