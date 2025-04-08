"""
    Exercice 6 :

    Écrivez un programme qui prend une date de début, une durée et renvoie la date de fin.
"""
from datetime import datetime as dt, timedelta

# debut = dt.strptime("07-04-2025", "%d-%m-%Y")

debut = dt.strptime(input("Date de début (dd-mm-yyyy) : "), "%d-%m-%Y")

jours = int(input("Durée (en jours) : "))

fin = debut + timedelta(days=jours)

print(fin.strftime("%d-%m-%Y"))
