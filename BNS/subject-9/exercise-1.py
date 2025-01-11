def effectif_notes(notes_eval):
    """
    >>> effectif_notes([2, 0, 5, 9, 6, 9, 10, 5, 7, 9, 9, 5, 0, 9, 6, 5, 4])
    [2, 0, 1, 0, 1, 4, 2, 1, 0, 5, 1]
    """
    result = [0] * 11
    for note in notes_eval:
        result[note] += 1
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()