"""
Ce module contient un ensemble de fonctions pour la gestion des utilisateurs.

Les fonctionnalités incluent :
    → Vérification et validation des informations utilisateur (nom, prénom, email, login, etc.).
    → Affichage des informations des utilisateurs sous forme de liste ou de tableau formaté.
    → Enregistrement interactif de nouveaux utilisateurs avec validation des données.

Fonctions principales :
    → check_nom_prenom : Valide le nom et le prénom.
    → check_cp : Valide le code postal.
    → check_email : Valide une adresse e-mail.
    → check_login : Vérifie la disponibilité et la validité d'un login.
    → check_mot_de_passe : Valide un mot de passe selon des critères de sécurité.
    → afficher_utilisateur : Affiche les informations d'un utilisateur individuel.
    → affichage_des_utilisateurs : Affiche la liste des utilisateurs enregistrés.
    → tableau_des_utilisateurs : Affiche les utilisateurs sous forme de tableau formaté.
    → enregistrer_un_utilisateur : Guide l'utilisateur dans l'ajout d'un nouvel utilisateur avec validation.
    → enregistrer_des_utilisateurs : Permet l'enregistrement de plusieurs utilisateurs à la fois.
"""


# ===========================================================================================================
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

    if nom.lower() == prenom.lower():
        return False, "Veuillez entrer un nom et prénom différents"

    for cara in (nom, prenom):
        if "@" in cara or "." in cara:
            return False, "Les seuls caractères spéciaux acceptés sont le 'trait d'union'"

    if not all(c.isalpha() or c in '- ' for c in nom) or not all(c.isalpha() or c in '- ' for c in prenom):
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
    if len(cp) != 4 or not cp.isdigit():
        return False, "Le code postal doit être composé de 4 chiffres uniquement."

    if not (1000 <= int(cp) <= 9999):
        return False, "Le code postal doit être un nombre compris entre 1000 et 9999."

    return True, "Code postal valide."


