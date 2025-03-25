"""
    Exercice1 :

    Reprenez l’exercice sur la manipulation des étudiants au travers d’une liste
    en créant un package qui contiendra deux modules :
        • module etd_dico.py ;
        • module etd_list.py ;

    Exercice2 :

    Rajoutez un module cote_list.py, au package précédent, qui permet de rajouter des côtes à un étudiant.
    Ce module devra posséder les fonctionnalités suivantes :
        • ajouter, modifier, supprimer, lire une côte ;
        • donner la plus basse et la plus grande côte ;
        • donner la moyenne de l’étudiant.


    Pour tester...

        --------------------
        Ajouter un étudiant :
        --------------------
            nom : DION
            prenom : Céline
            date_de_naissance : 1988-07-25
            email : celine@test.be
            telephone : +32 499 55 44 33
            section : Chant
            année : Licence 2

            adresse : Rue des Stars, H2Y3N8 MONTREAL

            côtes (sur 20) : {
                "Chant": 19,
                "Théorie musicale": 17,
                "Interprétation": 20,
                "Solfège": 18
            }
            ----------------------
            nom : GOLDMAN
            prenom : Jean-Jacques
            date_de_naissance : 1975-08-01
            email : jj-goldman@test.be
            telephone : +32 454 12 47 66
            section : Compositeur
            année : Licence 1

            adresse : Av. Rapp 14, 75001 PARIS

            côtes (sur 20) : {
                "Composition": 16,
                "Écriture musicale": 17,
                "Analyse harmonique": 16,
                "Arrangement": 15
            }
            ----------------------
            nom : TURING
            prenom : Alan
            date_de_naissance : 2002-06-23
            email : enigma@test.be
            telephone : +32 477 89 56 12
            section : Informatique
            année : Licence 3

            adresse : 42, Rue des Algorithmes, 1000 BRUXELLES

            côtes (sur 20) : {
                "Programmation": 18,
                "Structures de données": 17,
                "Algorithmique": 19,
                "Systèmes d'exploitation": 16
            }
            ----------------------

        ----------------------
        Modifier un étudiant :
        ----------------------
            ETU002 → nom → NEYMAR

        -------------------------
        Modifier structure dico :
        -------------------------
            Ajouter une clé : "adresse", "nationalité", "genre", "bourse"...
            Supprimer une clé : "telephone" (ou "adresse" si déjà ajoutée)

"""

from datetime import date

from utils.cote_list import ajouter_cote
from utils.cote_list import lire_une_cote
from utils.cote_list import modifier_cote
from utils.cote_list import moyennes
from utils.cote_list import calculer_moyenne
from utils.cote_list import supprimer_cote
from utils.cote_list import trouver_min_max_cotes

from utils.etd_dico import gerer_champs_etudiants
from utils.etd_dico import modifier_etudiant

from utils.etd_list import afficher_etudiants
from utils.etd_list import ajouter_etudiant
from utils.etd_list import supprimer_etudiant

# ==============================================================================================
# ===================================  Liste des étudiants  ===================================
# ==============================================================================================

liste_etudiants = [
    {
        "id": "ETU001",
        "nom": "LAMY",
        "prenom": "Alexandra",
        "date_de_naissance": date(2000, 5, 26),
        "email": "alex@test.be",
        "telephone": "+32 478 12 34 56",
        "section": "Français",
        "année": "Licence 2",
        "côtes (sur 20)": {
            "Littérature": 15,
            "Grammaire": 14,
            "Expression écrite": 16,
            "Histoire": 14.5
        },
        "moyenne": "74.38/100"
        # "moyenne": None
    },
    {
        "id": "ETU002",
        "nom": "DUJARDIN",
        "prenom": "Jean",
        "date_de_naissance": date(1999, 11, 3),
        "email": "jean@test.be",
        "telephone": "+32 465 78 90 12",
        "section": "Mathématiques",
        "année": "Master 1",
        "côtes (sur 20)": {
            "Analyse": 17,
            "Algèbre": 15,
            "Statistiques": 16,
            "Probabilités": 16.5
        },
        "moyenne": "80.62/100"
        # "moyenne": None
    },
    {
        "id": "ETU003",
        "nom": "TURING",
        "prenom": "Alan",
        "date_de_naissance": date(1930, 12, 31),
        "email": "alan@test.be",
        "telephone": "+32 477 89 56 12",
        "section": "Informatique",
        "année": "Licence 3",
        "côtes (sur 20)": {},
        "moyenne": None
    }
]


# ==============================================================================================
# ===================================  Fonctions  ===================================
# ==============================================================================================

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


# ==============================================================================================
# ===================================  Programme principal  ====================================
# ==============================================================================================

