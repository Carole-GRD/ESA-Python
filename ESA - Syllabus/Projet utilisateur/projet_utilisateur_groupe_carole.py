# PROPOSITION

def check_nom_prenom(nom, prenom):
    """
    Valide que le nom et le prénom sont différents et contiennent uniquement des lettres,
    des espaces ou des traits d'union.

    Args :
        → nom (str) : Le nom à vérifier.
        → prenom (str) : Le prénom à vérifier.

    Returns :
        → tuple : (bool, str) Indique si la validation est réussie et fournit un message.
    """

    if nom == prenom:
        return False, "Veuillez entrer un nom et prénom différents"

    for cara in (nom, prenom):
        if "@" in cara or "." in cara:
            return False, "Les seuls caractères spéciaux acceptés sont le 'trait d'union'"

    if not all(c.isalpha() or c == '-' for c in nom) or not all(c.isalpha() or c == '-' for c in prenom):
        return False, "Seuls les lettres A-Z, a-z et le trait d'union sont acceptés"

    return True, "Nom et prenom valides"


# ===========================================================================================================
def check_cp(cp):
    """
    Vérifie que le code postal contient exactement 4 chiffres.

    Args :
        → cp (str) : Le code postal à valider.

    Returns :
        → tuple : (bool, str) Indique si la validation est réussie et fournit un message.
    """

    # Vérifier que le code postal contient exactement 4 chiffres
    if len(cp) == 4 and cp.isdigit():
        return True, "Code postal valide."

    return False, "Le code postal doit être composé de 4 chiffres uniquement."


# ===========================================================================================================
def check_email(mon_adresse_mail):
    """
    Valide la structure d'une adresse e-mail.

    Args :
        → mon_adresse_mail (str) : L'adresse e-mail à vérifier.

    Returns :
        → tuple : (bool, str) Indique si la validation est réussie et fournit un message.

    Conditions de validité :
        → Un seul caractère '@' divisant l'adresse en deux parties.
        → La partie gauche contient uniquement des caractères alphanumériques, des points ou des tirets.
        → La partie droite est un domaine valide, avec un nom et une extension alphanumériques séparés par un point.
    """
    mon_adresse_mail_split = mon_adresse_mail.split("@")

    if len(mon_adresse_mail_split) != 2:
        return False, "Problème de @"

    for cara in mon_adresse_mail_split[0]:
        if not cara.isalnum() and cara not in (".", "-"):
            return False, "La partie de gauche contient des caractères interdits"

    mon_adresse_mail_droite = mon_adresse_mail_split[1].split(".")

    if len(mon_adresse_mail_droite) != 2:
        return False, "Le nom de domaine est mauvais"

    if mon_adresse_mail_droite[0].isalpha() and mon_adresse_mail_droite[1].isalpha():
        return True, "L'adresse est correcte"
    else:
        return False, "Le nom de domaine contient des caractères interdits"


# ===========================================================================================================
def check_login(login, users_list):
    """
    Vérifie la validité d'un login et sa disponibilité.

    Args :
        → login (str) : Le login à vérifier.
        → users_list (list) : La liste des utilisateurs existants, chaque utilisateur étant représenté par une liste.

    Returns :
        → tuple : (bool, str) Indique si la validation est réussie et fournit un message.

    Conditions de validité :
        → Vérifie si le login n'est pas déjà utilisé dans la liste des utilisateurs.
        → Le login doit contenir uniquement des lettres.
    """

    # Vérifier si le login est déjà utilisé dans la liste des utilisateurs
    if any(user[4] == login for user in users_list):
        return False, f'Login "{login}" est déjà pris. Choisissez un autre login.'

    # Vérifier que chaque caractère est une lettre
    for character in login:
        if not character.isalpha():
            return False, f"Le caractère invalide '{character}' a été détecté dans le login."

    return True, "Login valide"


# ===========================================================================================================
def check_mot_de_passe(mot_de_passe):
    """
    Valide un mot de passe en fonction de critères de sécurité.

    Args :
        → mot_de_passe (str) : Le mot de passe à vérifier.

    Returns :
        → tuple : (bool, str) Indique si la validation est réussie et fournit un message.

    Conditions de validité :
        → Longueur minimale de 10 caractères.
        → Au moins une lettre majuscule et une lettre minuscule.
        → Au moins un chiffre.
        → Au moins un caractère spécial.
    """

    contient_minuscule = False
    contient_majuscule = False
    contient_caractere_speciaux = False
    contient_chiffre = False
    longueur_minimum = False

    # critères de validation du mot de passe
    if len(mot_de_passe) >= 10:
        longueur_minimum = True

    for char in mot_de_passe:
        if char.islower():
            contient_minuscule = True
        elif char.isupper():
            contient_majuscule = True
        elif char.isdigit():
            contient_chiffre = True
        elif char in ("!", "@", "#", "$", "%", "^", "&", "*", "()", "-", "_", "=", "+", "[]", "{}", ";", "'", ":", "\"", ",", ".<>?/"):
            contient_caractere_speciaux = True

    if (longueur_minimum and
            contient_minuscule and contient_majuscule and contient_chiffre and contient_caractere_speciaux):
        return True, "Mot de passe valide."
    else:
        return False, ("Le mot de passe doit contenir au moins 10 caractères, 1 majuscule, 1 minuscule, "
                       "1 chiffre et un caractère spécial.")


