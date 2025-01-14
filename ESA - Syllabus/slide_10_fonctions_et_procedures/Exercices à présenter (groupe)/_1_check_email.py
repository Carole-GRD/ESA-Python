"""
    Faire un programme permettant d'encoder une adresse mail et
    vérifier si ce qui est encodé est bien valide au niveau syntaxe

    Rappel des règles :
        ● sous la forme de xxx@xxx.xx
        ● ne pourra contenir de caractères spéciaux autres que le "." ou le "-"
"""

# =======================================================================================
# ============================ SOLUTION DU GROUPE ======================================
# =======================================================================================


# programme qui verifie que l'adresse mail est conforme

# mail = input("entrer ton adresse mail : ")
#
#
# index = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)] + [chr(i) for i in range(48, 58)] + [".", "-","@"]
# end_index = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
# compteur = 0
# is_erreur = False
# if mail[0] == "@":
#     print("erreur : le mail ne peut pas commencer par un "@"")
# for lettre in mail:
#     if lettre == "@":
#         compteur += 1
#     if lettre not in index: # compare chaque caractere du mail et s'il a un caractere interdits !
#         print("Erreur : contient des caracteres interdits !!!")
#         is_erreur = True
#
#
# if compteur != 1:
#     print("Adresse mail invalide --> faute : @!")
#     is_erreur = True
# else:
#     split_mail = mail.split("@")
#     if split_mail[1][0] == ".":
#         print("erreur: au moins une lettre entre @ et . ")
#         is_erreur = True
#     if mail[len(mail)-1] not in end_index :
#         print("erreur: la fin du mail doit etre une lettre ")
#         is_erreur = True
#
# if is_erreur is False:
#     print("le mail est ok !!")
#


# =======================================================================================
# ============================ CORRECTION DU PROFESSEUR =================================
# =======================================================================================

# my_email_address = "toto@gmail.com"
# my_email_address = "to#to@gmail.com"
# my_email_address = "toto@gmail.com.be"
# my_email_address = "toto@gmail.com2"

# ----------------------------------------

my_email_address = input("Entrez l'adresse email : ")


def check_email(email):
    """
    Vérifie la validité d'une adresse email.

    : pre :
        — "email" est une chaîne de caractères non vide (str)
        — "email" contient au moins un caractère "@" séparant deux parties non vides
    : post :
        — Retourne un message indiquant si l'adresse email est correcte ou une erreur précise :
            - "Problème de @" si l'email ne contient pas exactement un caractère "@".
            - "La partie de gauche du @ contient des caractères interdits !" 
                si la partie avant "@" contient des caractères non autorisés (autres que alphanumériques, ".", ou "-").
            - "Le nom de domaine est mauvais !" si la partie après "@" 
                ne contient pas exactement un seul "." séparant deux parties non vides.
            - "Le nom de domaine contient des caractères interdits !" si les parties à droite de "." 
                dans le domaine ne contiennent que des caractères alphabétiques.
            - Si aucune erreur, retourne "L'adresse mail est correcte : {email}".
    """
    email_split = email.split("@")  # xxx@xxx.xx

    # print(email_split)
    if len(email_split) != 2:
        return "Problème de @"

    # print(my_email_address_split[0])
    for caractere in email_split[0]:    # Vérifions la partie à gauche du @
        if not caractere.isalnum() and caractere not in (".", "-"):
            return "La partie de gauche du @ contient des caractères interdits !"

    # Vérifions la partie de droite du @
    email_split_right = email_split[1].split(".")
    # print(my_email_address_split_right)

    if len(email_split_right) != 2:
        return "Le nom de domaine est mauvais !"

    if email_split_right[0].isalpha() and email_split_right[1].isalpha():
        return f"L'adresse mail est correcte : {email}"
    else:
        return "Le nom de domaine contient des caractères interdits !"


is_email_valid = check_email(my_email_address)
print(is_email_valid)

# =======================================================================================
# ============================ VERSION DE chatGPT ======================================
# =======================================================================================

# while True:
#     email = input("Entrez une adresse e-mail : ")
#
#     # Séparation de la partie locale et du domaine avec '@'
#     email_split = email.split("@")
#     if len(email_split) != 2 or not email_split[0] or not email_split[1]:
#         print("Erreur : L'adresse e-mail doit contenir exactement un '@' avec des parties non vides.")
#         continue
#
#     partie_locale = email_split[0]
#     partie_domaine = email_split[1]
#
#     # Vérification de la partie locale (avant le @)
#     partie_locale_valide = True
#     for char in partie_locale:
#         if not char.isalnum() and char not in (".", "-"):
#             print("Erreur : La partie avant le '@' contient des caractères non autorisés.")
#             partie_locale_valide = False
#             break
#
#     if not partie_locale_valide:
#         continue
#
#     # Vérification de la partie domaine (après le @)
#     domaine_split = partie_domaine.split(".")
#     if len(domaine_split) != 2 or not domaine_split[0] or not domaine_split[1]:
#         print("Erreur : La partie après le '@' doit contenir un domaine au format 'xxx.xx'.")
#         continue
#
#     nom_domaine = domaine_split[0]
#     tld = domaine_split[1]
#
#     # Vérification des caractères dans le domaine
#     if not nom_domaine.isalnum():
#         print("Erreur : Le nom de domaine (avant le '.') contient des caractères non autorisés.")
#         continue
#
#     # Vérification du TLD (top-level domain)
#     if not tld.isalpha() or len(tld) < 2:
#         print("Erreur : Le TLD (après le '.') doit être alphabétique et d'au moins 2 caractères.")
#         continue
#
#     # Si toutes les vérifications passent
#     print(f"L'adresse e-mail est valide : {email}")
#     break
#
#
# """
#     Résultat attendu
#
#     Entrées valides :
#         test.email@domaine.com → L'adresse email est valide : test.email@domaine.com
#
#     Entrées invalides :
#         test.email.com → Erreur : L'adresse e-mail doit contenir exactement un '@' avec des parties non vides.
#         @domaine.com → Erreur : L'adresse e-mail doit contenir exactement un '@' avec des parties non vides.
#
#         test!email@domaine.com → Erreur : La partie avant le '@' contient des caractères non autorisés.
#          test..email@domaine.com → Erreur : La partie avant le '@' contient des caractères non autorisés.
#
#         test.email@domaine..com → Erreur : La partie après le '@' doit contenir un domaine au format 'xxx.xx'.
#         test.email@com → Erreur : La partie après le '@' doit contenir un domaine au format 'xxx.xx'.
#         test.email@domaine.c → Erreur : Le TLD (après le '.') doit être alphabétique et d'au moins 2 caractères.
#
# """
