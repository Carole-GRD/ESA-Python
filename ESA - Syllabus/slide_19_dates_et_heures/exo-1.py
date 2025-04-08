"""
    Exercice 1 :

    Écrivez un programme qui demande à l'utilisateur deux dates (sous forme de chaînes)
    et affiche la différence entre ces deux dates en jours, heures, minutes et secondes.
"""
from datetime import datetime as dt

date_1 = dt.strptime(input("Première date (dd-mm-yyyy HH:MM:SS) : "), "%d-%m-%Y %H:%M:%S")
date_2 = dt.strptime(input("Seconde date (dd-mm-yyyy) HH:MM:SS : "), "%d-%m-%Y %H:%M:%S")
print(abs(date_1 - date_2))
