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
        Modifier un étudiant :
        ----------------------
            ETU002 → nom → NEYMAR
            ETU003 → adresse (si ajoutée) → 42, Rue des Algorithmes, 1000 BRUXELLES

        -------------------------
        Modifier structure dico :
        -------------------------
            Ajouter une clé : "adresse", "nationalité", "genre", "bourse"...
            Supprimer une clé : "telephone" (ou "adresse" si déjà ajoutée)

"""

from utils.charger_sauvegarder_donnees import charger_donnees
from utils.charger_sauvegarder_donnees import sauvegarder_donnees

from utils.cote_list import ajouter_cote
from utils.cote_list import lire_une_cote
from utils.cote_list import modifier_cote
from utils.cote_list import calculer_moyenne
from utils.cote_list import supprimer_cote
from utils.cote_list import trouver_min_max_cotes

from utils.etd_dico import gerer_champs_etudiants
from utils.etd_dico import modifier_etudiant

from utils.etd_list import afficher_etudiants
from utils.etd_list import ajouter_etudiant
from utils.etd_list import selectionner_etudiant
from utils.etd_list import supprimer_etudiant


# ==============================================================================================
# ===================================  Liste des étudiants  ===================================
# ==============================================================================================

liste_etudiants = charger_donnees("data/etudiants.json")

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
            liste_etudiants = ajouter_etudiant(liste_etudiants)

        case '3':
            liste_etudiants = modifier_etudiant(liste_etudiants)

        case '4':
            liste_etudiants = supprimer_etudiant(liste_etudiants)

        case '5':
            while True:
                menu_action = input(f"\n--------  📝 MODIFIER LE DICTIONNAIRE 📝  --------\n"
                                    f"1: 📝 Ajouter un champ\n"
                                    f"2: 📝 Supprimer un champ\n"
                                    f"q:    Quitter\n"
                                    f"\n         Votre choix : ").lower()

                action = ""
                if menu_action == 'q':
                    break
                elif menu_action == '1':
                    action = "ajouter"
                elif menu_action == '2':
                    action = "supprimer"

                liste_etudiants = gerer_champs_etudiants(liste_etudiants, action)

        case '6':
            while True:
                etudiant_selectionne = selectionner_etudiant(liste_etudiants)

                menu_action = input(f"\n------------  ✔️ GESTION DES CÔTES ✔️  ------------\n"
                                    f"1: ✔️ Ajouter une côte\n"
                                    f"2: ✔️ Modifier une côte\n"
                                    f"3: ✔️ Supprimer une côte\n"
                                    f"4: ✔️ Lire une côte\n"
                                    f"5: ✔️ Plus petite côte et plus grande côte\n"
                                    f"6: ✔️ Calculer la moyenne\n"
                                    f"q:    Quitter\n"
                                    f"\n         Votre choix : ").lower()

                match menu_action:

                    case 'q':
                        break

                    case '1':
                        liste_etudiants = ajouter_cote(liste_etudiants, etudiant_selectionne, calculer_moyenne)

                    case '2':
                        liste_etudiants = modifier_cote(liste_etudiants, etudiant_selectionne)

                    case '3':
                        liste_etudiants = supprimer_cote(liste_etudiants, etudiant_selectionne)

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
                        moyenne = calculer_moyenne(etudiant_selectionne['cotes (sur 20)'].values())
                        etudiant_selectionne['moyenne'] = "{:.2f}".format(moyenne) + '/100'
                        sauvegarder_donnees(liste_etudiants, fichier="data/etudiants.json")
                        liste_etudiants = charger_donnees("data/etudiants.json")

                quitter_gestion_cote = input('\nRevenir au menu principal (q) ou continuer (c) : ')
                if quitter_gestion_cote == 'q':
                    break
