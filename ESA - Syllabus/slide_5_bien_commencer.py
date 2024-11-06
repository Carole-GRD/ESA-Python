"""
    Silde 5 - Diapo 45

    Écrivez un programme permettant d'afficher le plus grand
    nombre entier et le plus petit nombre entier.
"""

import sys

# Afficher le plus grand entier
print("Le plus grand entier en Python :")
print(sys.maxsize)

# Afficher le plus petit entier
print("\nLe plus petit entier en Python :")
print(-sys.maxsize - 1)

# Afficher des informations supplémentaires
print("\nInformations supplémentaires :")
print(f"Nombre de bits utilisés pour représenter un entier : {sys.int_info.bits_per_digit}")
print(f"Taille maximale d'un entier en octets : {sys.int_info.sizeof_digit}")

print("\nNote : Python 3 utilise des entiers de précision arbitraire.")
print("Cela signifie qu'il n'y a pas de limite supérieure théorique,")
print("mais il y a des limites pratiques basées sur la mémoire disponible.")

# print("\n=========================================================\n")
#
# print(f"sys.maxsize: {sys.maxsize}")
# print(f"Type de sys.maxsize: {type(sys.maxsize)}")
#
# big_number = sys.maxsize ** 2
# print(f"\nsys.maxsize ** 2: {big_number}")
# print(f"Type de sys.maxsize ** 2: {type(big_number)}")
#
# print("\nTentons de créer un nombre encore plus grand:")
# very_big_number = 2 ** 1000
# print(f"2 ** 1000: {very_big_number}")
# print(f"Nombre de chiffres dans 2 ** 1000: {len(str(very_big_number))}")
#
# print("\nNous pouvons aller encore plus loin:")
# incredibly_big_number_1 = 2 ** 10000
# incredibly_big_number_2 = 2 ** 14284
# print(f"Nombre de chiffres dans 2 ** 10000: {len(str(incredibly_big_number_1))}")
# print(f"Nombre de chiffres dans 2 ** 14284: {len(str(incredibly_big_number_2))}")


# =========================================================================================
# =========================================================================================
# =========================================================================================


"""
        Silde 5 - Diapo 45

        Programme qui permet d’échanger le contenu de deux variables
"""


# ========================
#       Solution
# ========================

# a, b = input("Entrez deux nombres entiers séparés par un espace : ").split(" ")
# print("Avant traitement, A=", a, "B = ", b)
# a, b = b, a
# print("Après traitement, A=", a, "B = ", b)


# ========================
# Avec troisième variable
# ========================

# a = 3
# b = 7
# a = "trois"
# b = "sept"

# c = a
# a = b
# b = c
# print('a = ', a)
# print('b = ', b)


# ========================
# SANS troisième variable
# ========================


# -------
# NUMBER
# -------

# a = 3
# b = 7

# a = a + b
# b = a - b
# a = a - b
# print('a = ', a)
# print('b = ', b)


# ------------
# NUMBER (XOR)
# ------------
# explication voir ESA-Syllabus/slide_7_algebre_de_bool.py
# a = 2
# b = 5
# print('a = ', a, ' b = ',b)
# a = a ^ b
# b = a ^ b
# a = a ^ b
# print('a = ', a, ' b = ',b)


# -------
# STRING
# -------

# a = "trois"
# b = "sept"
# print('a =', a, ' b =', b)
#
# a = a + '-' +  b
# print('a :', a)   # a :  trois-sept
# print('a.split() :', a.split())   # a.split() : ['trois-sept']
#
# b = a.split('-')[0]
# a = a.split('-')[1]
# print('a =', a, ' b =', b)


# -------
# BOOLEAN
# -------

# a = bool(1)  # True
# b = bool(0)  # False
#
# # Afficher les valeurs avant la permutation
# print("Avant permutation:")
# print('a =', a, ' b =', b)
#
#
# # Permuter a et b
# print("Permutation...")
#
# print('-', a, b, '-', a ^ b)
# a = a ^ b  # a devient True si b est False, et vice versa
# # print('a :', a)
#
# print('-', a, b, '-', a ^ b)
# b = a ^ b  # b devient la valeur originale de a
# # print('b :', b)
#
# print('-', a, b, '-', a ^ b)
# a = a ^ b  # a devient la valeur originale de b
# # print(a)
#
# # Afficher les valeurs après la permutation
# print("Après permutation:")
# print('a =', a, ' b =', b)
