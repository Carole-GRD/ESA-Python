
# ---------------------------------
# Les chaînes de caractère (String)
# ---------------------------------

# # Comparaison de chaînes
# # ----------------------
# s1 = 'ac'
# s2 = 'abcdefg'
# print(len(s1))            # 2
# print(len(s2))            # 7
# print(len(s1) > len(s2))  # False
# print(len(s1) < len(s2))  # True


# # Accès à un ou plusieurs éléments x d’une chaîne
# # -----------------------------------------------
# ch1 = 'Hello'
# print(ch1[0])      # H
# print(ch1[:3])     # Hel
# print(ch1[-3:])    # ll0
# print(ch1[1:-1])   # ell


# -------------------------------------
# # Parcours d’une chaîne de caractères
# -------------------------------------

# s = "Hello world"
# i = 0  # l'indice pour parcourir les caractères de la chaîne
# while i < len(s):
#     print(s[i])
#     i += 1
#
# s = "Hello world"
# for i in range(0, len(s)):
#     print(s[i])
#     i += 1      # utilisté ???
#
# s = "Hello world"
# for c in s:
#     print(c)


# ---------------------------
# # Remplacement de caractère
# ---------------------------

# s = "Hello werld"    # par exemple : si on veut remplacer le e de werld par o
# print(s)
#
# # -----------------------------
# # Supprimer
# # s = s[:7] + s[8:]   # de 0 à 7 exclu (Hello w) et de 8 à la fin (rld) => on a supprimer le "e"
# # print(s)  # Hello wrld
#
# # Ajouter le caractère "o" après avoir supprimer le 7e caractère ("e")
# # s = s[: 7] + 'o' + s[7:]   # Hello w + o + rld
# # print(s)  # Hello world
# # -----------------------------
#
# # OU BIEN : Remplacer directement en une ligne
# s = s[: 7] + 'o' + s[8:]   # Hello w + o + rld   # le caractère 7 est exclu et on place directement le caractère "o"
# print(s)  # Hello world


# --------------------------------------------------------
# #  Listes des routines de gestion de chaînes (important)
# --------------------------------------------------------

# s = "Hello world"
#
# # En tapant help(nom_méthode), vous obtiendrez de l’aide sur la méthode "nom_méthode".
# # Par exemple, si on tape ceci :
# help(s.startswith)
# """
# startswith(...) method of builtins.str instance
#     S.startswith(prefix[, start[, end]]) -> bool
#
#     Return True if S starts with the specified prefix, False otherwise.
#     With optional start, test S beginning at that position.
#     With optional end, stop comparing S at that position.
#     prefix can also be a tuple of strings to try.
# """
#
# print(s.startswith("H"))   # True
# print(s.startswith("h"))   # False
