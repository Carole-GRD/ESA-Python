"""
    Travail Individuel :

    Sur Smartschool, reprenez le fichier "fstab".

    Après avoir analysé et compris sa structure, répondez aux questions suivantes :
        ● Combien d'infos devons-nous avoir par entrée ?                  (6 ?)
        ● Combien d'entrée avons-nous ?                                   (3 ?)
        ● Est-ce que toutes les entrées ont le bon nombre d'infos ?       (non, pas la dernière qui n'en a que 5 ?)
        ● Affichez les infos par entrée (soignez la présentation).

        ● Comme pour le travail de groupe N°2, chaque question fera l'objet d'une routine
          qui lui sera propre (étanche, correctement documentée, avec le pseudo-code ou l'algorigramme …).
"""


def compter_entrees(lignes):
    """
    Compte le nombre total d'entrées dans une liste de lignes non vides et non-commentées.

    :param lignes: (list) Liste des lignes extraites du fichier fstab.
    :return: (int) Nombre total d'entrées.
    """
    return len(lignes)


def compter_infos_par_entree(lignes):
    nb_infos = []
    for element in lignes:
        entree = element.split()
        nb_infos.append(len(entree))
    return nb_infos


def verifier_nb_entrees(lignes):
    """
    Vérifie si toutes les entrées ont le même nombre d'informations.

    :param lignes: (list) Liste des lignes extraites du fichier fstab.
    :return: (bool) True si toutes les entrées ont le même nombre d'informations, False sinon.
    """
    nb_infos = compter_infos_par_entree(lignes)
    return len(set(nb_infos)) == 1


def afficher_infos_par_entree(lignes):
    """
    Affiche les informations détaillées de chaque entrée du fichier fstab de manière formatée.

    :param lignes: (list) Liste des lignes extraites du fichier fstab.
    :return: None. Cette fonction affiche directement les informations au lieu de les retourner.
    """
    print("Affichage des informations par entrée :")
    for i, ligne in enumerate(lignes, 1):
        elements = ligne.split()
        print(f"\nEntrée {i}:")
        print(f"    Système de fichiers : {elements[0]}")
        print(f"    Point de montage    : {elements[1]}")
        print(f"    Type                : {elements[2]}")
        print(f"    Options             : {elements[3]}")
        if len(elements) > 4:
            print(f"    Dump                : {elements[4]}")
        if len(elements) > 5:
            print(f"    Pass                : {elements[5]}")


def lire_fstab(fichier):
    """
    Lit le contenu du fichier fstab et retourne une liste de lignes non vides et non-commentées.

    :param fichier: (str) chemin vers le fichier fstab
    :return: (list) Une liste contenant les lignes utiles du fichier fstab.
    """
    with open(fichier, 'r') as f:
        lignes = [ligne.strip() for ligne in f if ligne.strip() and not ligne.startswith('#')]
    return lignes, colonnes


lignes = lire_fstab('fstab')
print(f"Combien d'entrée avons-nous ? {compter_entrees(lignes)}")
print(f"Combien d'infos devons-nous avoir par entrée ? {compter_infos_par_entree(lignes)}")
print(f"Est-ce que toutes les entrées ont le bon nombre d'infos ? {'oui' if verifier_nb_entrees(lignes) else 'non'}")
print("\n")
afficher_infos_par_entree(lignes)


"""
Explication du retour de la fonction verifier_nb_entrees()
[6, 6, 5]
En convertissant cette liste en un ensemble (set), on élimine automatiquement les doublons. 
[6, 5]
Si l'ensemble contient exactement un élément, cela signifie que toutes les entrées ont le même nombre d'informations.
len([6, 5]) == 1    => False
"""
