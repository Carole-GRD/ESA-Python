"""
        Module : dictionnaire contenant les informations sur chaque étudiant

        Fonctions :
            modifier_etudiant
            gerer_champs_etudiants
"""

from .charger_sauvegarder_donnees import charger_donnees
from .charger_sauvegarder_donnees import sauvegarder_donnees

from .etd_list import selectionner_etudiant


def modifier_etudiant(liste_etudiants):
    """
    Modifie une information (valeur du dictionnaire) concernant un étudiant.

    :param etudiant: (dict) Dictionnaire contenant les informations de l'étudiant.
    :return: (list) La liste des étudiants.
    """

    etudiant = selectionner_etudiant(liste_etudiants)

    for key, value in etudiant.items():
        # print(f"    {key}: {value}")
        if key != "cotes (sur 20)" and key != "moyenne":
            print(f"    {key}: {value}")

    while True:
        cle = input('Quelle information souhaitez-vous modifier : ')
        if cle in etudiant.keys():
            break

    valeur = input(f"{cle} : ")
    etudiant[cle] = valeur

    sauvegarder_donnees(liste_etudiants, fichier="data/etudiants.json")
    liste_etudiants = charger_donnees("data/etudiants.json")

    print(f"Étudiant avec ID {etudiant['id']} modifié avec succès.")
    return liste_etudiants


def gerer_champs_etudiants(liste_etudiants, action):
    """
    Ajoute/Supprime un champ (clé du dictionnaire) concernant les étudiants.

    :param liste_etudiants: (list) Liste des étudiants enregistrés.
    :param action: (str) Indique si on ajoute ou supprime un champ.
    :return: Ne retourne rien. Modifie la structure du dictionnaire.
    """
    print("\n")
    cle = input(f"Entrez le nom du champ à {"ajouter" if action == "ajouter" else "supprimer"} : ")

    if action == "ajouter":
        for etudiant in liste_etudiants:
            etudiant[cle] = 'non renseigné'
        print(f"Champ '{cle}' ajouté avec succès !")

    else:
        for etudiant in liste_etudiants:
            etudiant.pop(cle, None)  # Supprime la clé si elle existe
        print(f"Champ '{cle}' supprimé avec succès !")

    sauvegarder_donnees(liste_etudiants, fichier="data/etudiants.json")
    liste_etudiants = charger_donnees("data/etudiants.json")

    return liste_etudiants
