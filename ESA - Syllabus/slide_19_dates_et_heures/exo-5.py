"""
    Exercice 5 :

    Écrivez un programme qui prend une date de naissance en entrée et renvoie l'âge correspondant.
"""
from datetime import datetime as dt, timedelta

# date_naissance = "30-12-1996"
date_naissance = input("Date de naissance (dd-mm-yyyy) : ")

date_naissance_dt = dt.strptime(date_naissance, "%d-%m-%Y")

date_du_jour = dt.today()

age = (date_du_jour - date_naissance_dt) // timedelta(days=365.2425)

print(age)
