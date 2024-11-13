import math
# from math import *


# ==================================================================================================================

# Exercice 1 : qui lit la valeur du rayon d’un cercle et affiche la valeur de la circonférence (hypothèse : le
# nombre introduit est positif)

# ==================================================================================================================

# PI = math.pi
#
# while True:
#     try:
#         # Demander à l'utilisateur de saisir un nombre
#         rayon = float(input("rayon : "))
#
#         # Vérifier si le nombre est positif
#         if rayon > 0:
#             # Calculer la circonference du cercle puis l'afficher et sortir de la boucle
#             perimetre = 2 * PI * rayon
#             aire = PI * pow(rayon, 2)
#
#             print(f"La circonférence d'un cercle de rayon {rayon} est {round(perimetre, 2)}")
#             print(f"La superficie d'un cercle de rayon {rayon} est {round(aire, 2)}")
#
#             break
#         else:
#             print("Le rayon doit être un nombre positif. Veuillez réessayer.")
#
#     # Gérer les erreurs si l'utilisateur entre autre chose qu'un nombre
#     except ValueError:
#         print("Erreur : Vous devez entrer un nombre valide.")




# ==================================================================================================================

# Exercice 2 : qui calcul la TVA et le prix net à partir du prix hors taxe et du taux à appliquer (en %)

# ==================================================================================================================

# taux = int(input("Taux en % : "))
#
# prix_ht = float(input("Prix en € : "))
#
# tva = prix_ht * taux / 100
#
# prix_ttc = prix_ht + tva
#
#
# print(f"Montant de la TVA {tva:.2f}€ - Prix net {prix_ttc:.2f}€")



# ==================================================================================================================

# Exercice 3 : qui permet d’échanger le contenu de deux variables

# ==================================================================================================================


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

# STRING
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


# ==================================================================================================================

# Exercice 4 : qui retourne la valeur absolue d’un entier [à l’aide de structure alternative uniquement]

# ==================================================================================================================

# def get_absolute_value(number):
#     if number < 0:
#         number = -number
#     return number
#
# input_number = int(input("Nombre : "))
# absolute_value = get_absolute_value(input_number)
#
# print(f'La valeur absolue de {input_number} est {absolute_value}')



# ==================================================================================================================

# Exercice 5 : qui compare deux entiers et affiche le plus grand (que doit-il afficher en cas… ?) [à l’aide de
# structure alternative uniquement]

# ==================================================================================================================

# def compare_integer(n_1, n_2):
#     biggest = f'Le plus grand nombre est : {n_1}'
#     if n_2 > n_1:
#         biggest = f'Le plus grand nombre est : {n_2}'
#     if n_2 == n_1:
#         biggest = "Les deux nombres sont égaux !"
#     return biggest
#
# num_1, num_2 = int(input('Premier nombre : ')), int(input('Second nombre : '))
#
# biggest_number = compare_integer(num_1, num_2)
# print(biggest_number)





# ==================================================================================================================

# Exercice 6 : qui ayant lu trois nombres entiers (nous supposons les valeurs distinctes), affiche la plus grande
# et la plus petite valeur [à l’aide de structure alternative uniquement]

# ==================================================================================================================

# ===========
# MA VERSION
# ===========

# def compare_integer(n_1, n_2, n_3):
#     if n_1 < n_2 and n_1 < n_3:
#         if n_2 < n_3:
#             smallest = f'Le plus petit nombre est : {n_1}'
#             biggest = f'Le plus grand nombre est : {n_3}'
#         else:
#             smallest = f'Le plus petit nombre est : {n_1}'
#             biggest = f'Le plus grand nombre est : {n_2}'
#     elif  n_2 < n_1 and n_2 < n_3:
#         if n_1 < n_3:
#             smallest = f'Le plus petit nombre est : {n_2}'
#             biggest = f'Le plus grand nombre est : {n_3}'
#         else:
#             smallest = f'Le plus petit nombre est : {n_2}'
#             biggest = f'Le plus grand nombre est : {n_1}'
#     else:
#         if n_1 < n_2:
#             smallest = f'Le plus petit nombre est : {n_3}'
#             biggest = f'Le plus grand nombre est : {n_2}'
#         else:
#             smallest = f'Le plus petit nombre est : {n_3}'
#             biggest = f'Le plus grand nombre est : {n_1}'
#     return smallest, biggest
#
# num_1, num_2, num_3 = int(input('Premier nombre : ')), int(input('Second nombre : ')), int(input('Troisième nombre : '))
#
# biggest_and_smallest = compare_integer(num_1, num_2, num_3)
# print(biggest_and_smallest)





