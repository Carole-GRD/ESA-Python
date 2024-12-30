"""
Module de validation de mot de passe saisi par l'utilisateur.

Ce module contient une fonction permettant de vérifier si un mot de passe satisfait certains critères de sécurité,
tels que la longueur minimale, la présence de lettres minuscules, majuscules, chiffres et caractères spéciaux.
"""


def check_password(min_length=10):
    """
    Vérifie si un mot de passe satisfait les critères de sécurité prédéfinis.

    Conditions de validité :
        * Longueur minimale : paramétrable (par défaut, 10 caractères)
        * Au moins 1 lettre minuscule
        * Au moins 1 lettre majuscule
        * Au moins 1 chiffre
        * Au moins 1 caractère spécial

    Args :
        min_length (int, optional) : Longueur minimale requise pour le mot de passe. Par défaut, 10.

    Returns :
        str :
            * Si le mot de passe est valide : retourne le mot de passe de manière cryptée (*).
            * Si le mot de passe est invalide : retourne un message d'erreur listant les critères manquants.
    """

    # Saisie du mot de passe avec nettoyage des espaces
    password = input("Mot de passe : ").strip()

    # Initialiser une liste pour collecter les erreurs de validation
    errors = []

    # Vérifier la longueur minimale
    if len(password) < min_length:
        errors.append(f"au moins {min_length} caractères")

    # Vérifier les types de caractères -> any() s'arrête dès qu'il trouve un caractère qui satisfait la condition
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special_character = any(not c.isalnum() for c in password)

    # Ajouter des messages d'erreur si les critères ne sont pas remplis
    if not has_lower:
        errors.append("1 minuscule")
    if not has_upper:
        errors.append("1 majuscule")
    if not has_digit:
        errors.append("1 chiffre")
    if not has_special_character:
        errors.append("1 caractère spécial")

    # # Afficher le résultat ou les erreurs
    # if not errors:
    #     return password
    # else:
    #     return f"ERREUR : Le mot de passe doit contenir {', '.join(errors)} !"

    # Afficher le résultat ou les erreurs
    if not errors:
        # Masquer le mot de passe pour le retour
        hidden_password = '*' * len(password)
        return hidden_password
    else:
        return f"ERREUR : Le mot de passe doit contenir {', '.join(errors)} !"