# ===========================================================================================================
def check_email(mon_adresse_mail):
    """
    Valide la structure d'une adresse e-mail.

    Args :
        mon_adresse_mail (str) : L'adresse e-mail à vérifier.

    Returns :
        tuple : (bool, str)
            bool : indique si l'adresse est valide ou non
            str : message décrivant le résultat de la validation

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
    if any(user[4] == login.lower() for user in users_list):
        return False, f'Le login "{login.lower()}" est déjà pris. Choisissez un autre login.'

    # # Vérifier que chaque caractère est une lettre
    if not all(character.isalpha() for character in login):
        return False, f"Le login doit contenir uniquement des lettres."

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
        elif char in ("!", "@", "#", "$", "%", "^", "&", "*", "()", "-", "_", "=", "+", "[]", "{}", ";", "'", ":", "\"",
                      ",", ".<>?/"):
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
    """
    Affiche les informations de l'utilisateur avec le mot de passe masqué.

    Args :
        → numero (int) : Le numéro de l'utilisateur.
        → nom (str) : Le nom de l'utilisateur.
        → prenom (str) : Le prénom de l'utilisateur.
        → cp (str) : Le code postal de l'utilisateur.
        → email (str) : L'adresse e-mail de l'utilisateur.
        → login (str) : Le login de l'utilisateur.
        → mot_de_passe (str) : Le mot de passe de l'utilisateur (affiché masqué).

    Returns :
        None
    """
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
    """
    Affiche les informations des utilisateurs sous forme de liste.

    Args :
        utilisateurs_liste (list) : Liste des utilisateurs, où chaque utilisateur est une liste de données.

    Returns :
        None
    """
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
    """
    Affiche les informations des utilisateurs sous forme de tableau formaté.

    Args :
        utilisateurs_liste (list) : la liste des utilisateurs enregistrés
            utilisateur[0] : Nom (str)
            utilisateur[1] : Prénom (str)
            utilisateur[2] : Code postal (str)
            utilisateur[3] : Email (str)
            utilisateur[4] : Login (str)
            utilisateur[5] : Mot de passe (str)

    Returns :
        None : La fonction ne retourne rien mais affiche un tableau formaté.
    """
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
def lancer_verification(champ, valeurs, fonction_verification, erreurs, messages_erreurs_liste, *args):
    """
    Vérifie la validité d'une ou plusieurs valeurs via une fonction de validation.

    Args :
        → champ (str) : Le nom du champ à valider.
        → valeurs (list) : Les valeurs à valider (ex : [nom, prenom]).
        → fonction_verification (function) : La fonction de validation à utiliser.
        → erreurs (list) : Liste pour enregistrer les erreurs.
        → message_erreur (str) : Message d'erreur à afficher.
        → *args : Paramètres supplémentaires pour la fonction de validation.

    Returns :
        → list : Les nouvelles valeurs validées.
    """
    valid, message = fonction_verification(*valeurs, *args)
    if not valid:
        erreurs.append((champ, message))
        print(f"\nErreur {champ} : {message}")
        nouvelles_valeurs = []
        for message_erreur in messages_erreurs_liste:
            nouvelles_valeurs.append(input(f"Corrigez {message_erreur} : ").strip())
        valeurs = nouvelles_valeurs
    return valeurs if len(valeurs) > 1 else valeurs[0]


# =====================================
#      ENREGISTRER UN UTILISATEUR
# =====================================
def enregistrer_un_utilisateur(utilisateurs_liste):
    """
    Enregistre un nouvel utilisateur en validant ses informations (saisie, validation, ajout).

    Args :
        → utilisateurs_liste (list) : La liste existante des utilisateurs,
                                      où chaque utilisateur est une liste de données.

    Returns :
        → list : Les données de l'utilisateur validé (nom, prénom, code postal, email, login, mot de passe masqué).
    """

    # Saisies des différentes informations, avec nettoyage des espaces
    nom = input("Nom : ").strip()
    prenom = input("Prénom : ").strip()
    cp = input("Code postal : ").strip()
    email = input("Email : ").strip()
    login = input("Login : ").strip()
    mot_de_passe = input("Mot de passe : ").strip()

    champs_valides = False
    while not champs_valides:
        erreurs = []

        # Vérifier nom et le prénom
        nom, prenom = lancer_verification("nom/prenom", [nom, prenom], check_nom_prenom, erreurs,
                                          ["le nom", "le prénom"])

        # Vérifier code postal
        cp = lancer_verification("code postal", [cp], check_cp, erreurs, ["le code postal"])

        # Vérifier email
        email = lancer_verification("email", [email], check_email, erreurs, ["l'email"])

        # Vérifier login
        login = lancer_verification("login", [login], check_login, erreurs, ["le login"],
                                    utilisateurs_liste)
        login = login.lower()

        # Vérifier mot de passe
        mot_de_passe = lancer_verification("mot de passe", [mot_de_passe], check_mot_de_passe, erreurs,
                                           ["le mot de passe"])

        # S'il n'y a pas d'erreurs, on ajoute l'utilisateur à la liste et on sort de la boucle.
        if not erreurs:
            utilisateurs_liste.append([nom, prenom, cp, email, login, '*' * len(mot_de_passe)])
            champs_valides = True

    # On retourne les données de l'utilisateur.
    return [nom, prenom, cp, email, login, '*' * len(mot_de_passe)]


# =====================================
#     ENREGISTRER DES UTILISATEURS
# =====================================
def enregistrer_des_utilisateurs(nbr_utilisateurs_a_enregister):
    """
    Enregistre plusieurs utilisateurs (saisie, validation et affichage).

    Args :
        → nbr_utilisateurs_a_enregister (int) : Le nombre d'utilisateurs à enregistrer.

    Returns :
        → None
    """

    utilisateurs_liste = []

    for i in range(nbr_utilisateurs_a_enregister):  # Permettre l'enregistrement de x utilisateurs
        print(f"\nEnregistrement de l'utilisateur {i + 1}")

        # Obtenir les informations initiales
        nom, prenom, cp, email, login, mot_de_passe = enregistrer_un_utilisateur(utilisateurs_liste)

        print("\nToutes les informations sont valides !")
        afficher_utilisateur(i + 1, nom, prenom, cp, email, login, mot_de_passe)

    # Affichage de TOUS les utilisateurs
    affichage_des_utilisateurs(utilisateurs_liste)
    tableau_des_utilisateurs(utilisateurs_liste)


# =====================================
#      LANCER LE PROGRAMME
# =====================================
nbr_utilisateurs = int(input("Nombre d'utilisateurs à enregistrer : "))
enregistrer_des_utilisateurs(nbr_utilisateurs)
