t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]

def annee_temperature_minimale(releve, date):
    temp_mini = releve[0]
    date_mini = date[0]
    for i in range(len(releve)):
        if releve[i] < temp_mini:
            temp_mini = releve[i]
            date_mini = date[i]
    return temp_mini, date_mini

def inverse_chaine(chaine):
    '''Retourne la chaine inversée'''
    resultat = '' 
    for caractere in chaine:
        resultat = caractere + resultat 
    return resultat

def est_palindrome(chaine):
    '''Renvoie un booléen indiquant si la chaine ch
    est un palindrome'''
    inverse = inverse_chaine(chaine)
    return chaine == inverse 

def est_nbre_palindrome(nbre):
    '''Renvoie un booléen indiquant si le nombre nbre 
    est un palindrome'''
    chaine = str(nbre) 
    return est_palindrome(chaine)



