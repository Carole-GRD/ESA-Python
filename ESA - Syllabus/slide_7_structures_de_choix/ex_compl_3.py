"""
    Exercice3 :

    Ecrire un programme qui résout l' équation AX+B=0.

    N'oubliez pas tous les cas particuliers !

    Notamment les cas "tout x est solution" et "pas de solution".
"""

a, b = input("Entrez les valeurs A et B (séparées par un espace) de l'équation Ax + B = 0 ").split(' ')
a, b = float(a), float(b)

if a == 0:
    if b == 0:
        print("Tout X est solution")
    else:
        print("Pas de solution")
else:
    print("La solution est x=-B/A : ", -b/a)
