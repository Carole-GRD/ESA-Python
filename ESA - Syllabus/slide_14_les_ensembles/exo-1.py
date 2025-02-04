"""
    Exercice1 :

    Écrire un programme qui lit une phrase et qui affiche, par ordre alphabétique,
    les lettres (minuscules) que la phrase ne contient pas.
    Les lettres Majuscules utilisées dans la phrase compteront comme minuscules.
"""

lettre = set("abcdefghijklmnopqrstuvwxyz")
phrase = set(input('Entrez une phrase : ').lower())
# Exemple :
# Les lettres Majuscules utilisées dans la phrase compteront comme minuscules.

ensemble = sorted(lettre - phrase)
print(ensemble)  # ['b', 'f', 'g', 'k', 'q', 'v', 'w', 'x', 'y', 'z']
