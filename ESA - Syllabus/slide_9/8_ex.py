"""
    Exercice 8 :

    Écrire un programme qui renvoie une chaîne de caractères reprenant les différents caractères
    utilisés dans une chaîne de caractères introduite par l'utilisateur.

    Aide :
        ● Une solution facile, mais ne correspondant pas au besoin serait de
          passer par un set (on verra plus tard ce que c'est).
            phrase = input("'Entrez la phrase : ")
            print(set(phrase))
        ● Ce que vous devez faire :
            parcourez la phrase et lorsque vous trouver un nouveau caractère
            (caractère not in caractere_deja_trouve [par exemple]),
            ajouter le dans caractere_deja_trouve.
"""

# chaine = "Écrire"
# chaine = "Écrire un programme ! 54 k H"
# chaine = "Kayak"
# chaine = "BAC"
# chaine = "Aacb"
# chaine = "AacbB"
# chaine = "AacbB583"
chaine = "AacbB583!?"


# ==================================================================================================
# ======================  Avec une chaîne pour accumuler les caractères  ==========================
# ==================================================================================================


def different_characters(chaine):
    characters_already_found = ""
    for c in chaine:
        if c not in characters_already_found:
            characters_already_found += c
    return characters_already_found


# ==================================================================================================
# =======================  Avec une liste pour accumuler les caractères  ==========================
# ==================================================================================================


# def different_characters(chaine):
#     characters_already_found = []
#     for c in chaine:
#         if c not in characters_already_found:
#             characters_already_found.append(c)
#     return ''.join(characters_already_found)


# ==================================================================================================
# =======  Ignorer la casse (majuscules/minuscules) et les caractères non alphanumériques   =========
# ==================================================================================================


# def different_characters(chaine):
#     characters_already_found = []
#     for char in chaine:
#         # Vérifier si le caractère est alphanumérique (on ignore les espaces, ponctuation, etc.)
#         # et si sa version en minuscule n'est pas déjà dans la liste
#         if char.isalnum() and char.lower() not in characters_already_found:
#             characters_already_found.append(char.lower())
#     return ''.join(characters_already_found)


# ==================================================================================================
# ===========================  Avec un set pour éliminer les doublons  =============================
# ==================================================================================================


# def different_characters(chaine):
#     unique_characters = set()     # Utiliser un set pour stocker les caractères uniques
#     for char in chaine:
#         unique_characters.add(char)
#     return ''.join(sorted(unique_characters))


print(different_characters(chaine))
