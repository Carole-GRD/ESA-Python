# ==================================================================================================================

# Exercice 5 : qui compare deux entiers et affiche le plus grand (que doit-il afficher en cas… ?) [à l’aide de
# structure alternative uniquement]

# ==================================================================================================================



# ===========
# MA VERSION
# ===========


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





# ===================
# VERSION DE chatGPT
# ===================

# def compare_integer(n_1, n_2):
#     if n_1 > n_2:
#         result = f'{n_1} est plus grand (que {n_2})'
#     elif n_2 > n_1:
#         result = f'{n_2} est plus grand (que {n_1})'
#     else:
#         result = f'{n_1} et {n_2} sont égaux'
#     return result
#
# num_1, num_2 = int(input('Premier nombre : ')), int(input('Second nombre : '))
#
# biggest_number = compare_integer(num_1, num_2)
# print(biggest_number)
