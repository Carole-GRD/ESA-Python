# -----------------------------------------------------
#                  Challenge
# -----------------------------------------------------


"""
    Consigne :

    Considérons un programme utilisant cinq variables a, b, c, d et e.
    Comment feriez-vous, en utilisant uniquement des if ...: .... else: ...
    pour calculer la médiane de ces cinq valeurs.
"""

"""
    Remarque :

    Calculer la médiane de cinq valeurs avec seulement des if et else
    sans utiliser de listes ou de fonctions comme sorted()
    demande de tester toutes les combinaisons possibles.

    Cela nécessite de nombreux tests conditionnels,
    car il y a plusieurs façons d'obtenir la troisième plus grande valeur
    en fonction des relations entre les variables.
"""

# Réalisé avec les listes et la fonction sorted()


from math import *

# Variables d'entrée
a = 10
b = 2
c = 4
d = 8
e = 6

# Création de la liste de nombres
numbers_list = [a, b, c, d, e]

# numbers_list.append(7)
# numbers_list.append(12)


# Tri de la liste
sorted_list = sorted(numbers_list)

# Calcul de la médiane
median = sorted_list[floor(len(sorted_list) / 2)]

# Code principal pour affichage
if __name__ == '__main__':
    print("Liste originale :", numbers_list)
    print("Liste triée :", sorted_list)
    print("Médiane :", median)