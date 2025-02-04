"""
    Exercice 2 :

    Soit un tableau de nombre tab_nbr. Rendre récursive la fonction somme suivante :

    def somme(tab_nbr):
        s = 0
        for nbr in tab_nbr:
            s += nbr
        return s
"""


# ================================================================================
# ================= INITIALISATION D'UN TABLEAU ALÉATOIRE  =======================
# ================================================================================

from random import randint


def initialize(nbr_elt, _min, _max):
    """
    Génère un tableau de nombres aléatoires.

    :param nbr_elt: (int) Le nombre d'éléments à générer dans le tableau.
    :param _min: (int) La valeur minimale possible pour les nombres générés.
    :param _max: (int) La valeur maximale possible pour les nombres générés.
    :return: (list) Un tableau contenant `nbr_elt` nombres aléatoires compris entre `_min` et `_max`.
    """
    t = []
    for i in range(nbr_elt):
        t.append(randint(_min, _max))
    return t


nbr_elt = randint(0, 4)
tab = initialize(nbr_elt, 0, 10)
print(tab)


# ================================================================================
# ================================  MA VERSION ===================================
# ================================================================================

def somme(tab_nbr):
    """
    Calcule récursivement la somme des éléments d'un tableau.

    :param tab_nbr: (list) Un tableau de nombres.
    :return: (int) La somme des éléments du tableau (0 si le tableau est vide).
    """
    if not tab_nbr:     # Cas de base : tableau vide
        return 0
    return tab_nbr[0] + somme(tab_nbr[1:])


tab_somme = somme(tab)
print(f"Somme = {tab_somme}")


"""
    Visualisation de la pile d'appels
    
    La récursivité fonctionne comme une pile : 
        chaque appel de fonction est empilé jusqu'à atteindre le cas de base, 
        puis les appels sont résolus dans l'ordre inverse. Voici une représentation :

    Empilement (descente) :
        somme([3, 7, 2, 10])
        somme([7, 2, 10])
        somme([2, 10])
        somme([10])
        somme([])
        
    Résolution (remontée) :
        somme([]) -> 0
        somme([10]) -> 10 + 0 = 10
        somme([2, 10]) -> 2 + 10 = 12
        somme([7, 2, 10]) -> 7 + 12 = 19    
        somme([3, 7, 2, 10]) -> 3 + 19 = 22 
        
    Résumé
        - La fonction somme décompose le problème (somme d'un tableau) 
          en petits sous-problèmes (somme du premier élément avec le reste).
        - La récursion s'arrête lorsqu'elle atteint un tableau vide (cas de base).
        - Les résultats sont ensuite combinés lors de la remontée dans la pile d'appels.
"""