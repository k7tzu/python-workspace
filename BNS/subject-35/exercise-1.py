t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]

def annee_temperature_minimale(t_moy, annees):
    """
    >>> annee_temperature_minimale(t_moy, annees)
    (12.5, 2016)
    """
    t_moy_min = t_moy[0]
    annees_min = annees[0]
    for i in range(len(annees)):
        if t_moy[i] < t_moy_min:
            t_moy_min = t_moy[i]
            annees_min = annees[i]
    return t_moy_min, annees_min

if __name__ == "__main__":
    import doctest
    doctest.testmod()