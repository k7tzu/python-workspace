class Expr:
    def __init__(self, g, v, d):
        self.gauche = g
        self.valeur = v
        self.droite = d
    
    def est_une_feuille(self):
        return self.gauche is None and self.droite is None
    
    def infixe(self):
        """
        >>> a.infixe()
        '(1+2)'
        >>> b.infixe()
        '((1+2)*(3+4))'
        >>> e.infixe()
        '((3*(8+7))-(2+1))'
        """
        s = ''
        if self.gauche is not None:
            s = s + '(' + self.gauche.infixe()
        s = s + str(self.valeur)
        if self.droite is not None:
            s = s + self.droite.infixe() + ')'
        return s
    
a = Expr(Expr(None, 1, None), '+', Expr(None, 2, None))

b = Expr(Expr(Expr(None, 1, None), '+', Expr(None, 2, None)),
    '*', Expr(Expr(None, 3, None), '+', Expr(None, 4, None)))

e = Expr(
    Expr(Expr(None, 3, None), '*', Expr(Expr(None, 8, None),
        '+', Expr(None, 7, None))),
    '-', Expr(Expr(None, 2, None), '+', Expr(None, 1, None)))

if __name__ == '__main__':
    import doctest
    doctest.testmod()