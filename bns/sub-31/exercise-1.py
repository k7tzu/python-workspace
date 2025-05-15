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
    for i in range(len(texte) - len(motif) + 1):
        if texte[i:i + len(motif)] == motif:
            result.append(i)
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()