# ===================================================================================================
# ===================================================================================================
# ===================================================================================================


# ======================================
# AFFICHAGE DES DONNEES D'UN UTILISATEUR
# ======================================
def afficher_utilisateur(numero, nom, prenom, cp, email, login, mot_de_passe):
    """Affiche les informations de l'utilisateur avec le mot de passe masqué."""
    print(f"\nInformations de l'utilisateur {numero} :")
    print(f"Nom : {nom}")
    print(f"Prénom : {prenom}")
    print(f"Code postal : {cp}")
    print(f"Email : {email}")
    print(f"Login : {login}")
    print(f"Mot de passe : {'*' * len(mot_de_passe)}")


# ======================================
# AFFICHAGE DE LA LISTE DES UTILISATEURS
# ======================================
def affichage_des_utilisateurs(utilisateurs_liste):
    print("\nLa liste des utilisateurs !")
    for i, utilisateur in enumerate(utilisateurs_liste):
        print(f"\nUtilisateurs n°{i + 1}")
        print(f"Nom : {utilisateur[0]}\n"
              f"Prénom : {utilisateur[1]}\n"
              f"Adresse (code postal) : {utilisateur[2]}\n"
              f"Email : {utilisateur[3]}\n"
              f"Login : {utilisateur[4]}\n"
              f"Mot de passe : {utilisateur[5]}")


# =====================================
# AFFICHAGE DU TABLEAU DES UTILISATEURS
# =====================================
def tableau_des_utilisateurs(utilisateurs_liste):
    print("\nTableau des utilisateurs !")
    # Affichage des en-têtes de colonne
    print(f"\n{'Numéro':<10} {'Nom':<15} {'Prénom':<20} {'Code postal':<15} {'Email':<30} "
          f"{'Login':<15} {'Mot de passe'}")

    # Affichage des lignes de données
    for i, utilisateur in enumerate(utilisateurs_liste):
        print(f"{i + 1:<10} {utilisateur[0]:<15} {utilisateur[1]:<20} {utilisateur[2]:<15} {utilisateur[3]:<30} "
              f"{utilisateur[4]:<15} {utilisateur[5]}")


# ======================================================================
# VALIDATION DES DONNEES GRACE AUX FONCTIONS DE VERIFICATION "check_..."
# ======================================================================
def verifier_entree(champ, valeur, fonction_verification, erreurs, message_erreur):
    valid, message = fonction_verification(valeur)
    while not valid:
        erreurs.append((champ, message))
        print(f"\nErreur {champ} : {message}")
        valeur = input(f"Corrigez {message_erreur} : ")
    return valeur


# =================================
# =================================
def enregistrer_utilisateur(utilisateurs_liste):
    # Demander les informations initiales
    nom = input("Nom : ").strip()
    prenom = input("Prénom : ").strip()
    cp = input("Code postal : ").strip()
    email = input("Email : ").strip()
    login = input("Login : ").strip().lower()
    mot_de_passe = input("Mot de passe : ").strip()

    erreurs_trouvees = True
    while erreurs_trouvees:
        erreurs = []

        # Vérifier nom et le prénom
        valid, message = check_nom_prenom(nom, prenom)
        if not valid:
            erreurs.append(("nom/prenom", message))
            print(f"\nErreur nom/prenom : {message}")
            nom = input("Corrigez le nom : ")
            prenom = input("Corrigez le prénom : ")
        else:
            # Capitalisation du nom et du prénom
            nom = ' '.join([part.capitalize() for part in nom.split(' ')])
            prenom = '-'.join([part.capitalize() for part in prenom.split('-')])

        # Vérifier code postal
        cp = verifier_entree("code postal", cp, check_cp, erreurs, "le code postal")

        # Vérifier email
        email = verifier_entree("email", email, check_email, erreurs, "l'email")

        # Vérifier login
        valid, message = check_login(login, utilisateurs_liste)
        if not valid:
            erreurs.append(("login", message))
            print(f"\nErreur login : {message}")
            login = input("Corrigez le login : ").lower()

        # Vérifier mot de passe
        mot_de_passe = verifier_entree("mot de passe", mot_de_passe, check_mot_de_passe, erreurs,
                                       "le mot de passe")

        # S'il n'y a pas d'erreurs, on ajoute l'utilisateur à la liste et on sort de la boucle.
        if not erreurs:
            utilisateurs_liste.append([nom, prenom, cp, email, login, '*' * len(mot_de_passe)])
            erreurs_trouvees = False

    # On retourne les données de l'utilisateur.
    return [nom, prenom, cp, email, login, '*' * len(mot_de_passe)]


def enregistrer_des_utilisateurs(nbr_utilisateurs_a_enregister):
    """Fonction pour enregistrer des utilisateurs."""

    users_list = []

    for i in range(nbr_utilisateurs_a_enregister):  # Permettre l'enregistrement de x utilisateurs
        print(f"\nEnregistrement de l'utilisateur {i + 1}")

        # Obtenir les informations initiales
        nom, prenom, cp, email, login, mot_de_passe = enregistrer_utilisateur(users_list)

        print("\nToutes les informations sont valides !")
        afficher_utilisateur(i + 1, nom, prenom, cp, email, login, mot_de_passe)

    # Affichage de TOUS les utilisateurs
    affichage_des_utilisateurs(users_list)
    tableau_des_utilisateurs(users_list)


# Lancer le programme
enregistrer_des_utilisateurs(3)
