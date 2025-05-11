class AdresseIP:
    def __init__(self, adresse):
        self.adresse = adresse

    def liste_octets(self):
        """
        >>> adresse1.liste_octets()
        [192, 168, 0, 1]
        """
        return [int(i) for i in self.adresse.split(".")]
    
    def est_reservee(self):
        """
        >>> adresse1.est_reservee()
        False
        >>> adresse3.est_reservee()
        True
        """
        reservees = ['192.168.0.0', '192.168.0.255']
        return self.adresse in reservees
    
    def adresse_suivante(self):
        """
        >>> adresse2.adresse_suivante().adresse
        '192.168.0.3'
        """
        octets = self.liste_octets()
        if octets[3] == 254:
            return None
        octet_nouveau = octets[3] + 1
        return AdresseIP('192.168.0.' + str(octet_nouveau))
    
adresse1 = AdresseIP('192.168.0.1')
adresse2 = AdresseIP('192.168.0.2')
adresse3 = AdresseIP('192.168.0.0')

if __name__ == '__main__':
    import doctest
    doctest.testmod()