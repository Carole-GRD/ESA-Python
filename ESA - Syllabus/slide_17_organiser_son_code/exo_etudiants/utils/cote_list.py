"""
    Module : gestion des côtes d'un étudiant

    Fonctions :
        calculer_moyenne
        ajouter_cote
        modifier_cote
        supprimer_cote
        lire_une_cote
        trouver_min_max_cotes
        moyennes
"""


def calculer_moyenne(cote_list):
    """
    Calcule la moyenne des côtes d'un étudiant en pourcentage.

    :param cote_list: (list) Liste des côtes obtenues sur 20.
    :return: (float) Moyenne en pourcentage (/100).
    """
    total = sum(cote for cote in cote_list)
    nombre_de_cotes = len(cote_list)
    moyenne_sur_20 = total / nombre_de_cotes
    pourcentage = moyenne_sur_20 * 5
    return pourcentage

# ======================


def ajouter_cote(etudiant, calculer_moyenne):
    """
    Ajoute une nouvelle côte à un étudiant et met à jour sa moyenne.

    :param etudiant: (dict) Dictionnaire contenant les informations de l'étudiant.
    :param calculer_moyenne: (function) Fonction permettant de recalculer la moyenne.
    :return: Rien.
    """
    cote_list = etudiant['côtes (sur 20)']

    for cours, cote in cote_list.items():
        print(f"{cours} : {cote}/20")

    while True:
        cours = input('Intitulé du cours à ajouter : ')
        try:
            cote = float(input('Côte (sur 20) : '))
            if 0 <= cote <= 20:
                cote_list[cours] = cote
            else:
                print("❌ La côte doit être comprise entre 0 et 20.")
                continue
        except ValueError:
            print("❌ Veuillez entrer une valeur numérique.")
            continue

        ajouter = input('✍️ Ajouter une autre côte (o/n) ? ')
        if ajouter == 'n':
            break

    pourcentage = calculer_moyenne(cote_list.values())

    etudiant["moyenne"] = "{:.2f}".format(pourcentage) + '/100'


def modifier_cote(etudiant):
    """
    Modifie une côte existante pour un étudiant et met à jour sa moyenne.

    :param etudiant: (dict) Dictionnaire contenant les informations de l'étudiant.
    :return: Rien.
    """
    cote_list = etudiant['côtes (sur 20)']

    for cours, cote in cote_list.items():
        print(f"{cours} : {cote}/20")

    while True:
        cours = input('Intitulé du cours à modifier : ')
        if not cote_list.get(cours):
            print(f'Cours "{cours}" non trouvé !')
            continue
        cote = float(input('Côte (sur 20) : '))
        cote_list[cours] = cote

        modifier = input('✍️ Modifier une autre côte (o/n) ? ')
        if modifier == 'n':
            break

    pourcentage = calculer_moyenne(cote_list.values())

    etudiant["moyenne"] = "{:.2f}".format(pourcentage) + '/100'


def supprimer_cote(etudiant):
    """
    Supprime une côte d'un étudiant et met à jour sa moyenne.

    :param etudiant: (dict) Dictionnaire contenant les informations de l'étudiant.
    :return: Rien.
    """
    cote_list = etudiant['côtes (sur 20)']

    for cours, cote in cote_list.items():
        print(f"{cours} : {cote}/20")

    while True:
        cours = input('Intitulé du cours à supprimer : ')
        if not cote_list.get(cours):
            print(f'Cours "{cours}" non trouvé !')
            continue
        # cote = float(input('Côte (sur 20) : '))
        cote_list.pop(cours, None)

        supprimer = input('✍️ Supprimer une autre côte (o/n) ? ')
        if supprimer == 'n':
            break

    pourcentage = calculer_moyenne(cote_list.values())

    etudiant["moyenne"] = "{:.2f}".format(pourcentage) + '/100'


def lire_une_cote(etudiant, cours):
    """
    Récupère la côte d'un étudiant pour un cours spécifique.

    :param etudiant: (dict) Dictionnaire contenant les informations de l'étudiant.
    :param cours: (str) Nom du cours pour lequel on veut récupérer la côte.
    :return: (float | None) La côte du cours ou None si le cours n'existe pas.
    """
    # Vérifier si l'étudiant a bien un dictionnaire de côtes
    if not isinstance(etudiant.get('côtes (sur 20)'), dict):
        return None  # Aucun cours enregistré

    return etudiant['côtes (sur 20)'].get(cours, None)


def trouver_min_max_cotes(etudiant):
    """
    Trouve la matière avec la plus grande et la plus petite côte d'un étudiant.

    :param etudiant: (dict) Dictionnaire contenant les informations de l'étudiant.
    :return: (dict) Contenant les matières et leurs côtes min/max.
    """
    cote_list = etudiant['côtes (sur 20)']
    if not cote_list:
        return {"min": None, "max": None}  # Cas où l'étudiant n'a pas encore de notes

    return {
        "matiere_max": max(cote_list, key=cote_list.get),
        "max_valeur": max(cote_list.values()),
        "matiere_min": min(cote_list, key=cote_list.get),
        "min_valeur": min(cote_list.values())
    }


def moyennes(liste_etudiants):
    """
    Calcule et met à jour la moyenne de tous les étudiants si elle est absente.

    :param liste_etudiants: (list) Liste des étudiants.
    :return: (list) Liste des étudiants mise à jour.
    """
    for etudiant in liste_etudiants:
        if etudiant['côtes (sur 20)'] != {} and etudiant["moyenne"] is None:
            pourcentage = calculer_moyenne(etudiant['côtes (sur 20)'].values())
            etudiant['moyenne'] = "{:.2f}".format(pourcentage) + '/100'
    print("Les moyennes ont été calculées avec succès !")
    return liste_etudiants
