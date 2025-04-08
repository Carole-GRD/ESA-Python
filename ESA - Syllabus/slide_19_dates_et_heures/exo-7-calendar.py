"""
    Exercice 7 :

    Écrivez une fonction qui prend un mois et une année en entrée et renvoie le nombre de jours dans ce mois.
"""
import calendar


def nombre_jours_dans_mois(mois, annee):
    """
    Renvoie le nombre de jours dans un mois donné pour une année donnée.

    :param mois: (int) Le mois (1 = janvier, ..., 12 = décembre)
    :param annee: (int) L'année (ex: 2025)
    :return: (int) Le nombre de jours dans le mois
    """
    # La fonction monthrange retourne (jour_de_la_semaine_du_premier_jour, nb_jours)
    _, nb_jours = calendar.monthrange(annee, mois)
    return nb_jours


# Utilisation :
print(nombre_jours_dans_mois(2, 2024))  # ➡️ 29 (année bissextile)
print(nombre_jours_dans_mois(2, 2025))  # ➡️ 28
print(nombre_jours_dans_mois(4, 2025))  # ➡️ 30

mois = int(input("Mois : "))
annee = int(input("Année : "))
print(nombre_jours_dans_mois(mois, annee), "jours")
