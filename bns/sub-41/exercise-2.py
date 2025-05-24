class Carre:
    def __init__(self, liste, n):
        self.ordre = n
        self.tableau = [[liste[i + j * n] for i in range(n)]
                        for j in range(n)]
        
    def affiche(self):
        for i in range(self.ordre):
            print(self.tableau[i])

    def somme_ligne(self, i):
        somme = 0

        for j in range(self.ordre):
            somme = somme + self.tableau[i][j]
        return somme
    
    def somme_col(self, j):
        somme = 0

        for i in range(self.ordre):
            somme = somme + self.tableau[i][j]
        return somme
    
    def est_semimagique(self):
        s = self.somme_ligne(0)
        for i in range(self.ordre):
            if self.somme_ligne(i) != s:
                return False
            
        for j in range(self.ordre):
            if self.somme_col(j) != s:
                return False
            
        return True

lst_c2 = [1, 7, 7, 1]
c2 = Carre(lst_c2, 2)
c2.affiche()
print(c2.est_semimagique())

lst_c3 = [3, 4, 5, 4, 4, 4, 5, 4, 3]
c3 = Carre(lst_c3, 3)
c3.affiche()
print(c3.est_semimagique())

lst_c3bis = [2, 7, 6, 9, 0, 1, 4, 3, 8]
c3bis = Carre(lst_c3bis, 3)
c3bis.affiche()
print(c3bis.est_semimagique())