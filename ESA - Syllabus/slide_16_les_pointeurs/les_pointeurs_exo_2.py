"""
    Exercice 2 :

    Reprenez l’exercice permettant d’encoder des utilisateurs dans une liste et,
    cette-fois ci, utilisez, non pas une liste mais un tuple.
        ● faites un schéma comparatif de ce qui se passe, point de vue adressage des variables,
        lors de l’appel de vos fonctions.

    Rappel de l'exercice (voir slide_14_structures_de_donnees_heterogenes :

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
        "date_de_naissance": date(2000, 5, 26),
        "email": "alex@test.be",
        "telephone": "+32 478 12 34 56",
        "cursus": "Français",
        "niveau": "Licence 2",
        "moyenne": 14.80,
        "notes (sur 20)": [15, 14, 16, 14.5]
    },
    {
        "id": "ETU002",
        "nom": "Dujardin",
        "prenom": "Jean",
        "date_de_naissance": date(1999, 11, 3),
        "email": "jean@test.be",
        "telephone": "+32 465 78 90 12",
        "cursus": "Mathématiques",
        "niveau": "Master 1",
        "moyenne": 16.20,
        "notes (sur 20)": [17, 15, 16, 16.5]
    }
]

# Affichage formaté de la date
# print(dico_etudiant["date_de_naissance"].strftime("%d/%m/%Y"))  # 26/05/1980
# print(dico_etudiant["date_de_naissance"].strftime("%d-%m-%Y"))  # 26-05-1980


# ==============================================================================================
# ==================================  Afficher les étudiants  ==================================
# ==============================================================================================

def afficher_etudiants(liste_etudiants):
    """
    :param liste_etudiants: (list) Liste de dictionnaires reprenant les informations des étudiants.
    :return: Ne retourne rien. Affiche la liste des étudiants de manière formatée.
    """
    for i, etudiant in enumerate(liste_etudiants):
        print(f"\nEtudiant {i + 1}")
        print("----------")
        for key, value in etudiant.items():
            print(f"    {key}: {value}")


# ==============================================================================================
# ===================================  Ajouter un étudiant  ===================================
# ==============================================================================================


def ajouter_etudiant(liste_etudiants):
    """
    :param liste_etudiants: (list) Liste de dictionnaires reprenant les informations des étudiants.
    :return liste_etudiants: (list) Liste de dictionnaires avec le nouvel étudiant ajouté.
    """
    print("\nAjouter un étudiant...")

    # Créer un dictionnaire vide pour le nouvel étudiant
    nouvel_etudiant = {}

    for cle in liste_etudiants[0].keys():  # On parcourt les clés du premier étudiant pour voir les champs disponibles.

        if cle == "id":
            # Extraire les numéros d'ID existants.
            numeros_ids = [int(etudiant["id"][3:]) for etudiant in liste_etudiants if etudiant["id"].startswith("ETU")]
            # Trouver le plus grand ID existant.
            dernier_id = max(numeros_ids, default=0)
            # Générer le nouvel ID en l'incrémentant de 1.
            nouvel_etudiant["id"] = f"ETU{dernier_id + 1:03}"

        elif cle == "notes (sur 20)":
            notes = input("Notes (séparées par une virgule, laisser vide si non renseignées) : ")
            if notes == "":  # Si aucune note n'est saisie
                # notes = []
                # moyenne = None
                nouvel_etudiant["notes"] = 'pas de notes'
                nouvel_etudiant["moyenne"] = '/'
            else:
                notes = [float(x) for x in notes.split(",")]
                moyenne = sum(notes) / len(notes)
                nouvel_etudiant["notes"] = [int(note) for note in notes]
                nouvel_etudiant["moyenne"] = "{:.2f}".format(moyenne)

        elif cle == "moyenne":  # la moyenne est calculée sur base des notes
            continue

        else:
            valeur = input(f"{cle.capitalize()} : ")
            if valeur.strip() == "":
                valeur = "non renseigné"  # Si aucun renseignement
            nouvel_etudiant[cle] = valeur

    # Ajouter l'étudiant à la liste
    liste_etudiants.append(nouvel_etudiant)
    print(f"Étudiant {nouvel_etudiant['nom']} {nouvel_etudiant['prenom']} ajouté avec succès !")

    return liste_etudiants


# Exemple d'utilisation :
# ------------------------

# Entrer les données suivantes

# nom : Dion
# prenom : Céline
# date_de_naissance : 2001-7-15
# email : celine@test.be
# telephone : +32 499 55 44 33
# cursus : Chanteuse
# niveau : Licence 2
# notes : [19, 17, 20, 18]

# adresse : Rue des Stars, MONTREAL H2Y 3N8


# ----------------------

# nom : Goldman
# prenom : Jean-Jacques
# date_de_naissance : 1975-08-01
# email : jj-goldman@test.be
# telephone : +32 454 12 47 66
# cursus : Compositeur
# niveau : Licence 1
# notes : [16, 17, 16, 15]

# adresse :

# ==============================================================================================
# ===============================  Modifier un étudiant par ID  ===============================
# ==============================================================================================

def modifier_etudiant(liste_etudiants):
    """
    :param liste_etudiants: (list) Liste de dictionnaires reprenant les informations des étudiants.
    :return liste_etudiants: (list) Liste de dictionnaires, des étudiants, mise à jour.
    """

    # Demander l'ID de l'étudiant à supprimer
    etudiant_id = input("\nEntrez l'ID de l'étudiant (dont il faut mettre à jour les données) : ")

    # Chercher l'étudiant par son ID
    for etudiant in liste_etudiants:
        if etudiant["id"] == etudiant_id:
            for key, value in etudiant.items():
                print(f"    {key}: {value}")
            while True:
                cle = input('Quelle information souhaitez-vous modifier : ')
                if cle in etudiant.keys():
                    break
            valeur = input(f"{cle} : ")
            etudiant[cle] = valeur
            print(f"Étudiant avec ID {etudiant_id} modifié avec succès.")
            return liste_etudiants

    print(f"\nÉtudiant avec l'ID {etudiant_id} introuvable.")


# Exemple d'utilisation :
# ------------------------

"""
Entrez l'ID de l'étudiant (dont il faut mettre à jour les données) :   ETU001
Quelle information souhaitez-vous modifier :                           niveau
niveau :                                                               Licence 3

