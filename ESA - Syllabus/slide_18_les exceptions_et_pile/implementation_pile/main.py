"""

    Dans Python, on n’a pas à se préoccuper de l’implémentation de la pile,
    étant donné que ce type de structure de données est déjà fourni et prêt à l’emploi (type list).

    Il est cependant intéressant de comprendre comment une pile est implémentée.

    Exercice1 :

    Implémentation d’une pile à l’aide d’une liste.

"""

from utils.pile_file import *

ma_pile = creer_pile()

print(est_vide(ma_pile))

print('sommet ma_pile : ', sommet(ma_pile))  # None
print('sommet Hello', sommet('Hello'))       # o

for caractere in 'Hello':
    empiler(ma_pile, caractere)

print('sommet ma_pile : ', sommet(ma_pile))  # o
affiche_pile(ma_pile)

print(est_vide(ma_pile))

depiler(ma_pile)
print('sommet ma_pile : ', sommet(ma_pile))  # l

affiche_pile(ma_pile)

for i in range(5):
    depiler(ma_pile)

affiche_pile(ma_pile)
