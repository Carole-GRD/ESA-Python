def check_email():
    """
    Vérifie si l'adresse email saisie est valide.

    Conditions de validité :
        1. L'email doit contenir exactement un '@'.
        2. La partie locale (avant le '@') doit contenir uniquement des lettres, chiffres, points ('.')
            ou traits d'union ('-').
        3. La partie domaine (après le '@') doit inclure un point ('.') séparant le nom de domaine et l'extension.
        4. Le nom de domaine doit être alphanumérique, et l'extension uniquement composée de lettres.

    Retour :
        → L'email si valide.
        → Un message d'erreur expliquant la règle non respectée en cas d'échec.
    """

    email = input("Email : ").strip()

    # Découper l'email autour du @
    if email.count("@") != 1:
        return "ERREUR : L'email doit contenir exactement un '@'."

    local_part, domain_part = email.split("@")

    # Vérifier la partie locale (avant le @)
    for caractere in local_part:
        if not (caractere.isalnum() or caractere in ".-"):
            return "ERREUR : La partie locale (avant '@') contient un caractère non autorisé."

    # Vérifier la partie domaine (après le @)
    if "." not in domain_part:
        return "ERREUR : Le domaine (après '@') doit contenir au moins un point (ex. domain.com)."

    domain_name, domain_extension = domain_part.rsplit(".", 1)

    if not (domain_name.isalnum() and domain_extension.isalpha()):
        return "ERREUR : Le domaine ou l'extension est invalide."

    # print(f"DEBUG (check_email): {email}")
    return email
