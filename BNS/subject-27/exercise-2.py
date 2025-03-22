def colore_comp1(M, i, j, val):
    """
    >>> colore_comp1(M, 2, 1, 3)
    >>> M
    [[0, 0, 1, 0], [0, 3, 0, 1], [3, 3, 3, 0], [0, 3, 3, 0]]
    """
    if M[i][j] != 1:
        return
    
    M[i][j] = val

    if i-1 >= 0:
        colore_comp1(M, i-1, j, val)
    if i+1 < len(M):
        colore_comp1(M, i+1, j, val)
    if j-1 >= 0:
        colore_comp1(M, i, j-1, val)
    if j+1 < len(M):
        colore_comp1(M, i, j+1, val)

M = [[0, 0, 1, 0], [0, 1, 0, 1], [1, 1, 1, 0], [0, 1, 1, 0]]

if __name__ == '__main__':
    import doctest
    doctest.testmod()