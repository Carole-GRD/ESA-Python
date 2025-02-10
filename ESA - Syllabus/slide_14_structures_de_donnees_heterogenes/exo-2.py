"""
    Exercice 2 :

    Écrivez une fonction qui échange les clés et les valeurs d’un dictionnaire (ce qui permettra par
    exemple de transformer un dictionnaire anglais/français en un dictionnaire français/anglais).
    On suppose que le dictionnaire ne contient pas plusieurs valeurs identiques.
"""


def inverser_dictionnaire(dico):
    """
    Échange les clés et les valeurs d'un dictionnaire.

    :param dico: (dict) Un dictionnaire dont les clés et les valeurs doivent être inversées.
    :return: (dict) Un nouveau dictionnaire avec les clés et valeurs échangées.
    """
    dico_inverse = {}

    for key, value in dico.items():
        dico_inverse[value] = key

    return dico_inverse


# dico_initial = {
#     '1': 'A',
#     '2': 'B',
#     '3': 'C'
# }
# print(f"dico initial : {dico_initial}")
# print(f"dico inverser : {inverser_dictionnaire(dico_initial)}")
