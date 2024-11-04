# Les types (slide 6)

# phrase = "Bonjour"
# phrase += " tout"
# phrase += " le"
# phrase += " monde"
# print(phrase)  # Résultat : "Bonjour tout le monde"

mots = ["Bonjour", "tout", "le", "monde"]
phrase = " ".join(mots)
# print(phrase)


message = "Bonjour"


# print(message[0:3])  # Bon (les indices 0 à 2)
# print(message[1:3])  # on (les indices 1 à 2)


def addition(a, b):
    """Cette fonction additionne deux nombres."""
    return a + b


# help(addition)
# print(addition.__doc__)


ma_variable1 = 5
ma_variable2 = "10.65 "
ma_variable3 = ma_variable1 * ma_variable2
# print(ma_variable3)


# a = 9
# b = 2
# c = a << b
# print('9 shl 2 : ', c)   # 36
# c = a >> b
# print('9 shr 2 : ', c)   # 2
"""
    # Pourquoi le résultat donne 36 et 2 ?

    ● Si on représente 9 sur un octet, nous aurons en binaire la valeur suivante : 00001001, soit 2^0+2^3 = 1+8 = 9

    ● si on fait un shift de 2 vers la gauche (shl), nous aurons ceci : 00100100, soit 2^2+2^5 = 4+32 = 36

    ● si on fait un shift de 2 vers la droite (shr), nous aurons ceci : 00000010, soit 2^1 = 2 
"""

# print(divmod(9, 2))  # (4, 1) => la paire a // b, a & b
# print(divmod(9, 2))  # (4, 1) => la paire a // b, a % b


# Faire un exposé dessus (une slide) ?
# Pour le x.5 -> quand on a un nombre impair, il arrondi au-dessus et quand c'est un nombre pair, il arrondi en dessous
# print("round(1.5)", round(1.5))
# print("round(2.5)", round(2.5))
# print("round(3.5)", round(3.5))
# print("round(4.5)", round(4.5))
