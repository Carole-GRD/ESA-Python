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

