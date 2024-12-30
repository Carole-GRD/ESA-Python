"""
Module de validation du login saisi par l'utilisateur.

Ce module contient une fonction permettant de vérifier que le login n'est pas déjà pris
et qu'il est composé uniquement de lettres alphabétiques.
"""


def check_login(login_list):
    """
    Vérifie la validité d'un login utilisateur.

    Conditions de validité :
        1. Vérifie si le login existe déjà dans la liste des logins.
        2. Vérifie si tous les caractères du login sont des lettres (a-z, A-Z).

    Args :
        login_list : list
            Une liste des logins déjà existants.

    Returns :
        str
            Le login validé ou un message d'erreur.
    """

    # Saisie du login avec nettoyage des espaces et uniquement des minuscules
    login_input = input('Login : ').strip().lower()

    # # Vérifier si le login est déjà présent dans la liste pour éviter la redondance
    # if any(login_input == login for login in login_list):
    #     return f'ERREUR : Login "{login_input}" est déjà pris. Choisissez un autre login.'

    # Vérifier si le login est déjà présent dans la liste pour éviter la redondance
    if login_input in set(login_list):
        return f'ERREUR : Login "{login_input}" est déjà pris. Choisissez un autre login.'

    # Vérifier que chaque caractère est une lettre
    for character in login_input:
        if not character.isalpha():
            return f"ERREUR : Le caractère invalide '{character}' a été détecté dans le login."

    return login_input
