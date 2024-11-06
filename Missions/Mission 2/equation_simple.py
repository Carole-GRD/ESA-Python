# Recherche des racines d'une équation a x + b y = c
# Charles Pecheur, septembre 2018
from sympy.codegen.cfunctions import expm1


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


def get_integer_input(prompt, allow_negative=False):
    """
    Fonction pour obtenir une entrée entière de l'utilisateur.
    :param prompt: Message affiché pour demander l'entrée.
    :param allow_negative: Si True, permet les nombres négatifs.
    :return: Valeur entière saisie par l'utilisateur.
    """

    while True:
        value = input(prompt)

        try:
            is_decimal = value.lstrip("-").replace(".", "", 1).isdigit() and "." in value

            if is_decimal:
                if not allow_negative and value.startswith("-"):
                    raise ValueError("Vous avez entré un nombre DECIMAL NEGATIF. "
                                     "Veuillez entrer un nombre ENTIER POSITIF.")
                else:
                    raise ValueError("Vous avez entré un nombre DECIMAL. "
                                     "Veuillez entrer un nombre ENTIER.")
            
            # Vérifie si l'entrée est non numérique
            if not value.lstrip("-").isdigit():
                raise ValueError("Vous avez entré des lettres ou des caractères non numériques. "
                                 "Veuillez entrer un nombre entier.")

            value = int(value)  # Convertit en entier après validation

            # Vérifie les conditions de validité
            if value <= 0 and not allow_negative:
                raise ValueError("La valeur doit être un nombre entier POSITIF non nul.")

            return value  # Retourne la valeur valide

        except ValueError as e:
            print("Erreur:\n", str(e))


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
