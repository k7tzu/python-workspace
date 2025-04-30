romains = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

def traduire_romain(nombre):
    """
    >>> traduire_romain("XIV")
    14
    >>> traduire_romain("CXLII")
    142
    >>> traduire_romain("MMXXIV")
    2024
    """
    if len(nombre) == 1:
        return romains[nombre]
    elif romains[nombre[0]] >= romains[nombre[1]]:
        return romains[nombre[0]] + traduire_romain(nombre[1:])
    else:
        return traduire_romain(nombre[1:]) - romains[nombre[0]]
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()