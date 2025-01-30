def cadeau(a, b):
    if a == 0 and b == 0:
        return 0
    if a == 0 and b == 1:
        return 1
    if a == 1 and b == 0:
        return 1
    if a == 1 and b == 1:
        return 0
    
def ou_exclusif(tab1, tab2):
    resultat = []
    taille = len(tab1)
    for i in range(taille):
        resultat.append(cadeau(tab1[i],tab2[i]))
    return resultat


print(ou_exclusif([1, 0, 1, 0, 1, 1, 0, 1], [0, 1, 1, 1, 0, 1, 0, 0]))




class Carre:
    def __init__(self, liste, n):
        self.ordre = n
        self.tableau = [[liste[i + j * n] for i in range(n)] for j in range(n)]

    def affiche(self):
        '''Affiche un carré'''
        for i in range(self.ordre):
            print(self.tableau[i])

    def somme_ligne(self, i):
        '''Calcule la somme des valeurs de la ligne i'''
        somme = 0
        for j in range(self.ordre):
            somme = somme + self.tableau[i][j]
        return somme

    def somme_col(self, j):
        '''Calcule la somme des valeurs de la colonne j'''
        somme = 0
        for i in range(self.ordre):
            somme = somme + self.tableau[i][j]
        return somme

    def est_semimagique(self):
        s = self.somme_ligne(0)

        #test de la somme de chaque ligne
        for i in range(self.ordre):
            if self.somme_ligne(i) != s:
                return False

        #test de la somme de chaque colonne
        for j in range(self.ordre):
            if self.somme_col(j) != s:
                return False

        return True