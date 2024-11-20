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
#         if character.isalpha() and character.islower():
#             has_lower = True
#         if character.isalpha() and character.isupper():
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

while True:
    # Réinitialisation des drapeaux
    has_lower = False
    has_upper = False
    has_digit = False

    my_password = input("Mot de passe : ")

    # Vérifie la longueur du mot de passe
    if len(my_password) < 10:
        print("Invalide : au moins 10 caractères !")
        continue  # Recommence la boucle

    # Parcours des caractères
    for character in my_password:
        if character.islower():
            has_lower = True
        elif character.isupper():
            has_upper = True
        elif character.isdigit():
            has_digit = True

        # Si tous les critères sont remplis, on peut sortir de la boucle for
        if has_lower and has_upper and has_digit:
            break

    # Vérification finale et messages
    if has_lower and has_upper and has_digit:
        print("OK : mot de passe valide")
        break  # Sortie de la boucle while
    else:
        # Construction du message d'erreur
        errors = []
        if not has_lower:
            errors.append("1 minuscule")
        if not has_upper:
            errors.append("1 majuscule")
        if not has_digit:
            errors.append("1 chiffre")
        print(f"Invalide : doit contenir au minimum {', '.join(errors)} !")


