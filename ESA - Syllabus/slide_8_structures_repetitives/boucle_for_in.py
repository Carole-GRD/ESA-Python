
# jours = ("Lundi", "mardi", "mercredi")
# for i, jour in enumerate(jours):
#     if i == 0:
#         print(jour)
#
# SEQUENCE = 'ma séquence'
# for CARACTERE in SEQUENCE:
#     print(CARACTERE)

# ma_sequence = (1, 3.14, -4, 'toto')
# print(ma_sequence)
# for el in ma_sequence:
#     print(el)
#     print(ma_sequence)


# # ATTENTION: un entier, une float n'est pas une séquence (on ne sait donc pas boucler dedans !)
# ma_sequence = (1, 3.14, -4, 'toto')
# for el in ma_sequence[0]:     # TypeError: 'int' object is not iterable
#     print(el)

# # OR: une chaine de caractère est une séquence
# ma_sequence = (1, 3.14, -4, 'toto')
# for el in ma_sequence[3][0]:
#     print(el)


# # SLICING (découpe une séquence en sous-séquences)
# ma_sequence = (1, 3.14, -4, 'toto', "Albert", 25, 0)
# for el in ma_sequence[2, 3]:         # TypeError: tuple indices must be integers or slices, not tuple
#     print(el)


# ma_sequence = (1, 3.14, -4, 'toto', "Albert", 25, 0)
# for el in ma_sequence[2:4]:
#     print(el)
# print(ma_sequence[2:3])


# pourquoi de 2 à 4 "exclu" ? faire des recherches


# ma_sequence = (1, 3.14, -4, 'toto', "Albert", 25, 0)
# for i in range(3):    # 0 1 2
#     i += 1            # 1 2 3
#     print(ma_sequence[i])

# ma_sequence = (1, 3.14, -4, 'toto', "Albert", 25, 0)
# for i in range(3):    # 0 1 2
#     i *= 2            # 0 2 4
#     print(ma_sequence[i])

# ma_sequence = (1, 3.14, -4, 'toto', "Albert", 25, 0)
# for i in (0, 1, 0, 1):    # 0 1 0 1
#     i *= 2                # 0 2 0 2
#     print(ma_sequence[i])


# cote_sur_dix = (10, 4, 9, 7)
# for cote in cote_sur_dix:
#     print("Ma cote sur 20 = ", cote * 2)


# cote_sur_dix = (10, 4, 9, 7)
# for cote in cote_sur_dix[0:2]:
#     print(cote)
# print(cote)
