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

dico_ssh_config_template = {}
with open('ssh_config_template', 'r') as fichier:
    lignes = fichier.readlines()

    for ligne in lignes[21:]:
        new_ligne = ligne.replace('\n', '')
        new_ligne = new_ligne[4:]
        elements = new_ligne.split()
        # clé = valeur (s'il y a plusieurs valeurs, on aura un tableau au sinon on aura juste la valeur)
        dico_ssh_config_template[elements[0]] = elements[1:] if (len(elements[1:]) > 1) else elements[1]

# print(dico_ssh_config_template)
# for key in dico_ssh_config_template:
#     print(key, dico_ssh_config_template[key])

liste_hotes = []
with open('ssh_config', 'r') as fichier:
    lignes = fichier.readlines()

    for ligne in lignes:
        new_ligne = ligne.replace('\n', '')

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

# print(liste_hotes)
# for dico in liste_hotes:
#     print(dico)
#     for key in dico:
#         print(key, dico[key])

liste_hotes_complete = []
for dico in liste_hotes:
    dico_complet = dico_ssh_config_template | dico
    liste_hotes_complete.append(dico_complet)

# print(liste_hotes_complete)
# for dico in liste_hotes_complete:
#     print(dico)


def compter_hotes(hotes):
    """
    :param hotes: (list) la liste des hôtes
    :return: (int) le nombre d'hôtes dans la liste
    """
    return len(hotes)


# nombre_d_hotes = compter_hotes(liste_hotes_complete)
# print(f"Nombre d'hôtes : {nombre_d_hotes}")
# print(f"Type - Nombre d'hôtes : {type(nombre_d_hotes)}")


def obtenir_noms_hotes(hotes):
    """
    :param hotes: (list) la liste des hôtes
    :return noms: (list) un tableau contenant les noms des hôtes
    """
    noms = []
    for hote in hotes:
        noms.append(hote['Host'])
    return noms
    # return [hote["Host"] for hote in hotes]    -> en une seule ligne


# noms_des_hotes = obtenir_noms_hotes(liste_hotes_complete)
# print(f"Noms des hôtes : {", ".join(noms_des_hotes)}")


def compter_utilisateur(hotes, utilisateur):
    """
    :param hotes: (list) la liste des hôtes
    :param utilisateur: l'utilisateur à rechercher
    :return nombre: (int) le nombre d'hôtes dont la clé 'User' à la valeur 'etd-esa'
    """
    nombre = 0
    for hote in hotes:
        if hote['User'] == utilisateur:
            nombre += 1
    return nombre
    # return sum(1 for hote in hotes if hote.get("User") == utilisateur)    -> en une seule ligne


# nombre_etd_esa = compter_utilisateur(liste_hotes_complete, 'etd-esa')
# print(f"Nombre de user \"etd-esa\" : {nombre_etd_esa}")


print(f"Nombre d'hôtes : {compter_hotes(liste_hotes_complete)}")
print(f"Noms des hôtes : {", ".join(obtenir_noms_hotes(liste_hotes_complete))}")
print(f"Nombre de user \"etd-esa\" : {compter_utilisateur(liste_hotes_complete, 'etd-esa')}")
