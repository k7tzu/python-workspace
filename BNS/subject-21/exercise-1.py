def recherche_motif(motif, texte):
    """
    >>> recherche_motif("ab", "")
    []
    >>> recherche_motif("ab", "cdcdcdcd")
    []
    >>> recherche_motif("ab", "abracadabra")
    [0, 7]
    >>> recherche_motif("ab", "abracadabraab")
    [0, 7, 11]
    """
    result = []
    i = 0
    while i <= len(texte) - len(motif):
        j = 0
        while j < len(motif) and motif[j] == texte[j + i]:
            j += 1
        if j == len(motif):
            result.append(i)
        i += 1
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()