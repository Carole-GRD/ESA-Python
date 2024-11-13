"""
    Exercice1 :

    Écrire un programme qui demande à l’utilisateur de saisir un nombre N
    puis qui affiche "ERREUR" si N n'est pas un nombre impair compris entre 27 et 85 bornes incluses.
    Dans le cas contraire, on affiche "PAS D'ERREUR".
"""

NBR_MIN = 27
NBR_MAX = 85
nombre = int(input('Quel est votre nombre ? '))

if ((nombre % 2) == 0) or (nombre < NBR_MIN) or (nombre > NBR_MAX):
    print("erreur")
else:
    print("pas d'erreur")


# Loi de De Morgan

# if not ((nombre % 2) != 0 and (nombre >= NBR_MIN) and (nombre <= NBR_MAX)):
if not ((nombre % 2) != 0 and NBR_MIN <= nombre <= NBR_MAX):
    print("erreur")
else:
    print("pas d'erreur")