while True:
    menu = input(f"\n|-----------------------------|\n"
                 f"|-------- 📜 MENU 📜 ---------|\n"
                 f"|-----------------------------|\n"
                 f"1: 📜 Afficher les étudiants\n"
                 f"2: 📜 Ajouter un étudiant\n"
                 f"3: 📜 Modifier un étudiant\n"
                 f"4: 📜 Supprimer un étudiant\n"
                 f"5: 📜 Modifier la structure des informations\n"
                 f"6: 📜 Gestion des côtes\n"
                 f"q:    Quitter\n"
                 f"\n       Votre choix : ").lower()

    match menu:

        case 'q':
            print("\nÀ bientôt 👋")
            break

        case '1':
            afficher_etudiants(liste_etudiants)

        case '2':
            ajouter_etudiant(liste_etudiants)

        case '3':
            etudiant_a_modifier = selectionner_etudiant(liste_etudiants)
            modifier_etudiant(etudiant_a_modifier)

        case '4':
            etudiant_a_supprimer = selectionner_etudiant(liste_etudiants)
            supprimer_etudiant(liste_etudiants, etudiant_a_supprimer)

        case '5':
            while True:
                action = input(f"\n--------  📝 MODIFIER LE DICTIONNAIRE 📝  --------\n"
                               f"1: 📝 Ajouter un champ\n"
                               f"2: 📝 Supprimer un champ\n"
                               f"q:    Quitter\n"
                               f"\n         Votre choix : ").lower()
                if action == 'q':
                    break
                elif action == '1':
                    gerer_champs_etudiants(liste_etudiants, "ajouter")
                elif action == '2':
                    gerer_champs_etudiants(liste_etudiants, "supprimer")

        case '6':
            while True:
                etudiant_selectionne = selectionner_etudiant(liste_etudiants)

                action = input(f"\n------------  ✔️ GESTION DES CÔTES ✔️  ------------\n"
                               f"1: ✔️ Ajouter une côte\n"
                               f"2: ✔️ Modifier une côte\n"
                               f"3: ✔️ Supprimer une côte\n"
                               f"4: ✔️ Lire une côte\n"
                               f"5: ✔️ Plus petite côte et plus grande côte\n"
                               f"6: ✔️ Calculer les moyennes\n"
                               f"q:    Quitter\n"
                               f"\n         Votre choix : ").lower()

                match action:
                    case 'q':
                        break
                    case '1':
                        ajouter_cote(etudiant_selectionne, calculer_moyenne)
                    case '2':
                        modifier_cote(etudiant_selectionne)
                    case '3':
                        supprimer_cote(etudiant_selectionne)
                    case '4':

                        cours = input('Intitulé du cours : ')
                        cote = lire_une_cote(etudiant_selectionne, cours)
                        print(f"{cours} : {cote}/20")
                    case '5':
                        resultats = trouver_min_max_cotes(etudiant_selectionne)

                        if resultats["min_valeur"] is None:
                            print("❌ Cet étudiant n'a pas encore de notes.")
                        else:
                            print(
                                f"📌 Matière avec la meilleure note :"
                                f" {resultats['matiere_max']} ({resultats['max_valeur']}/20)")
                            print(
                                f"📌 Matière avec la plus faible note :"
                                f" {resultats['matiere_min']} ({resultats['min_valeur']}/20)")
                    case '6':
                        moyennes(liste_etudiants)

                quitter_gestion_cote = input('\nRevenir au menu principal (q) ou continuer (c) : ')
                if quitter_gestion_cote == 'q':
                    break

# TODO : 

"""
    1. Lire les données JSON
    ------------------------
    # Lire le fichier JSON
    with open("etudiants.json", "r", encoding="utf-8") as fichier_json:
        etudiants = json.load(fichier_json)
    
    # Afficher les données
    for etudiant in etudiants:
        print(f"Étudiant : {etudiant['prenom']} {etudiant['nom']}")
        print(f"Moyenne : {etudiant['moyenne']}")
        print(f"Notes : {etudiant['notes (sur 20)']}")
    
    2. Modifier les données
    -----------------------
    # Exemple : Augmenter la note de "Chant" de 1 point pour chaque étudiant
    for etudiant in etudiants:
        if "Chant" in etudiant["notes (sur 20)"]:
            etudiant["notes (sur 20)"]["Chant"] += 1
            etudiant["moyenne"] = sum(etudiant["notes (sur 20)"].values()) / len(etudiant["notes (sur 20)"])

    3. Sauvegarder les modifications
    --------------------------------
    # Écrire les modifications dans un nouveau fichier JSON
    with open("etudiants_modifies.json", "w", encoding="utf-8") as fichier_json:
        json.dump(etudiants, fichier_json, indent=4, ensure_ascii=False)
    
    print("Données JSON modifiées et sauvegardées !")


--------------------------


import json

def sauvegarder_donnees(liste_etudiants, fichier="etudiants.json"):
    with open(fichier, "w", encoding="utf-8") as f:
        json.dump(liste_etudiants, f, default=str, indent=4)

def charger_donnees(fichier="etudiants.json"):
    try:
        with open(fichier, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
"""

# def sauvegarder_donnees(liste_etudiants, fichier="etudiants.json"):
#     """
#     Sauvegarde la liste des étudiants dans un fichier JSON.
#
#     :param liste_etudiants: (list) Liste des étudiants à sauvegarder.
#     :param fichier: (str) Nom du fichier où stocker les données.
#     """
#     import json
#     with open(fichier, "w", encoding="utf-8") as f:
#         json.dump(liste_etudiants, f, default=str, indent=4)
#
#
# def charger_donnees(fichier="etudiants.json"):
#     """
#     Charge les données des étudiants depuis un fichier JSON.
#
#     :param fichier: (str) Nom du fichier contenant les données.
#     :return: (list) Liste des étudiants chargée depuis le fichier.
#     """
#     import json
#     try:
#         with open(fichier, "r", encoding="utf-8") as f:
#             return json.load(f)
#     except FileNotFoundError:
#         return []
