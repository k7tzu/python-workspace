class Noeud:
    def __init__(self, tache, indice):
        self.tache = tache
        self.indice = indice
        self.gauche = ABR()
        self.droite = ABR()

class ABR:
    def __init__(self):
        self.racine = None

    def est_vide(self):
        return self.racine == None

    def insere(self, nouveau_noeud):
        if self.est_vide():
            self.racine = nouveau_noeud
        elif self.racine.indice < nouveau_noeud.indice:
            self.racine.gauche.insere(nouveau_noeud)
        else:
            self.racine.droite.insere(nouveau_noeud)
    def est_present(self, indice_recherche):
        if self.racine.est_vide():
            return False
        if self.racine.indice == indice_recherche:
            return True
        if self.racine.indice < indice_recherche:
            return self.racine.gauche.est_present(self, indice_recherche)
        if self.racine.indice > indice_recherche:
            return self.racine.droite.est_present(self, indice_recherche)