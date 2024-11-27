"""
    Exercice 5 :

    Faire un programme permettant de compter le nombre de voyelles
    et le nombre de consonnes que possède une chaîne de caractère encodée par l'utilisateur.
"""

import unicodedata

VOYELLES = ["a", "e", "i", "o", "u", "y"]
CONSONNES = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]

phrase = input("Encodez une phrase : ")

cpt_voyelle = 0
cpt_consonne = 0
phrase = unicodedata.normalize('NFD', phrase).encode('ascii', 'ignore').decode("utf-8")

for caractere in phrase[0:]:
    if caractere.lower() in VOYELLES:
        cpt_voyelle += 1
    elif caractere.lower() in CONSONNES:
        cpt_consonne += 1
        # c'est un caractère autre

print("Le nombre de voyelle est {} ".format(cpt_voyelle))
print("Le nombre de consonne est {} ".format(cpt_consonne))
