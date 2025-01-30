def multiplication(chiffre1, chiffre2):
    if chiffre1 < 0:
        return -multiplication(-chiffre1, chiffre2)
    if chiffre2 < 0:
        return -multiplication(chiffre1, -chiffre2)
    resultat = 0
    for i in range(chiffre2):
        resultat += chiffre1
    return resultat
print(multiplication(3, 5))
print(multiplication(-4, -8))
print(multiplication(-2, 6))
print(multiplication(-2, 0))


def chercher(tab, x, i, j):
    '''Renvoie l'indice de x dans tab, si x est dans tab, 
    None sinon.
    On suppose que tab est trié dans l'ordre croissant.'''
    if i > j:
        return None
    m = (i + j) // 2 
    if tab[m] < x: 
        return chercher(tab, x, m+1 , j) 
    elif tab[m] > x:
        return chercher(tab, x, i , m-1) 
    else:
        return m
chercher([1, 5, 6, 6, 9, 12], 7, 0, 10)
chercher([1, 5, 6, 6, 9, 12], 7, 0, 5)
chercher([1, 5, 6, 6, 9, 12], 9, 0, 5)
chercher([1, 5, 6, 6, 9, 12], 6, 0, 5)

#