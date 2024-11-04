"""
    1. Utiliser les exceptions pour les cas exceptionnels


    Ne pas utiliser les exceptions pour contrôler le flux normal du programme.
    Les exceptions doivent être réservées aux cas où une condition exceptionnelle survient.
    --------- IDEM exprimé autrement
    L'idée ici est de ne pas utiliser les exceptions pour des conditions courantes,
    mais pour des situations vraiment exceptionnelles.
    --------
"""








# ====================================================================

# print(10 / 0)   # ZeroDivisionError: division by zero


"""
    try:            Code susceptible de provoquer une erreur
    except ...:     Gérer l'erreur
"""


# try:
#     num1 = int(input("Entrez un nombre : "))
#     num2 = int(input("Entrez un autre nombre : "))
#     resultat = num1 / num2
#     print("Le résultat de la division est :", resultat)
# except ValueError:
#     print("Veuillez entrer des nombres entiers.")
# except ZeroDivisionError:
#     print("Vous ne pouvez pas diviser par zéro.")
# # except Exception as e:
# #     print("Exception : Une erreur inattendue s'est produite :", e)
# # except BaseException as b:
# #     print("BaseException : Une erreur inattendue s'est produite :", b)
# finally:
#     print("Fin du bloc try-except-finally")



# def get_positive_number():
#     while True:
#         try:
#             number = int(input("Enter a positive number: "))
#             if number < 0:
#                 raise ValueError("negative number")
#             return number
#         # except ValueError:
#         #     print("Please enter a valid positive integer.")
#         except ValueError as e:
#             if str(e) == "negative number":
#                 print(f"Error: You entered a {e}. Please try again.")
#             else:
#                 print("Please enter a valid positive integer.")
#
#
#
# print(get_positive_number())




# =======================================
import math


# Clarté et spécificité

def diviser_et_convertir(numerateur, denominateur, base):

    try:
        # Effectuer la division
        resultat = numerateur / denominateur
        # Arrondir le résultat à l'entier le plus proche
        resultat_arrondi = round(resultat)
        # Convertir l'entier dans la base spécifiée
        return print(f"{numerateur} / {denominateur} = {int(str(resultat_arrondi), base)}")

    except ZeroDivisionError:
        print("Erreur : Division par zéro.")

    except ValueError as e:
        print(f"Erreur de valeur : {e}")
        # Vérification des erreurs spécifiques de conversion
        if str(e).startswith("invalid literal for int()"):
            print("La conversion en entier a échoué. Vérifiez la base.")
        elif str(e).startswith("int() base must be"):
            print(f"Base invalide : {base}. Utilisez 2, 8, 10, ou 16.")

    except ArithmeticError as e:
        print(f"Erreur arithmétique générale : {e}")

    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")


# # Tests
# print("\nTest 0 : Division normale")
# diviser_et_convertir(10, 2, 10)
#
# print("\nTest 1 : Division par zéro")
# diviser_et_convertir(10, 0, 10)
#
# print("\nTest 2 : Base invalide (base doit être 2, 8, 10, ou 16)")
# diviser_et_convertir(10, 2, 3)
#
# print("\nTest 3 : Base négative (invalide)")
# diviser_et_convertir(10, 2, -5)
#
# print("\nTest 4 : Erreur de conversion (en base 2, il n'y a que des 0 et des 1)")
# diviser_et_convertir(10, 3, 2)
#
# print("\nTest 5 : Erreur inattendue (simulation avec une chaîne en entrée)")
# diviser_et_convertir("dix", 2, 10)
#
#
# # Test déclenchant un OverflowError avec un très grand nombre
# print("\nTest 6 : OverflowError (Erreur arithmétique générale)")
# try:
#     large_number = math.exp(1000)  # Provoque une valeur énorme qui peut causer un OverflowError
#     diviser_et_convertir(large_number, 1, 10)
# except OverflowError as e:
#     print(f"Erreur arithmétique générale (OverflowError capturée) : {e}")






def diviser(a, b):
    try:
        print(f" {a} / {b} = {a / b}")
    except Exception:
        print(f"Erreur : {Exception.__name__}")
    except TypeError:
        print("Les opérandes doivent être des nombres.")
    except ZeroDivisionError:
        print("Division par zéro.")
    # except Exception:
    #     print(f"Erreur : {Exception.__name__}")

# diviser(10, 'deux')
# diviser(10, 0)
# diviser(10, 5)

# =======================================

# Messages d'erreur clairs

class AgeError(Exception):
    """Exception levée pour des âges invalides."""

    def __init__(self, age):
        super().__init__(f"Invalid age: {age}. Age must be between 0 and 130.")


def validate_age(age):
    """Valide que l'âge est compris entre 0 et 130."""
    if not isinstance(age, int):
        raise TypeError(f"Expected an integer for age, but got {type(age).__name__}.")

    if age < 0 or age > 130:
        raise AgeError(age)

    print(f"Age {age} is valid.")


# # Exemple d'utilisation
# try:
#     validate_age(25)  # Devrait réussir
#     # validate_age(-5)  # Devrait lever AgeError
#     # validate_age("twenty")  # Devrait lever TypeError
#     # validate_age(bac)  # name 'bac' is not defined
# except AgeError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# except Exception as e:
#     print(e)


class IbanError(Exception):
    """Exception levée pour une erreur dans le format de l'IBAN."""
    pass


def valider_iban(iban):
    try:
        # Suppression des espaces dans l'IBAN s'il y en a
        iban = iban.replace(" ", "")

        # Vérification de la longueur minimale et du format
        if len(iban) < 15 or len(iban) > 34:
            raise IbanError(
                f"Erreur : L'IBAN '{iban}' a une longueur incorrecte. Il doit contenir entre 15 et 34 caractères.")

        if not iban[:2].isalpha() or not iban[2:].isdigit():
            raise IbanError(
                f"Erreur : L'IBAN '{iban}' est mal formaté. Il doit commencer par deux lettres suivies de chiffres.")

        # Si toutes les vérifications passent, IBAN est valide
        print(f"L'IBAN '{iban}' est valide.")

    except IbanError as e:
        print(e)


# Tests avec des IBAN corrects et incorrects
print("\nTest 1 : IBAN valide")
valider_iban("FR76 1234 5678 9012 3456 7890 123")

print("\nTest 2 : IBAN trop court")
valider_iban("FR76 123")

print("\nTest 3 : IBAN mal formaté (caractères non valides)")
valider_iban("FR76123A567B901234567890")

print("\nTest 4 : IBAN mal formaté (manque lettres en début)")
valider_iban("7612345678901234567890123")






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











#
# def traiter_donnees_fichier(nom_fichier):
#     fichier = None
#     try:
#         fichier = open(nom_fichier, 'r')
#         donnees = fichier.read()
#         print("Contenu du fichier :")
#         print(donnees)
#         return traiter(donnees)
#     except FileNotFoundError:
#         print(f"Le fichier {nom_fichier} n'existe pas.")
#         return None
#     except ValueError as e:
#         print(f"Erreur lors du traitement des données : {e}")
#         return None
#     finally:
#         if fichier:
#             fichier.close()
#             print("Fichier fermé.")
#
# def traiter(donnees):
#     # Simulons un traitement simple, comme compter les lignes
#     return len(donnees.splitlines())
#
# # Utilisation
# resultat = traiter_donnees_fichier("C:\\Users\\gerar\\OneDrive\\2022 Documents\\ESA\\Premiere\\donnees.txt")
# if resultat is not None:
#     print(f"Traitement réussi. Nombre de lignes : {resultat}")
#
