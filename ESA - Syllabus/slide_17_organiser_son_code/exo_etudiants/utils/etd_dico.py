"""
        Module : dictionnaire contenant les informations sur chaque étudiant

        Fonctions :
            modifier_etudiant
            gerer_champs_etudiants
"""


# ==============================================================================================
# =====================  Modifier une information concernant un étudiant  =====================
# ==============================================================================================

def modifier_etudiant(etudiant):
    """
    Modifie une information (valeur du dictionnaire) concernant un étudiant.

    :param etudiant: (dict) Dictionnaire contenant les informations de l'étudiant.
    :return: Rien, permet de mettre à jour les données de l'étudiant.
    """

    # Afficher les informations concernant l'étudiant
    for key, value in etudiant.items():
        print(f"    {key}: {value}")

    # Demander le champ à modifier
    while True:
        cle = input('Quelle information souhaitez-vous modifier : ')
        if cle in etudiant.keys():
            break

    # Demander la nouvelle valeur
    valeur = input(f"{cle} : ")
    # Modifier la valeur
    etudiant[cle] = valeur

    print(f"Étudiant avec ID {etudiant['id']} modifié avec succès.")


# ==============================================================================================
# ================================  Ajouter/Supprimer une clé  =================================
# ==============================================================================================

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

    return liste_etudiants
