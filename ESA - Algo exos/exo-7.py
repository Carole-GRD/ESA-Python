# ==================================================================================================================

# Exercice 7 : qui lit 2 entiers et affiche les nombres compris dans cet intervalle (on inclut les valeurs lues) [à
# l’aide de structures alternatives et répétitives uniquement]

# ==================================================================================================================


# ===========
# MA VERSION
# ===========


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




# =====================
# VERSION DE GEMINI AI
# =====================


# # Demande à l'utilisateur d'entrer les deux nombres
# n_1 = int(input("Entrez le premier nombre : "))
# n_2 = int(input("Entrez le deuxième nombre : "))
#
# # Détermine le plus petit et le plus grand nombre
# if n_1 < n_2:
#     pas = 1  # On incrémente pour un ordre croissant
# else:
#     pas = -1  # On décrémente pour un ordre décroissant
#
# # Affiche tous les nombres de l'intervalle
# print("Les nombres compris entre", n_1, "et", n_2, "sont :")
# nombre = n_1
# while nombre != n_2 + pas:
#     print(nombre)
#     nombre += pas




# ===================
# VERSION DE chatGPT
# ===================

# # Demande à l'utilisateur d'entrer les deux nombres
# n_1 = int(input("Entrez le premier nombre : "))
# n_2 = int(input("Entrez le deuxième nombre : "))
#
# # Afficher les nombres dans l'intervalle de a à b, peu importe leur ordre
# if n_1 > n_2:
#     for i in range(n_1, n_2 - 1, -1):  # Compte à rebours de 'a' à 'b'
#         print(i)
# else:
#     for i in range(n_1, n_2 + 1):  # Compte normal de 'a' à 'b'
#         print(i)





# =====================================
# VERSION DE chatGPT    (avec tableau)
# =====================================

# Demande à l'utilisateur d'entrer les deux nombres
n_1 = int(input("Entrez le premier nombre : "))
n_2 = int(input("Entrez le deuxième nombre : "))

# Afficher les nombres dans l'intervalle de a à b, peu importe leur ordre
numbers_in_range = []

def list_the_numbers_in_the_interval(n1, n2):
    if n_1 > n_2:
        for i in range(n_1, n_2 - 1, -1):  # Compte à rebours de 'a' à 'b'
            numbers_in_range.append(i)
    else:
        for i in range(n_1, n_2 + 1):  # Compte normal de 'a' à 'b'
            numbers_in_range.append(i)

list_the_numbers_in_the_interval(n_1, n_2)
print(numbers_in_range)