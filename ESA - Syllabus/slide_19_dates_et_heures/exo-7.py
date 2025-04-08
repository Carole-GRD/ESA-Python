"""
    Exercice 7 :

    Écrivez une fonction qui prend un mois et une année en entrée et renvoie le nombre de jours dans ce mois.
"""
from datetime import datetime as dt, timedelta


def nbr_jours_dans_mois(mois, annee):
    """
    :param mois: (int) Mois en chiffre (1 à 12)
    :param anne: (int) L'année (ex: 2025) - ATTENTION minimum 1000
    :return: (tuple) Nombre de jours, nom du mois en français, année
    """
    mois_anglais_vers_francais = {
        "January": "janvier",
        "February": "février",
        "March": "mars",
        "April": "avril",
        "May": "mai",
        "June": "juin",
        "July": "juillet",
        "August": "août",
        "September": "septembre",
        "October": "octobre",
        "November": "novembre",
        "December": "décembre"
    }

    # On convertit l'année en chaîne de 4 chiffres (ex : 999 devient '0999')
    # pour respecter le format attendu par strptime ("%Y")
    annee_str = str(annee).zfill(4)
    # Crée une date au 1er du mois
    date = dt.strptime(f"{mois}-{annee_str}", "%m-%Y")
    nom_mois_anglais = date.strftime("%B")  # Ex: "March"

    # On part de 28 jours, et on ajoute 1 jour jusqu'à ce que le mois change
    jours = 28

    while True:
        date_test = date + timedelta(days=jours)
        if date_test.month != mois:
            break
        jours += 1

    nom_mois_francais = mois_anglais_vers_francais[nom_mois_anglais]
    return jours, nom_mois_francais, annee


# Appel de la fonction
mois = int(input("Mois (1-12) : "))
annee = int(input("Année : "))
nb_jours, mois_fr, annee = nbr_jours_dans_mois(mois, annee)
print(f"Il y a {nb_jours} jours en {mois_fr} {annee}.")
