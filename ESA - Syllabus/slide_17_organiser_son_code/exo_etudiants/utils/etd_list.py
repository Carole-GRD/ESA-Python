"""
    Module : liste contenant l'ensemble des étudiants

    Fonctions :
        afficher_etudiants
        ajouter_etudiant
        supprimer_etudiant
"""


# ==============================================================================================
# ==================================  Afficher les étudiants  ==================================
# ==============================================================================================

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
            if key == "côtes (sur 20)" and isinstance(value, dict):
                print("    côtes :")
                for matiere, cote in value.items():
                    print(f"      ⏺️ {matiere}: {"{:.2f}".format(cote)}/20")
            elif key == "moyenne" and value is None:
                print(f"    {key}:")
            else:
                print(f"    {key}: {value}")


# ==============================================================================================
# ===================================  Ajouter un étudiant  ===================================
# ==============================================================================================

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

        elif cle == "côtes (sur 20)":
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
    print(f"Étudiant {nouvel_etudiant['nom']} {nouvel_etudiant['prenom']} ajouté avec succès !")

    return liste_etudiants


# ==============================================================================================
# ==================================  Supprimer un étudiant  ===================================
# ==============================================================================================

def supprimer_etudiant(liste_etudiants, etudiant):
    """
    Supprime un étudiant de la liste des étudiants.

    :param liste_etudiants: (list) Liste des étudiants enregistrés.
    :param etudiant: (dict) Dictionnaire contenant les informations de l'étudiant.
    :return: Rien, permet de mettre à jour les données de l'étudiant
    """

    liste_etudiants.remove(etudiant)
    print(f"L'étudiant {etudiant['id']} a été supprimé avec succès.")
