class IbanError(Exception):
    """Exception levée pour une erreur dans le format de l'IBAN."""
    pass


def valider_iban(iban):
    # Suppression des espaces dans l'IBAN s'il y en a
    iban = iban.replace(" ", "")

    # Vérification de la longueur
    if len(iban) < 15 or len(iban) > 34:
        raise IbanError(
            f"""Erreur : L'IBAN '{iban}' a une longueur incorrecte. 
            Il doit contenir entre 15 et 34 caractères."""
        )

    # Vérification que le code pays est bien composé de deux lettres
    if not iban[:2].isalpha():
        raise IbanError(
            f"""Erreur : Le code IBAN '{iban}' est mal formaté. 
            Les deux premiers caractères doivent être des lettres (code pays)."""
        )

    # Vérification de la clé de contrôle (deux chiffres)
    if not iban[2:4].isdigit():
        raise IbanError(
            f"""Erreur : Le code IBAN '{iban}' est mal formaté. 
            Les caractères 3 et 4 doivent être des chiffres (clé de contrôle)."""
        )

    # Vérification que le reste du code IBAN contient
    # uniquement des chiffres et des lettres
    if not iban[4:].isalnum():
        raise IbanError(
            f"""Erreur : Le code IBAN '{iban}' contient des caractères invalides. 
            Seules les lettres majuscules et les chiffres sont autorisés."""
        )

    # Si toutes les vérifications passent, l'IBAN est valide
    return True


# Utilisation avec try-except dans une autre fonction

def traiter_iban(iban):
    try:
        if valider_iban(iban):
            print(f"L'IBAN '{iban}' est valide et peut être utilisé.")
    except IbanError as e:
        print(f"Validation échouée : {e}")


# Tests avec des IBAN corrects et incorrects
print("\nTest 1 : IBAN valide")
traiter_iban("FR76 1234 5678 9012 3456 7890 123")

print("\nTest 2 : IBAN trop court")
traiter_iban("FR76 123")

print("\nTest 3 : IBAN mal formaté (caractères non valides)")
traiter_iban("FR76123A567@901234567890")

print("\nTest 4 : IBAN mal formaté (manque lettres en début)")
traiter_iban("7612345678901234567890123")
