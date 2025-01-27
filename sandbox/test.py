# Sujet Metropole 2023 J1 - Exercice 3
class Region:
    def __init__(self, nom_region):
        self.nom = nom_region
        self.tab_voisines = []
        self.tab_couleurs_disponibles = ['Rouge', 'Vert', 'Bleu', 'Jaune', 'Orange', 'Marron']
        self.couleur_attribuee = None
    def renvoie_premiere_couleur_disponible(self):
        return ...
    def renvoie_nb_voisines(self) :
        return ...
    def est_coloriee(self):
        return ...
    def retire_couleur(self, couleur):
        ...
    def est_voisine(self, region):
        ...

class Pays:
    def __init__(self):
        self.tab_regions = [aqui, occi, paca, auvergne, ile, hauts, ge, bre, norm, loire, centre, bourg, corse]
    def renvoie_tab_regions_non_coloriees(self):
        ...
    def renvoie_max(self):
        nb_voisines_max = -1
        region_max = None
        for reg in self.renvoie_tab_regions_non_coloriees():
            if reg.renvoie_nb_voisines() > nb_voisines_max:
                nb_voisines_max = reg.renvoie_nb_voisines()
                region_max = reg
        return region_max
    def colorie(self):
        ...

# instanciation des 13 régions
aqui = Region('Nouvelle-Aquitaine')
occi = Region('Occitanie')
paca = Region("Provence-Alpes-Côte-d-Azur")
auvergne = Region('Auvergne-Rhône-Alpes')
ile = Region('Ile-de-France')
hauts = Region('Hauts-De-France')
ge = Region('Grand-Est')
bre = Region('Bretagne')
norm = Region('Normandie')
loire = Region('Pays-De-La-Loire')
centre = Region('Centre-Val-De-Loire')
bourg = Region('Bourgogne-Franche-Comté')
corse = Region('Corse')

# affectations des régions voisines
aqui.tab_voisines = [loire, centre, auvergne, occi]
occi.tab_voisines = [aqui, auvergne, paca]
paca.tab_voisines = [occi, auvergne]
auvergne.tab_voisines = [paca, occi, aqui, bourg, centre]
ile.tab_voisines = [hauts, ge, bourg, centre, norm]
hauts.tab_voisines = [norm, ile, ge]
ge.tab_voisines = [hauts, ile, bourg]
bre.tab_voisines = [norm, loire]
norm.tab_voisines = [bre, loire, centre, ile, hauts]
loire.tab_voisines = [bre, norm, centre, aqui]
centre.tab_voisines = [ile, bourg, auvergne, aqui, loire, norm]
bourg.tab_voisines = [auvergne, ge, ile, centre]
corse.tab_voisines = []

# instanciation de la France
France = Pays()

# coloriage des régions
France.colorie()

# vérification des couples Région->Couleur
for r in France.tab_regions : 
    print(r.nom, "->", r.couleur_attribuee)



