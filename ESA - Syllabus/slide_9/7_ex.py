"""
    Exercice 7 :

    Écrire un programme qui renvoie vrai si la phrase encodée par l'utilisateur est un palindrome.

    Aide :
        ● Une phrase est un palindrome si elle se lit de manière identique de droite à gauche et de gauche à droite.
        ● Exemple, le mot "KAYAK"
        ● Donc si la phrase est égale à la phrase inversée...
"""


# ==================================================================================================
# =======================================   MON CODE ===============================================
# ==================================================================================================


# def is_palindrome(word):
#     lower_word = word.lower()
#     reversed_word = lower_word[::-1]
#     if lower_word == reversed_word:
#         return True
#     else:
#         return False
#
#
# print(is_palindrome("kayak"))   # True
# print(is_palindrome("Kayak"))   # True
# print(is_palindrome("maison"))   # False


# ==================================================================================================
# =======================================   PLUS CONCIS ============================================
# ==================================================================================================


# def is_palindrome(word):
#     lower_word = word.lower()
#     return lower_word == lower_word[::-1]  # Retourne directement le résultat de la comparaison


# ==================================================================================================
# ====================================   Gérer les espaces  ========================================
# ==================================================================================================


# def is_palindrome(word):
#     lower_word = word.lower().replace(" ", "")
#     return lower_word == lower_word[::-1]


# ==================================================================================================
# ============================   Gérer les accents et les espaces  =================================
# ==================================================================================================


from utils import remove_accents


def is_palindrome(word):
    # Nettoyer la chaîne : retirer les accents, espaces, caractères non alphanumériques et mise en minuscule
    cleaned_word = ''.join(
        char.lower() for char in remove_accents(word) if char.isalnum()
    )

    # Vérifier si c'est un palindrome
    return cleaned_word == cleaned_word[::-1]


# ==================================================================================================
# ====================================   Test de la fonction  =====================================
# ==================================================================================================


phrase = input("Entrez une phrase : ")
if is_palindrome(phrase):
    print("La phrase est un palindrome.")
else:
    print("La phrase n'est pas un palindrome.")


# EXEMPLES DE PALINDROMES
# kayak
# Kayak
# Ésope reste ici et se repose.
# A man, a plan, a canal, Panama!
# radar
# laval
# Mon nom.
# Non à ce canon.
# Le bon Nobel.
# Né de l'Eden.
# Tu l'as trop écrasé, César, ce Port-Salut !


# ==================================================================================================
# ============================   Gérer les accents avec unicodedata  ===============================
# ==================================================================================================


# import unicodedata
#
#
# def is_palindrome(word):
#     # 1. Retirer les accents et normaliser les lettres
#     def remove_accents(text):
#         return ''.join(
#             char for char in unicodedata.normalize('NFD', text)
#             if unicodedata.category(char) != 'Mn'
#         )
#
#     # 2. Nettoyer la chaîne : suppression des espaces, accents et mise en minuscule
#     cleaned_word = ''.join(
#         char.lower() for char in remove_accents(word) if char.isalnum()
#     )
#
#     # 3. Vérifier si la phrase est un palindrome
#     return cleaned_word == cleaned_word[::-1]
