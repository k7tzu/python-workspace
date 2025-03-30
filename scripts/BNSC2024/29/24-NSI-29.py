def moyenne(liste_notes):
    somme_notes = 0
    somme_coeffs = 0
    for devoir in liste_notes:
        note = devoir[0]
        coeff = devoir[1]
        somme_notes += note * coeff
        somme_coeffs += coeff
    return somme_notes / somme_coeffs

def ligne_suivante(ligne):
    '''Renvoie la ligne suivant ligne du triangle de Pascal'''
    ligne_suiv = [ligne[0]] 
    for i in range(1, len(ligne)): 
        ligne_suiv.append(ligne[i-1] + ligne[i]) 
    ligne_suiv.append(ligne[-1]) 
    return ligne_suiv

def pascal(n):
    '''Renvoie le triangle de Pascal de hauteur n'''
    triangle = [ [1] ]
    for k in range(n): 
        ligne_k = ligne_suivante(triangle[-1]) 
        triangle.append(ligne_k)
    return triangle