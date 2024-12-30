"""
Module de validation d'un code postal saisi par l'utilisateur.

Ce module contient une fonction permettant de vérifier la validité d'un code postal est une chaîne de 4 chiffres.
"""


def check_cp():
    """
    Vérifie la validité du code postal saisi par l'utilisateur.

    Conditions de validité :
        Le code postal doit être une chaîne composée exactement de 4 chiffres.

    Retour :
        → Le code postal (str) si valide.
        → Un message d'erreur si la validation échoue.
    """

    # Saisie du code postal avec nettoyage des espaces
    cp = input("Code postal : ").strip()

    # Vérifier que le code postal contient exactement 4 chiffres
    if len(cp) == 4 and cp.isdigit():
        # print(f"DEBUG (check_cp): {cp}")
        return cp

    return "ERREUR : Le code postal doit être composé de 4 chiffres uniquement."


# print(check_cp())
