"""
    Exercice  4 :

    Écrivez une fonction qui vérifie si une date donnée est valide ou non.
"""
from datetime import datetime as dt

date_ok = "2025-04-13"
date_ko = "13-04-2025"


def verifier_date(date, format="%Y-%m-%d"):
    """
    Vérifie si une date donnée est valide en fonction du format spécifié.

    :param date: (str) La chaîne de caractères représentant la date à vérifier.
    :param format: (str) Le format de la date attendue (par défaut : "YYYY-MM-DD").
    :return: (bool) Retourne True si la date est valide, False sinon.
    """
    try:
        dt.strptime(date, format)
        return True
    except ValueError as ve:
        print("ERREUR : ", ve)
        return False


print(verifier_date("2025-04-08"))  # True
print(verifier_date("2025-04-31"))  # False  ERREUR :  day is out of range for month
print(verifier_date("2025-13-01"))  # False  ERREUR :  time data '2025-13-01' does not match format '%Y-%m-%d'

print(f"La date est {"valide" if verifier_date(date_ok) else "invalide"} !")  # La date est valide !

print(f"La date est {"valide" if verifier_date(date_ko) else "invalide"} !")
# ERREUR :  time data '13-04-2025' does not match format '%Y-%m-%d'
# La date est invalide !
