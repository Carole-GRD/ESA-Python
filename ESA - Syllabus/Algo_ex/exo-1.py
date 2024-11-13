# ==================================================================================================================

# Exercice 1 : qui lit la valeur du rayon d’un cercle et affiche la valeur de la circonférence (hypothèse : le
# nombre introduit est positif)

# ==================================================================================================================



# VERSION 1


# import math
#
# PI = math.pi
#
# while True:
#     try:
#         # Demander à l'utilisateur de saisir un nombre
#         rayon = float(input("rayon : "))
#
#         # Vérifier si le nombre est positif
#         if rayon > 0:
#             # Calculer la circonference du cercle puis l'afficher et sortir de la boucle
#             perimetre = 2 * PI * rayon
#             aire = PI * pow(rayon, 2)
#
#             print(f"La circonférence d'un cercle de rayon {rayon} est {round(perimetre, 2)}")
#             print(f"La superficie d'un cercle de rayon {rayon} est {round(aire, 2)}")
#
#             break
#         else:
#             print("Le rayon doit être un nombre positif. Veuillez réessayer.")
#
#     # Gérer les erreurs si l'utilisateur entre autre chose qu'un nombre
#     except ValueError:
#         print("Erreur : Vous devez entrer un nombre valide.")






# ==================================================================================================================
# ==================================================================================================================
# ==================================================================================================================


# VERSION 2


"""
    Pour ajouter une option permettant de quitter la boucle en cas d’erreurs répétées,
    tu peux introduire un compteur d’erreurs. Si le nombre d’erreurs dépasse un certain seuil,
    le programme peut proposer à l’utilisateur de quitter ou de réessayer.
"""
import math

PI = math.pi
max_erreurs = 3  # Nombre maximum d'erreurs autorisées
compteur_erreurs = 0

while True:
    try:
        rayon = float(input("rayon : "))

        if rayon > 0:
            perimetre = 2 * PI * rayon
            aire = PI * pow(rayon, 2)

            print(f"La circonférence d'un cercle de rayon {rayon} est {round(perimetre, 2)}")
            print(f"La superficie d'un cercle de rayon {rayon} est {round(aire, 2)}")
            break
        else:
            print("Le rayon doit être un nombre positif. Veuillez réessayer.")
            compteur_erreurs += 1
    except ValueError:
        print("Erreur : Vous devez entrer un nombre valide.")
        compteur_erreurs += 1

    # Vérifier si le nombre maximum d'erreurs est atteint
    if compteur_erreurs >= max_erreurs:
        quitter = input("Vous avez fait trop d'erreurs. Voulez-vous quitter ? (oui/non) : ").strip().lower()
        if quitter == 'oui':
            print("Programme terminé.")
            break
        else:
            compteur_erreurs = 0  # Réinitialiser le compteur d'erreurs
