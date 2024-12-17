"""
    Exercice 6 :
    Écrire un programme qui compare 2 chaînes de caractères au regard de l'ordre lexicographique
    (l'ordre du dictionnaire pour les caractères non accentués).
    Vous ne pouvez pas utiliser de méthode toute faite !
    Aide :
        ● Considérez une chaîne de caractère comme étant une suite de caractère.
            - E X E M P L E
            - E X E M P L E S
        ● Dès qu'un des caractères est plus grand que l'autre, vous avez trouvé le mot devant être plus petit.
"""

# ==================================================================================================
# ========================================   MON CODE  =============================================
# ==================================================================================================

# word_1 = "exemple"
# word_2 = "exemples"
#
# is_same_length = True if len(word_1) == len(word_2) else False
# min_length = 0
# longest = ''
#
# if is_same_length:
#     min_length = len(word_1)
# elif len(word_1) < len(word_2):
#     min_length = len(word_1)
#     longest = word_2
# elif len(word_1) > len(word_2):
#     min_length = len(word_2)
#     longest = word_1
#
# # Parcourir chaque caractère jusqu'à la longueur de la plus courte chaîne
# for i in range(min_length):
#     if word_1[i] == word_2[i]:
#         continue
#     elif word_1[i] > word_2[i]:
#         exit(f"Le premier mot dans l'ordre lexicographique est : {word_2}")
#     elif word_1[i] < word_2[i]:
#         exit(f"Le premier mot dans l'ordre lexicographique est : {word_1}")
#
# # Si tous les caractères communs sont identiques, comparer les longueurs
# if is_same_length:
#     print("Les mots sont identiques !")
# elif longest == word_1:
#     print((f"Le premier mot dans l'ordre lexicographique est : {word_2}"))
# elif longest == word_2:
#     print((f"Le premier mot dans l'ordre lexicographique est : {word_1}"))

# ==================================================================================================
# ==============================   MON CODE AMELIORE PAR CHATGPT ===================================
# ==================================================================================================


# def comparer_chaines(chaine1, chaine2):
#     """
#     Compare deux chaînes de caractères selon l'ordre lexicographique.
#     : pre : chaine1 et chaine2 doivent être des chaînes de caractères valides (type str).
#     : post : La fonction retourne un message indiquant laquelle des deux chaînes est la première dans
#           l'ordre lexicographique, ou si elles sont égales.
#     """
#     # Trouver la longueur minimale
#     if len(chaine1) < len(chaine2):
#         min_length = len(chaine1)
#     elif len(chaine1) > len(chaine2):
#         min_length = len(chaine2)
#     else:
#         min_length = len(chaine1)  # Les deux chaînes sont de la même longueur
#     # Comparer les caractères un par un
#     for i in range(min_length):
#         if chaine1[i] < chaine2[i]:
#             return f"'{chaine1}' vient avant '{chaine2}'"
#         elif chaine1[i] > chaine2[i]:
#             return f"'{chaine2}' vient avant '{chaine1}'"
#     # Si tous les caractères sont identiques jusqu'à la fin de la plus courte chaîne
#     if len(chaine1) < len(chaine2):
#         return f"'{chaine1}' vient avant '{chaine2}'"
#     elif len(chaine1) > len(chaine2):
#         return f"'{chaine2}' vient avant '{chaine1}'"
#     else:
#         return f"'{chaine1}' et '{chaine2}' sont égales"
#
#
# # Test avec des exemples
# print(comparer_chaines("exemple", "exemples"))  # "exemple" vient avant "exemples"
# print(comparer_chaines("chat", "chien"))  # "chat" vient avant "chien"
# print(comparer_chaines("python", "python"))  # "python" et "python" sont égales

# ==================================================================================================
# =================================   CODE AVEC METHODE MIN() ======================================
# ==================================================================================================


# def comparer_chaines(chaine1, chaine2):
#     # Parcourir chaque caractère jusqu'à la longueur de la plus courte chaîne
#     for i in range(min(len(chaine1), len(chaine2))):
#         if chaine1[i] < chaine2[i]:  # Comparaison des caractères
#             return f"'{chaine1}' vient avant '{chaine2}'"
#         elif chaine1[i] > chaine2[i]:
#             return f"'{chaine2}' vient avant '{chaine1}'"
#
#     # Si tous les caractères communs sont identiques, comparer les longueurs
#     if len(chaine1) < len(chaine2):
#         return f"'{chaine1}' vient avant '{chaine2}'"
#     elif len(chaine1) > len(chaine2):
#         return f"'{chaine2}' vient avant '{chaine1}'"
#     else:
#         return f"'{chaine1}' et '{chaine2}' sont égales'
#
#
# # Exemple d'utilisation
# chaine1 = "EXEMPLE"
# chaine2 = "EXEMPLES"
# print(comparer_chaines(chaine1, chaine2))

# ==================================================================================================
# =================================   CODE AVEC METHODE ZIP() ======================================
# ==================================================================================================


# def comparer_chaines(chaine1, chaine2):
#     # Parcourir les deux chaînes caractère par caractère
#     for c1, c2 in zip(chaine1, chaine2):
#         if c1 < c2:  # Si le caractère de chaine1 est plus petit
#             return f"'{chaine1}' vient avant '{chaine2}'"
#         elif c1 > c2:  # Si le caractère de chaine2 est plus petit
#             return f"'{chaine2}' vient avant '{chaine1}'"
#
#     # Si toutes les lettres jusqu'à présent sont identiques,
#     # on compare les longueurs des chaînes
#     if len(chaine1) < len(chaine2):
#         return f"'{chaine1}' vient avant '{chaine2}'"
#     elif len(chaine1) > len(chaine2):
#         return f"'{chaine2}' vient avant '{chaine1}'"
#     else:
#         return f"'{chaine1}' et '{chaine2}' sont égales"
#
# # Test du programme
# chaine1 = "EXEMPLE"
# chaine2 = "EXEMPLES"
#
# print(comparer_chaines(chaine1, chaine2))


# ==================================================================================================
# =================================   PLUS SIMPLE ======================================
# ==================================================================================================


def comparer_chaines(chaine1, chaine2):
    """
    Compare deux chaînes de caractères selon l'ordre lexicographique.
    : pre : chaine1 et chaine2 doivent être des chaînes de caractères valides (type str).
    : post : La fonction retourne un message indiquant laquelle des deux chaînes est la première dans
          l'ordre lexicographique, ou si elles sont égales.
    """
    if chaine1 < chaine2:
        return f"'{chaine1}' vient avant '{chaine2}'"
    elif chaine1 > chaine2:
        return f"'{chaine2}' vient avant '{chaine1}'"
    else:
        return f"'{chaine1}' et '{chaine2}' sont égales"


# Test avec des exemples
print(comparer_chaines("exemple", "exemples"))  # "exemple" vient avant "exemples"
print(comparer_chaines("exemples", "exemple"))  # "exemple" vient avant "exemples"
print(comparer_chaines("chat", "chien"))  # "chat" vient avant "chien"
print(comparer_chaines("python", "python"))  # "python" et "python" sont égales