---------------------------
ou si champs "adresse" ajouté
---------------------------
Entrez l'ID de l'étudiant (dont il faut mettre à jour les données) :   ETU001
Quelle information souhaitez-vous modifier :                           adresse
adresse :                                                              Rue de l'Ange 6, 5000 NAMUR  

Entrez l'ID de l'étudiant (dont il faut mettre à jour les données) :   ETU002
Quelle information souhaitez-vous modifier :                           adresse
adresse :                                                              Allée des Etoiles 11, 5100 JAMBES
"""


# ==============================================================================================
# ===============================  Supprimer un étudiant par ID  ===============================
# ==============================================================================================

def supprimer_etudiant(liste_etudiants):
    """
    :param liste_etudiants: (list) Liste de dictionnaires reprenant les informations des étudiants.
    :return liste_etudiants: (list) Liste de dictionnaires, des étudiants, mise à jour (sans celui qui a été supprimé).
    """

    # Demander l'ID de l'étudiant à supprimer
    etudiant_id = input("\nEntrez l'ID de l'étudiant à supprimer : ")

    # Chercher l'étudiant par son ID
    for etudiant in liste_etudiants:
        if etudiant["id"] == etudiant_id:
            liste_etudiants.remove(etudiant)  # Supprimer l'étudiant de la liste
            print(f"Étudiant avec ID {etudiant_id} supprimé avec succès.")
            return liste_etudiants

    print(f"\nÉtudiant avec l'ID {etudiant_id} introuvable.")


# Exemple d'utilisation :
# ------------------------

# entrer l'ID "ETU002" par exemple


# ==============================================================================================
# ================  Ajouter/Supprimer dynamiquement une clé avec une fonction  =================
# ==============================================================================================

def modifier_structure_dico(liste_etudiants, action):
    """
    :param liste_etudiants: (list) Liste de dictionnaires reprenant les informations des étudiants.
    :param action: (str, optionnel) Permet de savoir si on ajoute ou supprime un champs.
    :return: Ne retourne rien. Modifie la structure du dictionnaire.
    """
    print("\n")
    cle = input(f"Entrez le nom de la clé à {"ajouter" if action == "ajouter" else "supprimer"} : ")

    if action == "ajouter":
        valeur = input(f"Entrez la valeur par défaut pour '{cle}': ")
        for etudiant in liste_etudiants:
            etudiant[cle] = valeur
        print(f"Clé '{cle}' ajoutée avec succès !")

    else:
        for etudiant in liste_etudiants:
            etudiant.pop(cle, None)  # Supprime la clé si elle existe
        print(f"Clé '{cle}' supprimée avec succès !")

    return liste_etudiants


# Exemple d'utilisation :
# ------------------------

# Ajouter une clé (ex : "adresse" avec comme valeur par défaut "non renseignée")
# Supprimer une clé (ex : "telephone" ou "adresse" si ajoutée)

while True:
    menu = input(f"\n--------  MENU  --------\n"
                 f"1: Afficher les étudiants\n"
                 f"2: Ajouter un étudiant\n"
                 f"3: Modifier un étudiant\n"
                 f"4: Supprimer un étudiant\n"
                 f"5: Modifier la structure des informations\n"
                 f"q: Quitter\n"
                 f"Votre choix : ").lower()
    match menu:
        case 'q':
            print("\nÀ bientôt 👋")
            break
        case '1':
            afficher_etudiants(liste_etudiants)
        case '2':
            ajouter_etudiant(liste_etudiants)
        case '3':
            modifier_etudiant(liste_etudiants)
        case '4':
            supprimer_etudiant(liste_etudiants)
        case '5':
            action = input(f"\n--------  MODIFIER LE DICTIONNAIRE  --------\n"
                           f"1: Ajouter un champs\n"
                           f"2: Supprimer un champs\n"
                           f"q: Quitter\n"
                           f"Votre choix : ").lower()
            if action == 'q':
                continue
            elif action == '1':
                modifier_structure_dico(liste_etudiants, "ajouter")
            elif action == '2':
                modifier_structure_dico(liste_etudiants, "supprimer")
