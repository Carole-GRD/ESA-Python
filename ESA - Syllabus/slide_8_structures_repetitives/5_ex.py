"""
    Exercices 5 :

    Écrire un programme déterminant si un nombre entier, fourni par l’utilisateur, est premier ou non.
"""

n = int(input("Entrez un nombre entier : "))

if n == 0 or n == 1:
    print(f"{n} n'est pas premier")
else:
    for i in range(2, n+1):
        if i == n:
            print(f"{n} est premier")
            break
        if n % i == 0:
            print(f"{n} n'est pas premier")
            break
