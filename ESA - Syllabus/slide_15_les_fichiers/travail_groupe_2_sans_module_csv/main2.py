"""
    Travail de groupe N°2 :

    Sur Smartschool, reprenez les fichiers :
        ✔️ ssh_config
        ✔️ ssh_config_template

    ● À l'aide du fichier "ssh_config_template" créez un dictionnaire "dico_ssh_config"
      ayant comme clé les entrées (ligne 22 à 52 … mais attention, on veut toutes les lignes même celles commentées).

    ● À l'aide du fichier "ssh_config" créez une liste d'hôte reprenant les infos
      qui seront placées dans un dictionnaire "ssh_config_template"

    ● A vous de gérer les entrées manquantes.

    ● Répondez aux questions suivantes (en utilisant la liste fraîchement créée) :
        ✔️ Combien d'hôtes différents sont définis ?
        ✔️ Quels sont leurs noms ?
        ✔️ Combien de fois retrouvons-nous l'user "etd-esa" ?

    ● Chaque question fera l'objet d'une routine qui lui sera propre
      (étanche, correctement documentée, avec le pseudo-code & l'algorigramme …).
"""

# 1. Création du dictionnaire à partir de ssh_config_template
dico_ssh_config_template = {}
with open('ssh_config_template', 'r') as fichier:
    lignes = fichier.readlines()

    for ligne in lignes[21:]:
        # Supprimer les espaces, retirer les 4 premiers caractères et diviser la ligne en elements.
        element = ligne.strip('\n')[4:].split()
        dico_ssh_config_template[element[0]] = element[1:] if (len(element[1:]) > 1) else element[1]

# 2. Création de la liste des hôtes à partir de ssh_config
liste_hotes = []
with open('ssh_config', 'r') as fichier:
    lignes = fichier.readlines()

    for ligne in lignes:
        new_ligne = ligne.strip('\n')

        if new_ligne.startswith('Host '):
            # Si c'est une nouvelle configuration, alors on crée un nouveau dictionnaire
            dico_ssh_config = {}
            new_ligne_split = new_ligne.split(' ')
            dico_ssh_config[new_ligne_split[0]] = new_ligne_split[1]
        elif new_ligne:
            new_ligne_split = new_ligne.strip().split(' ')
            dico_ssh_config[new_ligne_split[0]] = new_ligne_split[1]
        elif not new_ligne:
            # Si la ligne est vide, c'est la fin de la configuration et on ajoute le dictionnaire à la liste
            liste_hotes.append(dico_ssh_config)

# 3. Complétion des configurations avec le template
configurations_hotes = []
for config_hote in liste_hotes:
    # Fusionne le template avec les données de l'hôte (priorité aux valeurs de l'hôte)
    merged_config = dico_ssh_config_template | config_hote  # opérateur | à partir de Python 3.9
    configurations_hotes.append(merged_config)


# 4. Fonctions pour répondre aux questions
def compter_hotes(hotes):
    """
    :param hotes: (list) Liste des dictionnaires contenant les configurations des hôtes
    :return: (int) Nombre d'hôtes
    """
    return len(hotes)


def obtenir_noms_hotes(hotes):
    """
    :param hotes: (list) Liste des dictionnaires contenant les configurations des hôtes
    :return: (list) Liste des noms des hôtes
    """
    noms = []
    for hote in hotes:
        noms.append(hote.get('Host', ''))
    return ', '.join(noms)


def compter_utilisateur(hotes, utilisateur):
    """
    :param hotes: (list) Liste des dictionnaires contenant les configurations des hôtes
    :param utilisateur: (str) Nom de l'utilisateur à rechercher
    :return: (int) Nombre d'occurrences de l'utilisateur
    """
    nombre = 0
    for hote in hotes:
        if hote.get('User', '') == utilisateur:
            nombre += 1
    return nombre


# 5. Affichage des résultats
print(f"Nombre d'hôtes : {compter_hotes(configurations_hotes)}")
print(f"Noms des hôtes : {obtenir_noms_hotes(configurations_hotes)}")
print(f"Nombre de user \"etd-esa\" : {compter_utilisateur(configurations_hotes, 'etd-esa')}")
