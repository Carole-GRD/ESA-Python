# def dessiner_losange():
#
#     nbr = int(input("Entre un nombre : "))
#
#     half_up = ''
#     spaces_up = nbr * ' '
#     for i in range(1, nbr + 1, 1):
#         spaces_up = spaces_up[:-1]
#         stars = i * 2 * '*'
#         half_up += spaces_up + stars + '\n'
#
#     half_down = ''
#     spaces_down = ''
#     for i in range(nbr - 1, 0, -1):
#         spaces_down += ' '
#         stars = i * 2 * '*'
#         half_down += spaces_down + stars + '\n'
#
#     return half_up + half_down
#
#
# losange = dessiner_losange()
# print(losange)

# =====================================================


def dessiner_losange(n):
    """
    Génère un losange sous forme de chaîne de caractères basé sur un nombre donné n.

    :param n: (int) la moitié de la longueur de la diagonale formée par les étoiles
                    (longueur maximale des lignes est 2 * n)
    :return: (str) une chaîne représentant le losange avec des '*' et des espaces
    """
    losange = []  # Liste pour stocker les lignes du losange

    # Partie supérieure du losange (y compris la ligne centrale)
    for i in range(n):
        spaces = ' ' * (n - i - 1)  # Calcul des espaces vides à gauche
        stars = '*' * (2 * (i + 1))  # Calcul du nombre d'étoiles
        losange.append(spaces + stars)  # Ajouter la ligne à la liste

    # Partie inférieure du losange
    for i in range(n - 1, 0, -1):
        spaces = ' ' * (n - i)  # Calcul des espaces vides à gauche
        stars = '*' * (2 * i)  # Calcul du nombre d'étoiles
        losange.append(spaces + stars)  # Ajouter la ligne à la liste

    return '\n'.join(losange)  # Joindre toutes les lignes avec des sauts de ligne


# Exemple d'utilisation
nombre = int(input("Entrez un nombre : "))
losange = dessiner_losange(nombre)
print(losange)
