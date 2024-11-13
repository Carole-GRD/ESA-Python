"""
    Exercice2 :

    Écrire un programme qui demande à l'utilisateur de taper 5 nombres et qui affiche le plus grand.

    Contrainte imposée : Le programme ne devra utiliser que 2 variables.
"""

nombre = int(input('Nombre 1 : '))
maxi = nombre

nombre = int(input('Nombre 2 : '))
if nombre > maxi:
    maxi = nombre

nombre = int(input('Nombre 3 : '))
if nombre > maxi:
    maxi = nombre

nombre = int(input('Nombre 4 : '))
if nombre > maxi:
    maxi = nombre

nombre = int(input('Nombre 5 : '))
if nombre > maxi:
    maxi = nombre

print('Le nombre le plus grand est : ', maxi)
