"""
    Module : gestion des données
             voir fichier "etudiants.json" du répertoire "data"

    Fonctions :
        sauvegarder_donnees
        charger_donnees
"""


def sauvegarder_donnees(liste_etudiants, fichier="data/etudiants.json"):
    """
    Sauvegarde la liste des étudiants dans un fichier JSON.

    :param liste_etudiants: (list) Liste des étudiants à sauvegarder.
    :param fichier: (str) Nom du fichier où stocker les données.
    """
    import json
    with open(fichier, "w", encoding="utf-8") as f:
        json.dump(liste_etudiants, f, default=str, indent=4)
        # json.dump(liste_etudiants, f, indent=4)


def charger_donnees(fichier="data/etudiants.json"):
    """
    Charge les données des étudiants depuis un fichier JSON.

    :param fichier: (str) Nom du fichier contenant les données.
    :return: (list) Liste des étudiants chargée depuis le fichier.
    """
    import json
    try:
        with open(fichier, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
