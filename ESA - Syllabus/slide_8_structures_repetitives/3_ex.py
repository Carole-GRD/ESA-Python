"""
    Exercice 3 :

    Écrire un programme qui demande le nombre de cote (sur 20) à introduire (maximum 5)
    et qui en calcul la moyenne de l’étudiant.

    Prévoyez la possibilité d’abandonner après chaque introduction de cote.
"""


# def valid_cote(number):
#     # prompt = Message spécifique pour la demande d'entrée (si premier input ou suite à une erreur)
#     prompt = f"Entrez une {number} cote sur 20 : "
#
#     # Encodage de la cote par l'utilisateur
#     while True:
#         cote = input(prompt)
#
#         try:
#             # Essayer de convertir en entier (si échoue, une exception est levée -> ValueError)
#             cote = float(cote)
#             # Vérifier si la cote est dans l'intervalle valide
#             if 0 <= cote <= 20:
#                 # cote = round(cote)
#                 break
#             else:
#                 prompt = "Entrez une cote comprise entre 0 et 20 : "
#
#         except ValueError:
#             # Si la conversion échoue, c'est que l'entrée n'est pas un nombre
#             prompt = "Entrez un nombre : "
#
#     return cote
#
#
# cote_1 = valid_cote("1re")
# cote_2 = valid_cote("2e")
# cote_3 = valid_cote("3e")
# cote_4 = valid_cote("4e")
# cote_5 = valid_cote("5e")
#
# # print(cote_1, cote_2, cote_3, cote_4, cote_5)
#
# average = (cote_1 + cote_2 + cote_3 + cote_4 + cote_5)/5
# print(f"Moyenne : {average}")


# =================================================================


def number_of_cote():
    """
        Prompts the user to enter the number of scores to input, between 1 and 5.

    Returns:
        int: The number of scores to input, between 1 and 5.
    """
    prompt = "Combien de cotes voulez-vous entrer (max 5) : "
    while True:
        try:
            number_cote = input(prompt)
            number_cote = int(number_cote)
            if 1 <= number_cote <= 5:
                return number_cote
            else:
                prompt = "Erreur : entrez un nombre entre 1 et 5 : "
        except ValueError:
            prompt = "Erreur : entrez des nombres ! \nCombien de cotes voulez-vous entrer (max 5) : "


def valid_cote(number):
    """
         Prompts the user to enter a score between 0 and 20.

     Args:
         number (int): The number of the score to be entered (1, 2, 3, etc.).

     Returns:
         float: The score entered by the user, between 0 and 20.
     """

    # prompt = Message spécifique pour la demande d'entrée (si premier input ou suite à une erreur)
    prompt = f"Entrez une {number}e cote sur 20 : "

    # Encodage de la cote par l'utilisateur
    while True:
        cote = input(prompt)

        try:
            # Essayer de convertir en entier (si échoue, une exception est levée -> ValueError)
            cote = float(cote)
            # Vérifier si la cote est dans l'intervalle valide
            if 0 <= cote <= 20:
                return cote
            else:
                prompt = "Entrez une cote comprise entre 0 et 20 : "

        except ValueError:
            # Si la conversion échoue, c'est que l'entrée n'est pas un nombre
            prompt = "Entrez un nombre : "


def average():
    """
        Calculates the average of the scores entered by the user.

    Returns:
        float: The average of the scores, rounded to 2 decimal places.
    """
    number_cote = number_of_cote()
    cotes = []
    sum_cotes = 0

    for cote in range(number_cote):
        cote = valid_cote(cote+1)
        cotes.append(cote)
        sum_cotes += cote

    print(f"Nombre de cotes : {number_cote}")
    print(f"Liste des cotes : {cotes}")
    print(f"Somme des cotes : {sum_cotes}")

    return sum_cotes / number_cote


average = average()
print(f"La moyenne est : {average:.2f}")


# help(number_of_cote)
# help(valid_cote)
# help(average)