# ===================
# VERSION DE chatGPT
# ===================

# # Exemple de trois nombres distincts
# # a = 15
# # b = 32
# # c = 27
# a, b, c = int(input('Premier nombre : ')), int(input('Second nombre : ')), int(input('Troisième nombre : '))
#
# # Trouver la plus grande valeur
# if a > b and a > c:
#     max_val = a
# elif b > a and b > c:
#     max_val = b
# else:
#     max_val = c
#
# # Trouver la plus petite valeur
# if a < b and a < c:
#     min_val = a
# elif b < a and b < c:
#     min_val = b
# else:
#     min_val = c
#
# print("La plus grande valeur est :", max_val)
# print("La plus petite valeur est :", min_val)



# =====================
# VERSION DE GEMINI AI
# =====================

# # Demande à l'utilisateur d'entrer les trois nombres
# a = int(input("Entrez le premier nombre : "))
# b = int(input("Entrez le deuxième nombre : "))
# c = int(input("Entrez le troisième nombre : "))
#
# # Initialisation des variables pour stocker le plus grand et le plus petit
# plus_grand = a
# plus_petit = a
#
# # Utilisation de structures alternatives pour déterminer le plus grand et le plus petit
# if b > plus_grand:
#     plus_grand = b
# if c > plus_grand:
#     plus_grand = c
#
# if b < plus_petit:
#     plus_petit = b
# if c < plus_petit:
#     plus_petit = c
#
# # Affichage des résultats
# print("Le plus grand nombre est :", plus_grand)
# print("Le plus petit nombre est :", plus_petit)








# ==================================================================================================================

# Exercice 7 : qui lit 2 entiers et affiche les nombres compris dans cet intervalle (on inclut les valeurs lues) [à
# l’aide de structures alternatives et répétitives uniquement]

# ==================================================================================================================

# n_1 = int(input('Premier nombre : '))
# n_2 = int(input('Deuxième nombre : '))
#
# def list_the_numbers_in_the_interval(n1, n2):
#     i = n1
#     if i < n2:
#         while i <= n2:
#             print(i)
#             i = i + 1
#     else:
#         while i >= n2:
#             print(i)
#             i = i - 1
#
# list_the_numbers_in_the_interval(n_1, n_2)




# ==================================================================================================================

# Exercice 8 : qui calcul le pgcd de 2 entiers strictement positifs [à l’aide de structures alternatives et
# répétitives uniquement]

# ==================================================================================================================


# n_1 = int(input('Premier nombre : '))
# n_2 = int(input('Deuxième nombre : '))
#
# def find_pgcd(n1, n2):
#
#     # Détermine le plus petit et le plus grand nombre
#     if n1 < n2:
#         max_value = n2
#         min_value = n1
#     else:
#         max_value = n1
#         min_value = n2
#
#     pgcd = euclide(max_value,min_value)
#
#     print(f'Le PGCD de {n1} et {n2} est {pgcd}')
#
#
# def euclide(max_value, min_value):
#     while min_value != 0:
#         r = max_value % min_value
#         max_value = min_value
#         min_value = r
#     return max_value
#
#
# find_pgcd(n_1, n_2)




# ==================================================================================================================

# Exercice 9 : qui calcul la somme des n premiers entiers positifs (n étant lu)

# ==================================================================================================================


# def sum_first_integers(n):
#     sum = 0
#     next = 0
#     while next <= n:
#         sum = sum + next
#         # print(sum)
#         next = next + 1
#     return sum
#
#
# n = int(input('Nombre : '))
# sum = sum_first_integers(n)
#
# print(f'La somme des n premiers entiers de {n} est {sum}.')



# ==================================================================================================================
