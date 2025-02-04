"""
    Exercice 3 :

    Soit un tableau "tab_nbr" de N entiers, écrire une fonction récursive simple
    permettant de déterminer le maximum du tableau (astuce : essayer le principe de dichotomie)
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


nbr_elt = randint(1, 10)
tab_nbr = initialize(nbr_elt, 0, 20)
print(tab_nbr)


# ================================================================================
# ================================  MA VERSION ===================================
# ================================================================================

# def find_max(tab):
#     if len(tab) == 1:
#         return tab[0]
#     else:
#         milieu = len(tab) // 2
#         gauche = tab[:milieu]
#         droite = tab[milieu:]
#         if find_max(gauche) > find_max(droite):
#             return find_max(gauche)
#         else:
#             return find_max(droite)
#
#
# print(f"find_max : {find_max(tab_nbr)}")

""" 
    Problème potentiel !
    
    J'appelle la fonction find_max trois fois dans chaque étape :
    
        if find_max(gauche) > find_max(droite):
            return find_max(gauche)
        else:
            return find_max(droite)

    Cela signifie que je calcule deux fois le maximum pour chaque sous-tableau (gauche et droite),
    ce qui peut être inefficace. 

"""


# ================================================================================
# ================================  CORRECTION ===================================
# ================================================================================

# def find_max(tab):
#     if len(tab) == 1:
#         return tab[0]
#     else:
#         milieu = len(tab) // 2
#         gauche = tab[:milieu]
#         droite = tab[milieu:]
#
#         # Calculer une seule fois le maximum de chaque sous-tableau
#         max_gauche = find_max(gauche)
#         max_droite = find_max(droite)
#
#         # Comparer et retourner le maximum
#         if max_gauche > max_droite:
#             return max_gauche
#         return max_droite
#
#
# print(f"find_max : {find_max(tab_nbr)}")


# ================================================================================
# ==============================  AMELIORATIONS ==================================
# ================================================================================

def maximum(tab_nbr):
    """
    Calcule récursivement le maximum d'un tableau d'entiers en utilisant le principe de dichotomie.

    :param tab_nbr:
        (list of int) Un tableau d'entiers dont on veut trouver le maximum.

    :return:
        (int) Le maximum des éléments du tableau.
    """

    # Cas de base : tableau avec un seul élément
    if len(tab_nbr) == 1:
        return tab_nbr[0]

    # Diviser le tableau en deux moitiés
    milieu = len(tab_nbr) // 2
    gauche = tab_nbr[:milieu]
    droite = tab_nbr[milieu:]

    # Appels récursifs sur chaque moitié
    max_gauche = maximum(gauche)
    max_droite = maximum(droite)

    # Comparer les deux résultats pour trouver le maximum
    return max(max_gauche, max_droite)


print(f"Maximum = {maximum(tab_nbr)}")


# ================================================================================
# ===============================  EXPLICATIONS ==================================
# ================================================================================

"""
        - Si le tableau contient un seul élément, cet élément est retourné directement.
        
        - La fonction divise le tableau en deux parties, traite chaque moitié récursivement,
          puis compare les résultats pour déterminer le maximum global.
          
        - Ce processus de division et de comparaison est effectué jusqu'à ce qu'il ne reste plus
          qu'un seul élément dans le tableau (cas de base).
"""