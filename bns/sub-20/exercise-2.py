class Carte:
    def __init__(self, c, v):
        self.couleur = c
        self.valeur = v
    
    def recuperer_valeur(self):
        valeurs = ['As','2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi']
        return valeurs[self.valeur - 1]
    
    def recuperer_couleur(self):
        couleurs = ['pique', 'coeur', 'carreau', 'trèfle']
        return couleurs[self.couleur - 1]

class Paquet_de_cartes:
    def __init__(self):
        self.contenu = []
        for c in range(1, 5):
            for v in range(1, 14):
                self.contenu.append(Carte(c, v))

    def recuperer_carte(self, pos):
        assert 0 <= pos <= 51, 'paramètre pos invalide'
        return self.contenu[pos]
    
p1 = Paquet_de_cartes()
cartes1= p1.recuperer_carte(42)
print(f"{cartes1.couleur},{cartes1.valeur}")