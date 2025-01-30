def max_dico(dico):
    cle_max = ''
    val_max = 0
    for cle in dico.keys():
        if dico[cle] > val_max:
            val_max = dico[cle]
            cle_max = cle
    return (cle_max, val_max)

class Pile:
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        return self.contenu == []

    def empiler(self, v):
        self.contenu.append(v)

    def depiler(self):
        assert not self.est_vide()
        return self.contenu.pop()

def eval_expression(tab):
    p = Pile()
    for element in tab:
        if element != '+' and element != '*':
            p.empiler(element)
        else:
            if element == '+':
                resultat = p.depiler() + p.depiler()
            else:
                resultat = p.depiler() * p.depiler()
            p.empiler(resultat)
    return p.depiler()


