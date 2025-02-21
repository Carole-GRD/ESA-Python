"""
    Exercice :

    Essayez de créer un fichier contenant des entiers positifs.
    On s’arrête dès que le nombre introduit est négatif.

    Demander d'encoder un nombre, tant qu'on entre un nombre positif, on l'ajoute.
    Si on entre un nombre négatif, on sort de la boucle et on affiche les nombres ajoutés dans le fichier.
"""

# ==============================================================================================================
# ===========================================  MA VERSION  =====================================================
# ==============================================================================================================

# # Crée le fichier s'il n'existe pas et ouvre le fichier en mode "append" (les données seront ajoutées à la suite)
# fichier_nombres = open('fichier_nombres.txt', 'a')
#
# # Ajoute les nombres choisis par l'utilisateur dans le fichier
# nombre = 0
# while nombre >= 0:
#     try:
#         nombre = int(input('Nombre à ajouter : '))
#         if nombre >= 0:
#             fichier_nombres.write(str(nombre) + '\n')
#     except ValueError:
#         print('ERREUR : Entrer un nombre !')
#
# # Ferme le fichier
# fichier_nombres.close()
#
# # Ouvre le fichier en mode "lecture"
# fichier_nombres = open('fichier_nombres.txt', 'r')
#
# # Lit le fichier et stocke les données dans la variable "les_nombres" afin de les afficher
# les_nombres = fichier_nombres.read()
# print('\nVoici les nombres écris dans le fichier "fichier_nombres" :\n\n', les_nombres)
#
# # Ferme le fichier
# fichier_nombres.close()


# ==============================================================================================================
# ===========================================  AUTRE VERSION  ==================================================
# ==============================================================================================================


# ========================================  Réécrire le fichier  ===============================================

# Ouvrir un fichier en mode "écriture"
with open("nombres_positifs.txt", "w") as fichier:
    while True:
        try:
            nombre = int(input("Entrer un nombre : "))

            if nombre < 0:
                break

            fichier.write(f"{nombre}\n")
        except ValueError:
            print("ERREUR : Vous devez entrer un nombre entier valide. Réessayez.")
# Le fichier est automatiquement fermé ici, à la fin du bloc `with`

# Lire et afficher le contenu du fichier
with open("nombres_positifs.txt", "r") as fichier:
    contenu = fichier.read()
    print("Les nombres ajoutés dans le fichier sont :")
    print(contenu)


# ====================================  Écrire à la suite du fichier  ===========================================

# # Ouvrir un fichier en mode ajout ("a")
# with open("nombres_positifs.txt", "a") as fichier:
#     while True:
#         # Demander à l'utilisateur d'entrer un nombre
#         nombre = int(input("Entrez un nombre (entrez un nombre négatif pour arrêter) : "))
#
#         # Vérifier si le nombre est négatif
#         if nombre < 0:
#             break  # Sortir de la boucle si le nombre est négatif
#
#         # Ajouter le nombre positif dans le fichier
#         fichier.write(f"{nombre}\n")
#
# # Lire et afficher le contenu du fichier
# with open("nombres_positifs.txt", "r") as fichier:
#     contenu = fichier.read()
#     print("Les nombres ajoutés dans le fichier sont :")
#     print(contenu)


# ==============================================================================================================
# ===========================================  AUTRE VERSION  ==================================================
# ==============================================================================================================

# def ecrire_nombres_positifs(nom_fichier):
#     with open(nom_fichier, 'w') as fichier:
#         while True:
#             try:
#                 nombre = int(input("Entrez un nombre entier positif (nombre négatif pour arrêter) : "))
#                 if nombre < 0:
#                     break
#                 fichier.write(str(nombre) + '\n')
#             except ValueError:
#                 print("Veuillez entrer un nombre entier valide.")
#
#     print(f"Les nombres ont été enregistrés dans {nom_fichier}.")
#
#     # Lecture et affichage des nombres enregistrés
#     print("Les nombres enregistrés sont :")
#     with open(nom_fichier, 'r') as fichier:
#         for ligne in fichier:
#             print(ligne.strip())
#
#
# # Exécution du programme
# ecrire_nombres_positifs("nombres_positifs.txt")
