"""
    Exercice 1 :

    Écrire un programme permettant de ranger dans une liste des éléments représentant des étudiants
    qui seront représentés par le dictionnaire “dico_etudiant” (à vous de définir les champs utiles).
    Le programme devra permettre de rajouter/supprimer/afficher des étudiants. Ainsi que de modifier la
    structure du dictionnaire (supprimer/ajouter des clés).
"""

from datetime import date

# ==============================================================================================
# ===================================  Liste des étudiants  ===================================
# ==============================================================================================

liste_etudiants = [
    {
        "id": "ETU001",
        "nom": "Lamy",
        "prenom": "Alexandra",
        "date_de_naissance": date(1980, 5, 26),
        "email": "alex@test.be",
        "telephone": "+32 478 12 34 56",
        "cursus": "Informatique",
        "niveau": "Licence 2",
        "moyenne": 14.8,
        "notes": [15, 14, 16, 14.5]
    },
    {
        "id": "ETU002",
        "nom": "Martin",
        "prenom": "Lucas",
        "date_de_naissance": date(1999, 11, 3),
        "email": "lucas@test.be",
        "telephone": "+32 465 78 90 12",
        "cursus": "Mathématiques",
        "niveau": "Master 1",
        "moyenne": 16.2,
        "notes": [17, 15, 16, 16.5]
    }
]

# Affichage formaté de la date
# print(dico_etudiant["date_de_naissance"].strftime("%d/%m/%Y"))  # 26/05/1980
# print(dico_etudiant["date_de_naissance"].strftime("%d-%m-%Y"))  # 26-05-1980


# ==============================================================================================
# ==================================  Afficher les étudiants  ==================================
# ==============================================================================================

for i, etudiant in enumerate(liste_etudiants):
    print(f"\nEtudiant {i + 1}")
    print("----------")
    for j, value in etudiant.items():
        print(f"{j}: {value}")


# ==============================================================================================
# ===================================  Ajouter un étudiant  ===================================
# ==============================================================================================


def ajouter_etudiant():
    """
    Permet d'ajouter un étudiant à la liste 'liste_etudiants'.

    L'utilisateur doit entrer les informations nécessaires pour le nouvel étudiant.
    La fonction s'adapte aux modifications de la structure des étudiants (ajout ou suppression de clés).
    """
    print("\nAjouter un étudiant...")

    # Créer un dictionnaire vide pour le nouvel étudiant
    nouvel_etudiant = {}

    # Demander les informations de l'étudiant uniquement pour les champs existants dans la structure
    for cle in liste_etudiants[0].keys():  # On parcourt les clés du premier étudiant pour voir les champs disponibles
        if cle == "moyenne" or cle == "notes":
            continue  # On saute ces champs, notes demandés plus tard et moyenne calculée automatiquement

        # Demander à l'utilisateur de saisir la valeur pour chaque champ existant
        valeur = input(f"{cle.capitalize()} : ")

        # Si aucun renseignement, la valeur sera `None`
        if valeur.strip() == "":
            valeur = None

        # Ajouter la valeur au dictionnaire de l'étudiant
        nouvel_etudiant[cle] = valeur

    # Demander les notes et calculer la moyenne
    notes = input("Notes (séparées par une virgule, laisser vide si non renseignées) : ")
    if notes == "":
        notes = []  # Si aucune note n'est saisie
        moyenne = None  # Pas de moyenne calculée si aucune note
    else:
        notes = [float(x) for x in notes.split(",")]
        moyenne = sum(notes) / len(notes)  # Calcul de la moyenne

    # Ajouter les notes et la moyenne calculée
    nouvel_etudiant["notes"] = notes
    nouvel_etudiant["moyenne"] = moyenne

    # Générer un ID unique pour l'étudiant
    nouvel_etudiant["id"] = f"ETU{len(liste_etudiants) + 1:03}"  # Crée un ID unique basé sur le nombre d'étudiants

    # Ajouter l'étudiant à la liste
    liste_etudiants.append(nouvel_etudiant)
    print(f"Étudiant {nouvel_etudiant['nom']} {nouvel_etudiant['prenom']} ajouté avec succès !")


# Exemple d'utilisation :
# ------------------------

# Entrer les données suivantes

# id : ETU003,
# nom : Dupont
# prenom : Sophie
# date_de_naissance : 2001-7-15
# email : sophie@test.be
# telephone : +32 499 55 44 33
# cursus : Physique
# niveau : Licence 1
# notes : [14, 12, 13, 15]


ajouter_etudiant()

for i, etudiant in enumerate(liste_etudiants):
    print(f"\nEtudiant {i + 1}")
    print("----------")
    for k, value in etudiant.items():
        print(f"{k}: {value}")


# ==============================================================================================
# ===============================  Supprimer un étudiant par ID  ===============================
# ==============================================================================================

def supprimer_etudiant():
    """
    Permet de supprimer un étudiant de la liste 'liste_etudiants' en fonction de son ID.

    L'utilisateur doit entrer l'ID de l'étudiant à supprimer.
    """

    # Demander l'ID de l'étudiant à supprimer
    etudiant_id = input("\nEntrez l'ID de l'étudiant à supprimer : ")

    # Chercher l'étudiant par son ID
    for etudiant in liste_etudiants:
        if etudiant["id"] == etudiant_id:
            liste_etudiants.remove(etudiant)  # Supprimer l'étudiant de la liste
            print(f"Étudiant avec ID {etudiant_id} supprimé avec succès.")
            return

    print(f"\nÉtudiant avec l'ID {etudiant_id} introuvable.")


# Exemple d'utilisation :
# ------------------------

# entrer l'ID "ETU002" par exemple
supprimer_etudiant()

for i, etudiant in enumerate(liste_etudiants):
    print(f"\nEtudiant {i + 1}")
    print("----------")
    for k, value in etudiant.items():
        print(f"{k}: {value}")


# ==============================================================================================
# ================  Ajouter/Supprimer dynamiquement une clé avec une fonction  =================
# ==============================================================================================

def modifier_structure(ajouter=True):
    """
    Modifie la structure des dictionnaires représentant des étudiants
    en ajoutant ou supprimant une clé.

    :param ajouter: (bool, optionnel)
        Si 'True', la clé sera ajoutée avec une valeur par défaut.
        Si 'False', la clé sera supprimée des dictionnaires.
        La valeur par défaut est 'True'.

    :return: /
    """
    print("\n")
    cle = input("Entrez le nom de la clé à " + ("ajouter" if ajouter else "supprimer") + " : ")

    if ajouter:
        valeur = input(f"Entrez la valeur par défaut pour '{cle}': ")
        for etudiant in liste_etudiants:
            etudiant[cle] = valeur
        print(f"Clé '{cle}' ajoutée avec succès !")

    else:
        for etudiant in liste_etudiants:
            etudiant.pop(cle, None)  # Supprime la clé si elle existe
        print(f"Clé '{cle}' supprimée avec succès !")


# Exemple d'utilisation :
# ------------------------

# Ajouter une clé (ex : "adresse" avec comme valeur par défaut "non renseignée")
modifier_structure(ajouter=True)

for i, etudiant in enumerate(liste_etudiants):
    print(f"\nEtudiant {i + 1}")
    print("----------")
    for k, value in etudiant.items():
        print(f"{k}: {value}")


# Supprimer une clé (ex : "telephone")
modifier_structure(ajouter=False)

for i, etudiant in enumerate(liste_etudiants):
    print(f"\nEtudiant {i + 1}")
    print("----------")
    for k, value in etudiant.items():
        print(f"{k}: {value}")
