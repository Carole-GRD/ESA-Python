"""
    Exercice 1 :

    Comparez la condition de terminaison de la boucle repeat (n > 0)
    et la condition de continuation de la boucle while (n <= 0).

    Si nous représentions, sous forme d’ensemble, les valeurs autorisées par cette condition,
    que diriez-vous sur ces 2 ensembles ?

    Comment passeriez-vous d'une expression à l'autre ?
"""

# condition de terminaison
# On simule une boucle repeat qui continue jusqu'à ce que n > 0
while True:
    n1 = int(input("Entrez un nombre positif : "))
    if n1 > 0:
        break

# condition de continuation
n2 = int(input("Entrez un nombre positif : "))
while n2 <= 0:
    n2 = int(input("On a dit un nombre positif : "))


# Autre version


# n = -5  # Exemple de valeur initiale
#
# # Boucle repeat
# while True:  # On simule une boucle repeat qui continue jusqu'à ce que n > 0
#     print(f"Dans la boucle repeat : n = {n}")
#     n += 1
#     if n > 0:  # Condition de terminaison de la boucle repeat
#         break
#
# # Boucle while avec condition de continuation équivalente
# n = -5  # On réinitialise n pour comparaison
# while n <= 0:  # Condition de continuation de la boucle while
#     print(f"Dans la boucle while : n = {n}")
#     n += 1

