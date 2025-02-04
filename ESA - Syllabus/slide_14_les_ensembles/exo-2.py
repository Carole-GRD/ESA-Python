"""
    Exercice2 :

    Écrire un programme définissant deux types d’ensembles
    composés, d’une part, des consonnes et, d’autre part, des voyelles.
    Après lecture d’une phrase, afficher le nombre de consonnes et de voyelles utilisés et affichez-les.
"""

VOYELLES = set("aeiouy")
CONSONNES = set("bcdfghjklmnpqrstvwxz")

phrase = set(input('Entrez une phrase : ').lower())

consonnes_utilisees = sorted(phrase & CONSONNES)
voyelles_utilisees = sorted(phrase & VOYELLES)

print("Consonnes utilisées : {0}, il y en a {1} d'utilisés".format(consonnes_utilisees, len(consonnes_utilisees)))
print("Voyelles utilisées : {0}, il y en a {1} d'utilisés".format(voyelles_utilisees, len(voyelles_utilisees)))
