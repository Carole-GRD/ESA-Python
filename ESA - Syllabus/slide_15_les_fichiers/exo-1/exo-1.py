"""
    Exercice 1 :

    Écrire un programme qui lit un fichier texte et qui compte
    chaque lettre alphabétique (le résultat sera stocké dans un tableau).

    Par exemple :
        A B C D E F G ...
        22 4 8 7 15 2 0 ...
"""

# ==============================================================================================================
# ===========================================  MA VERSION  =====================================================
# ==============================================================================================================

# dico_alpha = {
#     'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
#     'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0,
#     'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
# }
#
# with open('texte.txt', 'r') as fichier:
#     texte = fichier.read().lower()
# # Le fichier est automatiquement fermé ici, à la fin du bloc `with`
#
# lettres_liste = []
# for lettre in texte:
#     if lettre.isalpha():
#         dico_alpha[lettre] += 1
#         if lettre not in lettres_liste:
#             lettres_liste.append(lettre)
#
# print("Le fichier contient :")
# for lettre in lettres_liste:
#     print(f"{dico_alpha[lettre]}x la lettre '{lettre}'")


# ==============================================================================================================
# ===========================================  AUTRE VERSION  ==================================================
# ==============================================================================================================


# Fonction pour compter les lettres dans un fichier
def compter_lettres(nom_fichier):
    # Dictionnaire pour stocker les occurrences de chaque lettre
    compteur = {}

    # Initialiser le compteur pour chaque lettre de l'alphabet
    for lettre in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        compteur[lettre] = 0

    with open(nom_fichier, "r") as fichier:
        contenu = fichier.read()
    # Le fichier est automatiquement fermé ici, à la fin du bloc `with`

    for caractere in contenu:
        if caractere.isalpha():
            lettre = caractere.upper()
            compteur[lettre] += 1

    return compteur


# Fonction pour afficher le résultat sous forme de tableau
def afficher_resultat(compteur):

    # Afficher uniquement les lettres présentes avec leur occurrence
    lettres = []
    for lettre in compteur:
        if compteur[lettre]:
            lettres.append(f"{lettre}: {compteur[lettre]}")
    print(f"Les lettres sont : {', '.join(lettres)}")

    # Afficher toutes les lettres avec leur occurrence
    resultat = [lettre + ': ' + str(compteur[lettre]) for lettre in compteur]
    print("Lettres :\n", "\n ".join(resultat))

    # Afficher toutes les lettres sous forme de tableau
    print(" ".join(compteur.keys()))
    print(" ".join(str(compteur[lettre]) for lettre in compteur))


# Compter les lettres dans le fichier
compteur_lettres = compter_lettres("texte.txt")

# Afficher le résultat
afficher_resultat(compteur_lettres)
