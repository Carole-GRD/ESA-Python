"""
    Module : liste contenant l'ensemble des étudiants

    Fonctions :
        selectionner_etudiant
        afficher_etudiants
        ajouter_etudiant
        supprimer_etudiant
"""

from .charger_sauvegarder_donnees import charger_donnees
from .charger_sauvegarder_donnees import sauvegarder_donnees


def selectionner_etudiant(liste_etudiants):
    """
    Permet de sélectionner un étudiant à partir de son ID.

    :param liste_etudiants: (list) Liste des étudiants enregistrés.
    :return: (dict) L'étudiant sélectionné.
    """
    print("\n--------  LISTE DES ETUDIANTS  --------")
    for etudiant in liste_etudiants:
        print(f"{etudiant['id']} : {etudiant['prenom']} {etudiant['nom']}")

    etudiant_id = input("\nSélectionner un étudiant (ID) : ")

    for etudiant in liste_etudiants:
        if etudiant['id'] == etudiant_id:
            return etudiant


def afficher_etudiants(liste_etudiants):
    """
    Affiche les étudiants de manière formatée.

    :param liste_etudiants: (list) Liste des étudiants enregistrés.
    :return: Ne retourne rien. Affiche la liste des étudiants de manière formatée.
    """
    for i, etudiant in enumerate(liste_etudiants):
        print(f"\nEtudiant {i + 1}")
        print("----------")
        for key, value in etudiant.items():
            # if key == "date_de_naissance":
            #     print(f"    {key}: {value.strftime('%d/%m/%Y')}")  # Format : 26/05/1980
            if key == "cotes (sur 20)" and isinstance(value, dict):
                print("    côtes :")
                for matiere, cote in value.items():
                    print(f"      ⏺️ {matiere}: {"{:.2f}".format(cote)}/20")
            elif key == "moyenne" and value is None:
                print(f"    {key}:")
            else:
                print(f"    {key}: {value}")


def ajouter_etudiant(liste_etudiants):
    """
    Ajoute un nouvel étudiant à la liste des étudiants.

    L'utilisateur entre les informations générales de l'étudiant, mais **ne doit pas** saisir les notes ni la moyenne :
        → Les "notes" sont gérées par le module `note_list.py`.
        → La "moyenne" est calculée automatiquement à partir des notes.

    :param liste_etudiants: (list) Liste des étudiants enregistrés.
    :return liste_etudiants: (list) La liste des étudiants mise à jour (avec le nouvel étudiant ajouté).
    """
    print("\nAjouter un étudiant...")

    nouvel_etudiant = {}

    for cle in liste_etudiants[0].keys():  # On parcourt les clés du premier étudiant pour voir les champs disponibles.

        if cle == "id":
            # Extraire les numéros d'ID existants.
            numeros_ids = [int(etudiant["id"][3:]) for etudiant in liste_etudiants if etudiant["id"].startswith("ETU")]
            # Trouver le plus grand ID existant.
            dernier_id = max(numeros_ids, default=0)
            # Générer le nouvel ID en l'incrémentant de 1.
            nouvel_etudiant["id"] = f"ETU{dernier_id + 1:03}"

        elif cle == "cotes (sur 20)":
            nouvel_etudiant[cle] = {}

        elif cle == "moyenne":
            nouvel_etudiant[cle] = None

        else:
            valeur = input(f"{cle.capitalize()} : ")
            if valeur.strip() == "":
                valeur = "non renseigné"  # Si aucun renseignement
            nouvel_etudiant[cle] = valeur

    # Ajouter l'étudiant à la liste
    liste_etudiants.append(nouvel_etudiant)

    sauvegarder_donnees(liste_etudiants, fichier="data/etudiants.json")
    liste_etudiants = charger_donnees("data/etudiants.json")

    print(f"Étudiant {nouvel_etudiant['nom']} {nouvel_etudiant['prenom']} ajouté avec succès !")

    return liste_etudiants


def supprimer_etudiant(liste_etudiants):
    """
    Supprime un étudiant de la liste des étudiants.

    :param liste_etudiants: (list) Liste des étudiants enregistrés.
    :param etudiant: (dict) Dictionnaire contenant les informations de l'étudiant.
    :return: Rien, permet de mettre à jour les données de l'étudiant
    """
    etudiant = selectionner_etudiant(liste_etudiants)

    liste_etudiants.remove(etudiant)

    sauvegarder_donnees(liste_etudiants, fichier="data/etudiants.json")
    liste_etudiants = charger_donnees("data/etudiants.json")

    print(f"L'étudiant {etudiant['id']} a été supprimé avec succès.")
    return liste_etudiants
