"""
    Exercice 4 :

    Écrire un programme permettant de lire une phrase et de la mettre en Majuscule.

"""


def to_capitalize():
    phrase = input("Entrez une phrase : ")
    uppercase = phrase.upper()
    print(f"Phrase en majuscules : {uppercase}")


to_capitalize()
