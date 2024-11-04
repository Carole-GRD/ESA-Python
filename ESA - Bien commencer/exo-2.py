
"""
        Silde 5 - Diapo 45

        Programme qui permet d’échanger le contenu de deux variables
"""


# ========================
#       Solution
# ========================

a, b = input("Entrez deux nombres entiers séparés par un espace : ").split(" ")
print("Avant traitement, A=", a, "B = ", b)
a, b = b, a
print("Après traitement, A=", a, "B = ", b)





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



# -------
# STRING
# -------

# trois = "trois"
# sept = "sept"
# trois = trois + '-' +  sept
# sept = trois.split('-')[0]
# trois = trois.split('-')[1]
# print('trois = ', trois)
# print('sept = ', sept)



# -------
# BOOLEAN
# -------

# a = bool(1)  # True
# b = bool(0)  # False
#
# # Afficher les valeurs avant la permutation
# print("Avant permutation:")
# print("a =", a)  # True
# print("b =", b)  # False
#
# # Permuter a et b
# a = a ^ b  # a devient True si b est False, et vice versa
# b = a ^ b  # b devient la valeur originale de a
# a = a ^ b  # a devient la valeur originale de b
#
# # Afficher les valeurs après la permutation
# print("Après permutation:")
# print("a =", a)  # False
# print("b =", b)  # True
