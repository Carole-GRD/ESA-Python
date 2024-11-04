# Recherche des racines d'une équation a x + b y = c
# Charles Pecheur, septembre 2018

# solutions = 0
# a = int(input("Entrez la valeur du coefficient a : "))
# b = int(input("Entrez la valeur du coefficient b : "))
# c = int(input("Entrez la valeur du coefficient c : "))
# max_val = int(input("Entrez la valeur maximale pour x et y : "))
#
# for x in range(1, max_val+1):
#     for y in range(1, max_val+1):
#         if a*x + b*y == c:
#             print("x = ", x, " y = ", y)
#             solutions += 1
#
# if solutions == 0:
#     print("Aucune solutions trouvée")
# else:
#     print(solutions, "solutions trouvées")


# ======================================================



def find_linear_solutions(a, b, c, max_v):

    solutions = []
    for x in range(1, max_v + 1):
        for y in range(1, max_v + 1):
            if a * x + b * y == c:
                solutions.append((x, y))
                print("x = ", x, " y = ", y) # Impression d'une solution trouvée


    # Affichage du résultat final
    if solutions:
        print(f"{len(solutions)} solutions trouvées : {solutions}")
    else:
        print("Aucune solution trouvée : ", solutions)

    return solutions, len(solutions)



# if __name__ == '__main__':
#
#     try:
#         def validate_input(value):
#             if value.isdigit() or (value[0] == '-' and value[1:].isdigit()):
#                 data = int(value)
#                 return data
#             if type(value).__name__ == 'str':
#                 raise ValueError("La valeur doit être un entier.")
#
#         a_var = validate_input(input("Entrez la valeur du coefficient a : "))
#         b_var = validate_input(input("Entrez la valeur du coefficient b : "))
#         c_var = validate_input(input("Entrez la valeur du coefficient c : "))
#         max_val = validate_input(input("Entrez la valeur maximale pour x et y : "))
#
#         if int(max_val) <= 0:
#             raise ValueError("La valeur maximale doit être un entier positif (non nul).")
#
#         result = find_linear_solutions(a_var, b_var, c_var, max_val)
#
#         print(f"""\
#
#         ------------------------------------
#         result = {result}
#         ------------------------------------
#         """)
#
#     except ValueError as e:
#         print(f"Erreur : {e}")




def get_integer_input(prompt, allow_negative=False):
    """
    Fonction pour obtenir une entrée entière de l'utilisateur.
    :param prompt: Message affiché pour demander l'entrée.
    :param allow_negative: Si True, permet les nombres négatifs.
    :return: Valeur entière saisie par l'utilisateur.
    """
    while True:
        value = input(prompt)  # Demande à l'utilisateur de saisir une valeur.

        # Vérifie si la valeur est un entier valide
        if ((allow_negative and (value.isdigit() or (value[0] == '-' and value[1:].isdigit())))
                # -> vérifie si la valeur est un entier positif
                # ou un entier négatif (commence par '-' suivi de chiffres)
                or (not allow_negative and value.isdigit() and value != '0')):
                # -> vérifie si la valeur est un entier positif
                # (doit contenir uniquement des chiffres et ne pas être égal à '0')
            return int(value)  # Convertit la valeur en entier et la retourne.
        else:
            print("La valeur doit être un nombre entier." + (  # Affiche un message d'erreur.
                " (non nul)" if not allow_negative else ""))
            # -> Si les nombres négatifs ne sont pas autorisés, précise que la valeur doit être non nulle.


if __name__ == '__main__':

    # Obtenir les coefficients et la valeur maximale de l'utilisateur.
    a_var = get_integer_input("Entrez la valeur du coefficient a : ", allow_negative=True)
    b_var = get_integer_input("Entrez la valeur du coefficient b : ", allow_negative=True)
    c_var = get_integer_input("Entrez la valeur du coefficient c : ", allow_negative=True)
    max_val = get_integer_input("Entrez la valeur maximale pour x et y : ")  # max_val doit être positif.

    # Appelle la fonction pour trouver les solutions linéaires.
    result = find_linear_solutions(a_var, b_var, c_var, max_val)

    # Affiche le résultat des solutions trouvées.
    print(f"""\

       ------------------------------------
       result = {result}
       ------------------------------------
       """)