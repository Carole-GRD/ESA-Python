"""
Module de validation du login saisi par l'utilisateur.

Ce module contient une fonction permettant de vérifier que le login n'est pas déjà pris
et qu'il est composé uniquement de lettres alphabétiques.
"""


def check_login(users_list):
    """
    Vérifie la validité d'un login utilisateur.

    Conditions de validité :
        1. Vérifie si le login existe déjà dans la liste des logins.
        2. Vérifie si tous les caractères du login sont des lettres (a-z, A-Z).

    Args :
        users_list : list
            Une liste des utilisateurs déjà enregistrés, chaque utilisateur étant une sous-liste.

    Returns :
        str
            Le login validé ou un message d'erreur.
    """
    # Saisie du login avec nettoyage des espaces et conversion en minuscules
    login = input('Login : ').strip().lower()

    # Vérifier si le login est déjà utilisé dans la liste des utilisateurs
    if any(user[3] == login for user in users_list):
        return f'ERREUR : Login "{login}" est déjà pris. Choisissez un autre login.'

    # # Vérifier que chaque caractère est une lettre
    # if not all(character.isalpha() for character in login):
    #     return f"ERREUR : Le login contient des caractères non valides."

    # Vérifier que chaque caractère est une lettre
    for character in login:
        if not character.isalpha():
            return f"ERREUR : Le caractère invalide '{character}' a été détecté dans le login."

    return login
