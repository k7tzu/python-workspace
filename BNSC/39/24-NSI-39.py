def recherche(elt, tab):
    for i in range(len(tab)-1, -1, -1):
        if tab[i] == elt:
            return i
    return None



class AdresseIP:
    def __init__(self, adresse):
        self.adresse = adresse 

    def liste_octets(self):
        return [int(i) for i in self.adresse.split(".")]

    def est_reservee(self):
        reservees = [ '192.168.0.0', '192.168.0.255' ] 
        return self.adresse in reservees 

    def adresse_suivante(self):
        octets = self.liste_octets() 
        if octets[3] == 254: 
            return None
        octet_nouveau = octets[3] + 1 
        return AdresseIP('192.168.0.' + str(octet_nouveau))

print(recherche(1, [10, 12, 1, 56]))
print(recherche(1, [2, 3, 4]))
print(recherche(1, [1, 0, 42, 7]))
print(recherche(1, [1, 50, 1]))
print(recherche(1, [8, 1, 10, 1, 7, 1, 8]))
adresse1=AdresseIP('192.168.0.1')
adresse2=AdresseIP('192.168.0.2')
adresse3=AdresseIP('192.168.0.0')
print(adresse1.liste_octets())
print(adresse2.liste_octets())
print(adresse3.liste_octets())
