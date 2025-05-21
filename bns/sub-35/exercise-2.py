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
    """
    >>> eval_expression([2, 3, '+', 5, '*'])
    25
    >>> eval_expression([1, 2, '+', 3, '*'])
    9
    >>> eval_expression([1, 2, 3, '+', '*'])
    5
    """
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
    return resultat

if __name__ == '__main__':
    import doctest
    doctest.testmod()