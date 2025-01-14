"""
    Exercice 4 :

    Écrire une fonction récursive permettant de vérifier si un mot est palindrome.
"""

# ================================================================================
# =============================  VERSION SIMPLE  =================================
# ======================  N'AFFICHE PAS LE MOT DE DEPART  ========================
# ================================================================================

# def est_palindrome(mot):
#     if len(mot) < 2:
#         return f"{mot} est un palindrome"
#     else:
#         if mot[0] == mot[-1]:
#             return palindrome(mot[1:-1])
#         else:
#             return f"{mot} n'est pas un palindrome"


# ================================================================================
# =============================  VERSION AMELIOREE  ==============================
# =======================   AFFICHE LE MOT DE  DEPART   ==========================
# ================================================================================

def est_palindrome(mot, mot_initial=None):
    """
    Vérifie si un mot est un palindrome en utilisant une approche récursive.

    Un palindrome est un mot qui se lit de la même manière dans les deux sens.
    La fonction compare les caractères aux extrémités du mot,
    en les retirant progressivement à chaque appel récursif.

    :param mot:
        (str) Le mot à tester pour savoir s'il est un palindrome.

    :param mot_initial:
        (str ou None) Le mot initial (utilisé pour conserver l'affichage complet dans le résultat).
                      Si None, il est initialisé avec la valeur de "mot".
    :return:
        (str) Un message indiquant si le mot est un palindrome ou non.
    """

    # Si c'est la première itération, on garde le mot initial
    if mot_initial is None:
        # if not mot:   # Cas spécifique : la chaîne d'origine est vide
        #     return f'Une chaîne vide n\'est pas un palindrome.'
        mot_initial = mot

    # Cas de base : un mot de longueur 0 ou 1 est toujours un palindrome
    if len(mot) < 2:
        return f'"{mot_initial}" est un palindrome'

    # Vérifier les extrémités
    if mot[0].lower() == mot[-1].lower():
        # Appel récursif sur le mot sans les premiers et derniers caractères,
        # en passant le mot initial pour conserver son affichage dans le résultat final.
        return est_palindrome(mot[1:-1], mot_initial)
    else:
        return f'"{mot_initial}" n\'est pas un palindrome'


# ================================================================================
# ===================================  TESTS  ====================================
# ================================================================================

print(est_palindrome(''))          # "" est un palindrome
# OU BIEN :                        # Une chaîne vide n'est pas un palindrome.
# → si on décommente le cas spécifique (lignes 47 et 48)

print(est_palindrome(' '))         # " " est un palindrome
print(est_palindrome('a'))         # a est un palindrome
print(est_palindrome('abba'))      # kayak est un palindrome
print(est_palindrome('abcd'))      # "abcd" n'est pas un palindrome
print(est_palindrome('kayak'))     # kayak est un palindrome
print(est_palindrome('Kayak'))     # Kayak est un palindrome
# print(est_palindrome('koyak'))     # koyak n'est pas un palindrome
# print(est_palindrome('elle'))      # elle est un palindrome
# print(est_palindrome('elie'))      # elie n'est pas un palindrome
# print(est_palindrome('pantalon'))  # pantalon n'est pas un palindrome
# print(est_palindrome('test'))      # test n'est pas un palindrome
# print(est_palindrome('radar'))     # radar est un palindrome
# print(est_palindrome('python'))    # python n'est pas un palindrome
