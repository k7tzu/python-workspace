def annee_temperature_minimale(t_moy, annees):
    """
    >>> annee_temperature_minimale(temp, years)
    (12.5, 2016)
    """
    mini = t_moy[0]
    date_mini = annees[0]
    for i in range(1, len(t_moy)):
        if t_moy[i] < mini:
            mini = t_moy[i]
            date_mini = annees[i]
    return (mini, date_mini)

temp = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
years = [2013, 2014, 2015, 2016, 2017, 2018, 2019]

if __name__ == '__main__':
    import doctest
    doctest.testmod()