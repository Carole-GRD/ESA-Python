import check_fullname as fullname
import check_cp as cp
import check_email as email


# def save_user():
#     fullname_result = ''
#     cp_result = ''
#     email_result = ''
#     # login_result = ''
#     # password_result = ''
#
#     while True:
#         # FULLNAME
#         if not fullname_result or fullname_result.startswith('ERREUR'):
#             if fullname_result.startswith('ERREUR'):
#                 print(fullname_result)
#             fullname_result = fullname.check_lastname_firstname()
#
#         # CODE POSTAL
#         if not cp_result or cp_result.startswith('ERREUR'):
#             if cp_result.startswith('ERREUR'):
#                 print(cp_result)
#             cp_result = cp.check_cp()
#
#         # EMAIL
#         if not email_result or email_result.startswith('ERREUR'):
#             if email_result.startswith('ERREUR'):
#                 print(email_result)
#             email_result = email.check_email()
#
#         # check_login()
#         # check_mot_de_passe()
#
#         if (not fullname_result.startswith('ERREUR')
#                 and not email_result.startswith('ERREUR')
#                 and not cp_result.startswith('ERREUR')):
#             break
#
#     print("Utilisateur enregistré")
#
#     return [fullname_result, cp_result, email_result]


# =========================================================================================================


# def save_user():
#     def validate_input(check_function, result):
#         """Valide une entrée et retourne un message ou un résultat."""
#         if not result or result.startswith("ERREUR"):
#             if result.startswith("ERREUR"):
#                 print(result)
#             return check_function()
#         return result
#
#     fullname_result = ''
#     cp_result = ''
#     email_result = ''
#
#     while True:
#         # FULLNAME
#         fullname_result = validate_input(fullname.check_lastname_firstname, fullname_result)
#
#         # CODE POSTAL
#         cp_result = validate_input(cp.check_cp, cp_result)
#
#         # EMAIL
#         email_result = validate_input(email.check_email, email_result)
#
#         # Vérifier si toutes les validations sont valides
#         if (not fullname_result.startswith('ERREUR') and
#                 not cp_result.startswith('ERREUR') and
#                 not email_result.startswith('ERREUR')):
#             break
#
#     print("Utilisateur enregistré")
#     return [fullname_result, cp_result, email_result]
#
#
# # users = []
# # for i in range(2):
# #     user = save_user()
# #     users.append(user)
# #     print(f"users : {users}")
#
# # print(f"users : {users}")


# =======================================================================================================


def save_user():
    def validate_input(check_function, result):
        """Valide une entrée et retourne un message ou un résultat."""
        if not result or result.startswith("ERREUR"):
            # if result.startswith("ERREUR"):
            #     print(result)
            return check_function()
        return result

    users_list = []
    number_of_users = int(input("Combien d'utilisateurs souhaitez-vous enregistrer : "))

    for each_user in range(number_of_users):
        fullname_result = ''
        cp_result = ''
        email_result = ''

        while True:
            # FULLNAME
            fullname_result = validate_input(fullname.check_lastname_firstname, fullname_result)

            # CODE POSTAL
            cp_result = validate_input(cp.check_cp, cp_result)

            # EMAIL
            email_result = validate_input(email.check_email, email_result)

            # Vérifier si toutes les validations sont valides
            if (not fullname_result.startswith('ERREUR') and
                    not cp_result.startswith('ERREUR') and
                    not email_result.startswith('ERREUR')):
                break

            # Afficher un rapport qui reprend l’état des différents encodages
            print(f"--------------------\n"
                  f"Nom prénom : {fullname_result}\n"
                  f"Code postal : {cp_result}\n"
                  f"Email : {email_result}\n"
                  f"---------------------")

        users_list.append([fullname_result, cp_result, email_result])
        print(f"\nUtilisateur enregistré : {[fullname_result, cp_result, email_result]}\n")

    return users_list


# multiple_users = [['spider man', '1000', 'spider@marvel.us'],
#                   ['gillet andy', '2000', 'andy@marvel.us'],
#                   ['goffaux anne-marie', '9999', 'a-m.goff@test.be'],
#                   ['legrand sophie', '5055', 'user@test.eu']]

multiple_users = save_user()

# ======================================
# AFFICHAGE DES DONNEES PAR UTILISATEURS
# ======================================

# # Affichage des utilisateurs
# for i, user in enumerate(multiple_users):
#     print(f"\nUtilisateurs n°{i+1}")
#     print(f"Nom prénom : {user[0]}\n"
#           f"Adresse (code postal) : {user[1]}\n"
#           f"Email : {user[2]}")


# =================================
# AFFICHAGE DES DONNEES EN COLONNES
# =================================

# Affichage des en-têtes de colonne
print(f"{'Numéro':<10} {'Nom prénom':<25} {'Code postal':<15} {'Email'}")

# Affichage des lignes de données
for i, user in enumerate(multiple_users):
    print(f"{i+1:<10} {user[0]:<25} {user[1]:<15} {user[2]}")
