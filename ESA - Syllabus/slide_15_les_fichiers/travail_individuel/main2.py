"""
    Travail Individuel :

    Sur Smartschool, reprenez le fichier "fstab".

    Après avoir analysé et compris sa structure, répondez aux questions suivantes :
        ● Combien d'infos devons-nous avoir par entrée ?
        ● Combien d'entrée avons-nous ?
        ● Est-ce que toutes les entrées ont le bon nombre d'infos ?
        ● Affichez les infos par entrée (soignez la présentation).

        ● Comme pour le travail de groupe N°2, chaque question fera l'objet d'une routine
          qui lui sera propre (étanche, correctement documentée, avec le pseudo-code ou l'algorigramme …).
"""


# def compter_entrees(lignes):
#     """
#     Compte le nombre total d'entrées dans une liste de lignes non vides et non-commentées.
#
#     :param lignes: (list) Liste des lignes extraites du fichier fstab.
#     :return: (int) Nombre total d'entrées valides.
#     """
#     return len(lignes)


def compter_infos_attendues(infos_attendues):
    """
    Détermine le nombre d'informations attendues par entrée en analysant la ligne de définition dans fstab.

    :param infos_attendues: (str) Chaine de caractères, extraite du fichier fstab, contenant les différentes infos.
    :return: (int) Le nombre d'informations attendues par entrée.
    """
    champs = []
    start = None  # Position du dernier '<'

    # Parcourir la ligne caractère par caractère
    for i, char in enumerate(infos_attendues):
        if char == '<':  # Démarrage d'un champ
            start = i
        elif char == '>' and start is not None:  # Fin d'un champ
            champs.append(infos_attendues[start:i+1])  # Ajouter le champ trouvé (ex.: <file system>)
            start = None  # Réinitialiser

    return len(champs)  # Retourner le nombre de champs trouvés


def verifier_nb_entrees(lignes, nb_infos_attendues):
    """
    Vérifie si toutes les entrées ont le nombre d'informations attendues.

    :param lignes: (list) Liste des lignes extraites du fichier fstab.
    :param nb_infos_attendues: (int) Nombre d'informations attendues par entrée.
    :return: (bool) True si toutes les entrées ont le bon nombre d'informations, False sinon.
    """
    return all(len(ligne.split()) == nb_infos_attendues for ligne in lignes)


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
        # if len(elements) < 6:
        #     print("    ATTENTION : Cette entrée ne contient pas 6 informations.")
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

    :param fichier: (str) Chemin vers le fichier fstab.
    :return: (list) Une liste contenant les lignes utiles du fichier fstab.
             Si le fichier n'existe pas ou est inaccessible, retourne une liste vide.
    """
    with open(fichier, 'r') as f:
        lignes = f.readlines()
        entrees = []
        infos_attendues = ''
        for ligne in lignes:
            if ligne.strip() and not ligne.startswith('#'):
                entrees.append(ligne.strip())
            elif ligne.strip().startswith("#") and "<file system>" in ligne:
                infos_attendues += ligne[2:]
        return entrees, infos_attendues


# Script principal
entrees, infos_attendues = lire_fstab('fstab')
print(f"Combien d'entrée avons-nous ? {len(entrees)}")
# print(f"Combien d'entrée avons-nous ? {compter_entrees(entrees)}")
nb_infos_attendues = compter_infos_attendues(infos_attendues)
print(f"Combien d'infos devons-nous avoir par entrée ? {nb_infos_attendues}")
print(f"Est-ce que toutes les entrées ont le bon nombre d'infos ? "
      f"{'oui' if verifier_nb_entrees(entrees, nb_infos_attendues) else 'non'}")
print("\n")
afficher_infos_par_entree(entrees)
