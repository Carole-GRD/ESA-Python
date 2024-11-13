"""
    Exercice 4 :

    Écrivez un programme invitant l’utilisateur à introduire deux nombres entiers
    et afficher si le premier nombre est un multiple du second.
"""

while True:
    nbr1, nbr2 = map(int, input("Entrez deux nombres entiers séparés par un espace : ").split(" "))
    if nbr2 != 0:
        break
    else:
        print("Le second nombre ne peut pas être nul. -> Division par zéro impossible !")

if nbr1 % nbr2 == 0:
    print(nbr1 % nbr2)
    print(f"{nbr1} est un mulitple de {nbr2}")
else:
    print(nbr1 % nbr2)
    print(f"{nbr1} n'est pas un mulitple de {nbr2}")


# Réponse du professeur - Attention : vérifier condition (b % a) == 0
# a, b = input("Introduisez vos deux entiers séparés par un slash (/) : ").split('/')
# a, b = int(a), int(b)
#
# if (a != 0) and (b != 0) and ((b % a) == 0):
#     print("a : ", a, " est un multiple de b : ", b)
# else:
#     print("a : ", a, " n'est pas un multiple de b : ", b)


