"""
    Exercice 2 :

    Écrivez une fonction qui prend une date en entrée et renvoie le jour de la semaine correspondant
    (par exemple, lundi, mardi, etc.).
"""
from datetime import datetime as dt

# date = "08-04-2025"
date = input("Date (dd-mm-yyyy) : ")


def jour_de_la_semaine(date, ):
    """
    :param date: (str) date
    :return: (str) jour de la semaine
    """
    dict_jours_anglais_vers_francais = {
        "Monday": "lundi",
        "Tuesday": "mardi",
        "Wednesday": "mercredi",
        "Thursday": "jeudi",
        "Friday": "vendredi",
        "Saturday": "samedi",
        "Sunday": "dimanche"
    }

    date_dt = dt.strptime(date, "%d-%m-%Y")  # strptime => string parse time
    jour = date_dt.strftime("%A")                    # strftime => string format time

    return dict_jours_anglais_vers_francais[jour]


print(f"Le {date} est un {jour_de_la_semaine(date)}.")
