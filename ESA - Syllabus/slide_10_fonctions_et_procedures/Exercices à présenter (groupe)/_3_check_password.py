"""
    Faire un programme permettant d'encoder un mot de passe et vérifier
    si celui-ci contient au minimum 10 caractères, avec au minimum 1
    minuscule, 1 majuscule et 1 chiffre.
"""

# =========================================================================
# ============================   TESTS  ==================================
# =========================================================================

# my_password = "012345678"          # Au moins 10 caractères !
# my_password = "0123456789"         # Erreur : ...  (pas de minuscule, majuscule)
# my_password = "01234567890"        # Erreur : ...  (pas de minuscule, majuscule)

# my_password = "012abc6789"         # Erreur : ...  (pas de majuscule)
# my_password = "012ABC6789"         # Erreur : ...  (pas de minuscule)
# my_password = "abcdeFGHIJ"         # Erreur : ...  (pas de chiffre)
# my_password = "/@!-;:=+%_"         # Erreur : ...  (pas de majuscule, minuscule, chiffre)
# my_password = "abcdehghij"         # Erreur : ...  (pas de majuscule, chiffre)
# my_password = "ABCDEFGHIJ"         # Erreur : ...  (pas de minuscule, chiffre)


# my_password = "01abc56ABC"         # OK : mot de passe valide
# my_password = "!=?01abc56ABC"      # OK : mot de passe valide

# =========================================================================
# ===========================   MON CODE  =================================
# =========================================================================

# while True:
#     has_lower = False
#     has_upper = False
#     has_digit = False
#
#     my_password = input("Mot de passe : ")
#
#     if len(my_password) < 10:
#         print("Au moins 10 caractères !")
#         continue
#
#     for character in my_password:
#         if character.islower():
#             has_lower = True
#         if character.isupper():
#             has_upper = True
#         if character.isdigit():
#             has_digit = True
#
#     if has_lower and has_upper and has_digit:
#         print("OK : mot de passe valide")
#         break
#     elif not has_lower and has_upper and has_digit:
#         print("Invalide : doit contenir au minimum 1 minuscule !")
#     elif has_lower and not has_upper and has_digit:
#         print("Invalide : doit contenir au minimum 1 majuscule !")
#     elif has_lower and has_upper and not has_digit:
#         print("Invalide : doit contenir au minimum 1 chiffre !")
#     elif not has_lower and not has_upper and has_digit:
#         print("Invalide : doit contenir au minimum 1 minuscule et 1 majuscule !")
#     elif not has_lower and has_upper and not has_digit:
#         print("Invalide : doit contenir au minimum 1 minuscule et 1 chiffre !")
#     elif has_lower and not has_upper and not has_digit:
#         print("Invalide : doit contenir au minimum 1 majuscule et 1 chiffre !")
#     else:
#         print("Invalide : doit contenir au minimum 1 minuscule, 1 majuscule et 1 chiffre !")


# =========================================================================
# ================   MON CODE optimisé avec chatGPT  ======================
# =========================================================================


# def check_password():
#     while True:
#         my_password = input("Mot de passe : ")
#
#         # Liste pour stocker les erreurs
#         errors = []
#
#         # Vérifie la longueur
#         if len(my_password) < 10:
#             errors.append("10 caractères")
#
#         has_lower = False
#         has_upper = False
#         has_digit = False
#
#         # Vérifie les autres critères
#         for character in my_password:
#             if character.islower():
#                 has_lower = True
#             elif character.isupper():
#                 has_upper = True
#             elif character.isdigit():
#                 has_digit = True
#
#             # Sortir dès que tous les critères sauf la longueur sont remplis
#             if has_lower and has_upper and has_digit:
#                 break
#
#         # Ajout des erreurs restantes
#         if not has_lower:
#             errors.append("1 minuscule")
#         if not has_upper:
#             errors.append("1 majuscule")
#         if not has_digit:
#             errors.append("1 chiffre")
#
#         # Affichage du message et sortie de la boucle et la fonction si le mot de passe est correct
#         if not errors:
#             print("OK : mot de passe valide")
#             return
#         else:
#             print(f"Invalide : doit contenir au minimum {', '.join(errors)} !")
#
#
# check_password()

# =========================================================================
# ========   AUTRE VERSION de chatGPT avec la méthode any()  =============
# =========================================================================

# def check_password():
#     """
#     Valide un mot de passe selon les critères suivants :
#     - Longueur minimale : 10 caractères
#     - Contient au moins 1 minuscule, 1 majuscule, et 1 chiffre
#     Redemande à l'utilisateur tant que le mot de passe est invalide.
#     """
#     min_length = 10  # Longueur minimale configurable
#
#     while True:
#         password = input("Mot de passe : ")
#
#         # Initialiser une liste pour collecter les erreurs de validation
#         errors = []
#
#         # Vérifier la longueur minimale
#         if len(password) < min_length:
#             errors.append(f"{min_length} caractères")
#
#         # Vérifier les types de caractères -> any() s'arrête dès qu'il trouve un caractère qui satisfait la condition
#         has_lower = any(c.islower() for c in password)
#         has_upper = any(c.isupper() for c in password)
#         has_digit = any(c.isdigit() for c in password)
#
#         # Ajouter des messages d'erreur si les critères ne sont pas remplis
#         if not has_lower:
#             errors.append("1 minuscule")
#         if not has_upper:
#             errors.append("1 majuscule")
#         if not has_digit:
#             errors.append("1 chiffre")
#
#         # Afficher le résultat ou les erreurs
#         if not errors:
#             print("OK : mot de passe valide")
#             return
#         else:
#             print(f"Invalide : votre mot de passe doit contenir au moins {', '.join(errors)} !")
#
#
# check_password()

# =========================================================================
# =========================================================================
# =========================================================================


def verifie_mot_de_passe():
    """
        Valide un mot de passe selon les critères suivants :
            Longueur minimale : 10 caractères
            Contient au moins 1 minuscule, 1 majuscule, et 1 chiffre
        Redemande à l'utilisateur tant que le mot de passe est invalide.
    """
    while True:
        mpd = input("Entre un mot de passe avec 10 caracteres, min un chiffre, min une majuscule et une minuscule : ")

        if len(mpd) < 10:
            print("ERREUR : le mot de passe doit contenir 10 caracteres")

        maj = False
        min = False
        nbr = False
        for i in mpd:
            if i.isupper():
                maj = True
            if i.islower():
                min = True
            if i.isnumeric():
                nbr = True
        if not maj:
            print("ERREUR : il faut une majuscule")
        if not min:
            print("ERREUR : il faut  minuscule")
        if not nbr:
            print("ERREUR  : il faut un chiffre")
        elif maj and min and nbr:
            print("le code est correct")
            return


verifie_mot_de_passe()
