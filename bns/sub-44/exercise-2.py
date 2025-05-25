def affiche(dessin):
    for ligne in dessin:
        affichage = ''
        for col in ligne:
            if col == 1:
                affichage = affichage + "*"
            else:
                affichage = affichage + " "
        print(affichage)

def liste_zoom(liste_depart, k):
    liste_zoomee = []
    for elt in liste_depart:
        for i in range(k):
            liste_zoomee.append(elt)
    return liste_zoomee

def dessin_zoom(grille, k):
    grille_zoomee = []
    for ligne in grille:
        ligne_zoomee = liste_zoom(ligne, k)
        for i in range(k):
            grille_zoomee.append(ligne_zoomee)
    return grille_zoomee

coeur = [[0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
     [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
     [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
     [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
     [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]]

affiche(coeur)
affiche(dessin_zoom(coeur, 2))
print(liste_zoom([1, 2, 3], 3))