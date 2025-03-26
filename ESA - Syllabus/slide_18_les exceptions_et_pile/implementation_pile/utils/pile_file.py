"""
    Module
"""


# Méthode pour gérer une pile
def creer_pile():
    """
    :return: rien, sert à initialiser/créer une pile vide
    """
    # Initialiser une pile vide
    pile = []
    return pile


def sommet(pile):
    """
    :param pile: est une liste
    :return: le sommet de la pile
    """
    try:
        return pile[-1]
    except Exception as e:
        print("Error:", e)


def empiler(pile, element):
    """
    :param pile: est une liste
    :param element: élément à empiler
    :effet: ajoute l'élément sur le sommet de la pile
    """
    pile.append(element)


def depiler(pile):
    """
    :param pile: est une liste
    :effet: enlève l'élément du sommet de la pile (dernier ajouté)
    """
    try:
        pile.pop()
    except Exception as e:
        print("Error:", e)


def est_vide(pile):
    """
    :param pile: est une liste
    :return: true si la liste est vide
    """
    return pile == []


def affiche_pile(pile):
    """
    :param pile: est une liste
    :effet: affiche la pile
    """
    if len(pile) == 0:
        return print("La pile est vide")
    for element in pile[::-1]:
        print(element)
