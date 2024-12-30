"""
Module pour l'enregistrement des utilisateurs.

Ce module permet de collecter et de valider les informations personnelles des utilisateurs
(nom, prénom, code postal, e-mail, login, mot de passe) à l'aide de fonctions de validation externes.
Il enregistre ces informations et les affiche sous forme de tableau.
"""


import check_fullname as fullname
import check_cp as cp
import check_email as email
import check_login as login
import check_password as pwd


def save_user():
    """
    Enregistre une liste d'utilisateurs après validation de leurs informations.

    Pour chaque utilisateur, les informations suivantes sont demandées et validées :
        → Nom et prénom (via 'fullname.check_lastname_firstname')
        → Code postal (via 'cp.check_cp')
        → Email (via 'email.check_email')
        → Login (via 'login.check_login')
        → Mot de passe (via 'pwd.check_password')

    La fonction demande à l'utilisateur combien d'utilisateurs il souhaite enregistrer,
    valide les données saisies pour chacun, affiche un rapport en cas d'erreur,
    et les stocke dans une liste.

    Returns :
        list : Une liste contenant les informations des utilisateurs enregistrés.
              Chaque élément de la liste est une sous-liste au format :
              [nom prénom, code postal, email, login, mot de passe].
    """

    def data_validation(check_function, result, login_list):
        """
        Valide des données saisies par l'utilisateur.

        Args :
            * check_function (function) : La fonction utilisée pour valider l'entrée utilisateur.
            * result (str) : Le résultat de la validation précédente.
            * login_list (list) : Liste des logins existants pour éviter les doublons.

        Returns :
            str : Le résultat validé ou une nouvelle tentative si l'entrée est invalide.
        """
        if result.startswith("ERREUR") or not result:
            if login_list is None:
                return check_function()
            else:
                return check_function(login_list)
        return result

    users_list = []
    login_list = []
    while True:
        try:
            number_of_users = int(input("Combien d'utilisateurs souhaitez-vous enregistrer : "))
            if number_of_users < 0:
                print("Le nombre d'utilisateurs ne peut pas être négatif. Veuillez entrer un nombre positif.")
            else:
                break
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

    # number_of_users = int(input("Combien d'utilisateurs souhaitez-vous enregistrer : "))

    for _ in range(number_of_users):
        fullname_result = ''
        cp_result = ''
        email_result = ''
        login_result = ''
        password_result = ''

        while True:
            # FULLNAME
            fullname_result = data_validation(fullname.check_lastname_firstname, fullname_result, None)

            # CODE POSTAL
            cp_result = data_validation(cp.check_cp, cp_result, None)

            # EMAIL
            email_result = data_validation(email.check_email, email_result, None)

            # LOGIN
            login_result = data_validation(login.check_login, login_result, login_list)

            # PASSWORD
            password_result = data_validation(pwd.check_password, password_result, None)

            # Vérifier si toutes les validations sont valides
            if (not fullname_result.startswith('ERREUR') and
                    not cp_result.startswith('ERREUR') and
                    not email_result.startswith('ERREUR') and
                    not login_result.startswith('ERREUR') and
                    not password_result.startswith('ERREUR')):
                break

            # Afficher un rapport qui reprend l’état des différents encodages
            print(f"--------------------\n"
                  f"Nom prénom : {fullname_result}\n"
                  f"Code postal : {cp_result}\n"
                  f"Email : {email_result}\n"
                  f"Login : {login_result}\n"
                  f"Mot de passe : {password_result}\n"
                  f"---------------------")

        users_list.append([fullname_result, cp_result, email_result, login_result, password_result])
        login_list.append(login_result)
        print(f"\nUtilisateur enregistré : "
              f"{[fullname_result, cp_result, email_result, login_result, password_result]}\n")

    return users_list


# users_list = [['spider man', '1000', 'spider@marvel.us', 'spiderman', 'Pwd_100000'],
#                   ['gillet andy', '2000', 'andy@marvel.us', 'andy', 'Pwd_200000'],
#                   ['goffaux anne-marie', '9999', 'a-m.goff@test.be', 'anne', 'Pwd_300000'],
#                   ['guiot sophie', '5055', 'sophie@test.eu', 'fifi', , 'Pwd_400000']]

users_list = save_user()

# ======================================
# AFFICHAGE DES DONNEES PAR UTILISATEURS
# ======================================

# Affichage des utilisateurs
for i, user in enumerate(users_list):
    print(f"\nUtilisateurs n°{i + 1}")
    print(f"Nom prénom : {user[0]}\n"
          f"Adresse (code postal) : {user[1]}\n"
          f"Email : {user[2]}\n"
          f"Login : {user[3]}\n"
          f"Mot de passe : {user[4]}")


# =================================
# AFFICHAGE DES DONNEES EN COLONNES
# =================================

# Affichage des en-têtes de colonne
print(f"\n{'Numéro':<10} {'Nom prénom':<35} {'Code postal':<15} {'Email':<30} {'Login':<15} {'Mot de passe'}")

# Affichage des lignes de données
for i, user in enumerate(users_list):
    print(f"{i + 1:<10} {user[0]:<35} {user[1]:<15} {user[2]:<30} {user[3]:<15} {user[4]}")
