def ligne_suivante(ligne):
    ligne_suiv = [1]
    for i in range(len(ligne)-1):
        ligne_suiv.append(ligne[i] + ligne[i+1])
    ligne_suiv.append(1)
    return ligne_suiv

def pascal(n):
    triangle = [ [1] ]
    for k in range(n):
        ligne_k = ligne_suivante(triangle[-1])
        triangle.append(ligne_k)
    return triangle

print(ligne_suivante([1, 3, 3, 1]))
print(pascal(3))