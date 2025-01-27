class Region:
    def __init__(self, nom_region):
        self.nom = nom_region
        self.tab_voisines = []
        self.tab_couleurs_disponibles = ['Rouge', 'Vert', 'Bleu', 'Jaune', 'Orange', 'Marron']
        self.couleur_attribuee = None

    def renvoie_premiere_couleur_disponible(self):
        couleurs_utilisees = {voisine.couleur_attribuee for voisine in self.tab_voisines if voisine.couleur_attribuee}
        for couleur in self.tab_couleurs_disponibles:
            if couleur not in couleurs_utilisees:
                return couleur
        return None

    def renvoie_nb_voisines(self):
        return len(self.tab_voisines)

    def est_coloriee(self):
        return self.couleur_attribuee is not None

    def retire_couleur(self, couleur):
        if couleur in self.tab_couleurs_disponibles:
            self.tab_couleurs_disponibles.remove(couleur)

    def est_voisine(self, region):
        return region in self.tab_voisines


class Pays:
    def __init__(self):
        self.tab_regions = [aqui, occi, paca, auvergne, ile, hauts, ge, bre, norm, loire, centre, bourg, corse]

    def renvoie_tab_regions_non_coloriees(self):
        return [region for region in self.tab_regions if not region.est_coloriee()]

    def renvoie_max(self):
        nb_voisines_max = -1
        region_max = None
        for reg in self.renvoie_tab_regions_non_coloriees():
            if reg.renvoie_nb_voisines() > nb_voisines_max:
                nb_voisines_max = reg.renvoie_nb_voisines()
                region_max = reg
        return region_max

    def colorie(self):
        while self.renvoie_tab_regions_non_coloriees():
            region = self.renvoie_max()
            if region:
                couleur = region.renvoie_premiere_couleur_disponible()
                if couleur:
                    region.couleur_attribuee = couleur


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

France = Pays()
France.colorie()

for r in France.tab_regions:
    print(r.nom, "->", r.couleur_attribuee)
