"""
    Exercices 5 :

    Écrire un programme déterminant si un nombre entier, fourni par l’utilisateur, est premier ou non.
"""

# n = int(input("Entrez un nombre entier : "))
#
# if n == 0 or n == 1:
#     print(f"{n} n'est pas premier")
# else:
#     for i in range(2, n+1):
#         if i == n:
#             print(f"{n} est premier")
#             break
#         if n % i == 0:
#             print(f"{n} n'est pas premier")
#             break

# ==============================================================================

# is_prime = ""
# n = int(input("Entrez un nombre entier : "))
#
# if n == 0:
#     is_prime = ("0 ne peut pas être divisé par lui-même, "
#                 "car la division par 0 est une opération non définie. "
#                 "Il n'est donc pas un nombre premier.")
# elif n == 1:
#     is_prime = ("Le nombre 1 n'est pas considéré comme étant un nombre premier, "
#                 "car il ne possède pas 2 diviseurs différents. "
#                 "En effet, il n'a que 1 comme diviseur.")
# else:
#     for i in range(2, n+1):
#         if i == n:
#             is_prime = (f"{n} est un nombre premier \n"
#                         f"Diviseurs de {n} : ") + "{1, " + f"{n}" + "}"
#             break
#         if n % i == 0:
#             is_prime = (f"{n} est divisible par {i} car {i} x {round(n / i)} = {n} \n"
#                         f"{n} n'est donc pas un nombre premier")
#             break
#
# print(is_prime)

# ==============================================================================

# is_prime = ""
# n = int(input("Entrez un nombre entier : "))
#
# if n == 0:
#     is_prime = ("0 ne peut pas être divisé par lui-même, "
#                 "car la division par 0 est une opération non définie. "
#                 "Il n'est donc pas un nombre premier.")
# elif n == 1:
#     is_prime = ("Le nombre 1 n'est pas considéré comme étant un nombre premier, "
#                 "car il ne possède pas 2 diviseurs différents. "
#                 "En effet, il n'a que 1 comme diviseur.")
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             is_prime = (f"{n} est divisible par {i} car {i} x {round(n / i)} = {n} \n"
#                         f"{n} n'est donc pas un nombre premier")
#             break
#     if is_prime == "":
#         is_prime = (f"{n} est un nombre premier \n"
#                     f"Diviseurs de {n} : ") + "{1, " + f"{n}" + "}"
#
# print(is_prime)

# ==============================================================================

import math


def check_prime(number_checked):

    if number_checked < 2:
        if number_checked == 0:
            return ("0 ne peut pas être divisé par lui-même, "
                    "car la division par 0 est une opération non définie. "
                    "Il n'est donc pas un nombre premier.")
        elif number_checked == 1:
            return ("Le nombre 1 n'est pas considéré comme étant un nombre premier, "
                    "car il ne possède pas 2 diviseurs différents. "
                    "En effet, il n'a que 1 comme diviseur.")
    else:
        # Calculer la racine carrée de "number_checked"
        # réduit le nombre d'itérations nécessaires pour vérifier si c'est un nombre premier.
        for i in range(2, int(math.sqrt(number_checked)) + 1):
            if number_checked % i == 0:
                # Utiliser la division entière (//) pour éviter l'appel à round
                return (f"{number_checked} est divisible par {i} car {i} x {number_checked // i} = {number_checked} \n"
                        f"{number_checked} n'est donc pas un nombre premier.")
        return (f"{number_checked} est un nombre premier \n"
                f"Diviseurs de {number_checked} : {{1, {number_checked}}}")


# Exécution du code
n = int(input("Entrez un nombre entier : "))
print(check_prime(n))
