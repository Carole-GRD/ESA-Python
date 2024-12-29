def check_lastname_firstname():
    """
    Vérifie la validité du nom et du prénom fournis par l'utilisateur.

    Conditions de validité :
        1. Le nom et le prénom ne doivent pas être identiques.
        2. Ils doivent contenir uniquement des lettres, des espaces ou des traits d'union.

    Retour :
        → Une chaîne concaténée "Nom Prénom" si les entrées sont valides.
        → Un message d'erreur si l'une des conditions n'est pas respectée.
    """

    lastname = input("Nom : ").strip()
    firstname = input("Prenom : ").strip()

    # Vérifier que les champs ne sont pas vides
    if not lastname or not firstname:
        return "ERREUR : Le nom et le prénom ne peuvent pas être vides."

    # Vérifier que nom et prénom sont différents
    if lastname.lower() == firstname.lower():
        return "ERREUR : Le nom et le prénom ne peuvent pas être identiques."

    # Vérifier que chaque caractère est une lettre, un espace ou un trait d'union
    for character in lastname + firstname:
        if not (character.isalpha() or character in "- "):
            return f"ERREUR : Le caractère invalide '{character}' a été détecté dans le nom ou le prénom."

    # print(f"DEBUG (check_lastname_firstname): {lastname} {firstname}")
    return f"{lastname} {firstname}"
