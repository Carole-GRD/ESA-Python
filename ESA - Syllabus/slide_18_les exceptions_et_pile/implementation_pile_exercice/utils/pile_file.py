"""
    Module : Méthode pour gérer une pile
"""


# TODO : vérifier si la valeur par défaut est nécessaire
def creer_pile(taille_max=None):
    """
    :param taille_max: La taille maximum de la pile
    :return: Une pile vide représentée par une liste, avec sa taille maximale
    """
    return {"pile": [], "taille_max": taille_max}


def sommet(pile):
    """
    :param pile: La pile (dictionnaire contenant la liste et la taille max)
    :return: L'élément au sommet de la pile (dernier ajouté)
    """
    try:
        if not est_vide(pile):
            return pile["pile"][-1]
        else:
            raise IndexError("La pile est vide, pas de sommet à renvoyer.")
    except IndexError as e:
        print("Erreur :", e)


def empiler(pile, element):
    """
    Empile un élément sur le sommet de la pile.
    :param pile: La pile (dictionnaire contenant la liste et la taille max)
    :param element: L'élément à empiler
    """
    try:
        if est_pleine(pile):
            raise ValueError("La pile est pleine, impossible d'empiler.")
        pile["pile"].append(element)
    except ValueError as e:
        print("Erreur :", e)


def depiler(pile):
    """
    Dépile l'élément du sommet de la pile.
    :param pile: La pile (dictionnaire contenant la liste et la taille max)
    """
    try:
        if est_vide(pile):
            raise IndexError("La pile est vide, impossible de dépiler.")
        pile["pile"].pop()
    except IndexError as e:
        print("Erreur :", e)


# TODO : voir quel est le meilleur code (voir return)
def est_vide(pile):
    """
    :param pile: La pile (dictionnaire contenant la liste et la taille max)
    :return: True si la pile est vide, False sinon
    """
    # return pile["pile"] == []
    return len(pile["pile"]) == 0


def est_pleine(pile):
    """
    :param pile: La pile (dictionnaire contenant la liste et la taille max)
    :return: True si la pile est pleine, False sinon
    """
    return len(pile["pile"]) == pile["taille_max"]


def taille_maximum(pile):
    """
    :param pile: La pile (dictionnaire contenant la liste et la taille max)
    :return: La taille maximum de la pile
    """
    return pile["taille_max"]


# TODO : vérifier si ce n'est pas mieux de copier la pile avec sa taille maximum
def copier(source, cible):
    """
    Copie une pile source vers une pile cible.
    :param source: La pile source (dictionnaire contenant la liste et la taille max)
    :param cible: La pile cible (doit être au moins de la même taille)
    """
    try:
        if taille_maximum(cible) is not None and taille_maximum(cible) < taille_maximum(source):
            raise ValueError("La pile cible est trop petite pour recevoir la copie.")
        cible["pile"] = source["pile"].copy()
        # cible["taille_max"] = source["taille_max"]
    except ValueError as e:
        print("Erreur :", e)


def afficher_pile(pile):
    """
    Affiche le contenu de la pile.
    :param pile: La pile (dictionnaire contenant la liste et la taille max)
    """
    if est_vide(pile):
        print("La pile est vide.")
    else:
        for element in reversed(pile["pile"]):
            print(element)
