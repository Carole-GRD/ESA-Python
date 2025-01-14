"""
    Exercice 1 :

    Soit une chaîne de caractères, écrire un algorithme récursif permettant de déterminer sa longueur.
"""


# ==================================================================================
# ===============================   MA VERSION  ====================================
# ==================================================================================

# def longueur(chaine):
#     """
#     Cette fonction permet de détermniner la longueur d'une chaîne de caractères.
#
#     :param chaine: La chaîne de caractères dont la longueur doit être calculée (str).
#     :return: La longueur de la chaîne de caractères (int).
#     """
#     n = 1
#     if chaine[:1] == '':
#         return 0
#     else:
#         return n + longueur(chaine[1:])


# ==================================================================================
# ===============================   AMELIORATION  ==================================
# ==================================================================================

def longueur(chaine):
    """
    Cette fonction détermine la longueur d'une chaîne en utilisant la récursion.

    Le cas de base est une chaîne vide, qui a une longueur de 0.
    Si la chaîne n'est pas vide, on retourne 1 (le premier caractère)
    ajouté à la longueur de la sous-chaîne restante.

    :param chaine: (str) La chaîne de caractères dont on veut calculer la longueur.

    :return: (int) La longueur de la chaîne de caractères.
    """
    if chaine == "":  # Cas de base : chaîne vide
        return 0
    else:
        return 1 + longueur(chaine[1:])  # Retire le premier caractère et continue


# ==================================================================================
# ===================================  TESTS  =====================================
# ==================================================================================

print(f"chaine vide : {longueur("")}")    # 0
print(f"a : {longueur("a")}")             # 1
print(f"ab : {longueur("ab")}")           # 2
print(f"abc : {longueur("abc")}")         # 3

phrase = "Soit une chaîne de caractères, écrire un algorithme récursif permettant de déterminer sa longueur."

print(f"Longueur de la phrase : {longueur(phrase)}")              # 98
print(f"type de longueur(phrase) : {type(longueur(phrase))}")     # <class 'int'>
print(f"Vérification => len(phrase) : {len(phrase)}")             # 98


# ==================================================================================
# =============================== EXPLICATIONS  ==================================
# ==================================================================================

"""
    Cas de base : 
        - Si la chaîne est vide (chaine == ""), la fonction retourne 0.
        - C'est essentiel pour que la récursion s'arrête.
    
    Cas récursif :
        - La fonction compte 1 pour le premier caractère.
        - Puis, elle appelle récursivement longueur sur la sous-chaîne obtenue 
          en retirant le premier caractère (chaine[1:]).
"""
