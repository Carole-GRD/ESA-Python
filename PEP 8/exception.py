
# print("début")
# print(10 / 0)   # ZeroDivisionError: division by zero
# print("fin")

"""
    try - except - else
    try - excpet - finally

    try:            Bloc contenant le code susceptible de provoquer une erreur
    except ...:     Gérer l'erreur si elle survient
    else:           Bloc qui s'exécute uniquement si tout s'est bien passé (pas d'erreur survenue).
    finally:        Bloc toujours exécuté après, qu'une erreur soit survenue ou non
"""

# print("début")
# try:
#     print(10 / 0)
# except ZeroDivisionError:
#     print("Erreur: division par zéro")
# print("fin")


# =======================================


# Spécificité :

# Mauvaise pratique
# try:
#     print(10 / 5)      # Diviseurs : 0, 'deux', 2
# except Exception:
#     print("Une erreur s'est produite !")
#
#
# Bonne pratique
# try:
#     print(10 / 0)      # Diviseurs : 0, 'deux', 2
# except TypeError:
#     print("Erreur de type ! Entre des nombres !")
# except ZeroDivisionError:
#     print("Division par zéro !")





# =======================================

# Messages d'erreur clairs

class IbanError(Exception):
    """Exception levée pour une erreur dans le format de l'IBAN."""
    pass


def valider_iban(iban):
    try:
        # Suppression des espaces dans l'IBAN s'il y en a
        iban = iban.replace(" ", "")

        # Vérification de la longueur
        if len(iban) < 15 or len(iban) > 34:
            raise IbanError(
                f"Erreur : L'IBAN '{iban}' a une longueur incorrecte. Il doit contenir entre 15 et 34 caractères.")

        # Vérification du format
        if not iban[:2].isalpha() or not iban[2:].isdigit():
            raise IbanError(
                f"Erreur : L'IBAN '{iban}' est mal formaté. Il doit commencer par deux lettres suivies de chiffres.")

        # Si toutes les vérifications passent, IBAN est valide
        print(f"L'IBAN '{iban}' est valide.")

    except IbanError as e:
        print(e)


# Tests avec des IBAN corrects et incorrects
# print("\nTest 1 : IBAN valide")
# valider_iban("FR76 1234 5678 9012 3456 7890 123")
#
# print("\nTest 2 : IBAN trop court")
# valider_iban("FR76 123")
#
# print("\nTest 3 : IBAN mal formaté (caractères non valides)")
# valider_iban("FR76123A567B901234567890")
#
# print("\nTest 4 : IBAN mal formaté (manque lettres en début)")
# valider_iban("7612345678901234567890123")






# =======================================

# Nettoyage

def lire_fichier(nom_fichier):
    fichier = None
    try:
        fichier = open(nom_fichier, 'r')
        donnees = fichier.read()
        print(f"CONTENU DU FICHIER :\n{donnees}")
    except FileNotFoundError:
        print(f"Le fichier {nom_fichier} n'existe pas !")
    finally:
        print("LE BLOC FINALLY EST TOUJOURS EXECUTE")
        if fichier:
            fichier.close()
            print("FICHIER FERME")


# Utilisation
# lire_fichier("donnes.txt")








