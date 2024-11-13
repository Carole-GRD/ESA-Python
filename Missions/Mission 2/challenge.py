
# -----------------------------------------------------
#                  Challenge 1
# -----------------------------------------------------


"""
    Consigne :

    Modifiez votre programme de façon à ce qu'il n'affiche que les racines
    qui n'ont aucun diviseur commun à l'exception de 1.
    Pour cela vous devrez écrire un programme permettant de vérifier si trois nombres ont un diviseur commun.
"""

# print("""\
#
# ---------------------------------------
#               Challenge 1
# ---------------------------------------
# """)


# =====================================================================================================
# =====================================================================================================
# =====================================================================================================

# -----------------------------------------------------
#                  Challenge 2
# -----------------------------------------------------


"""
    Consigne :

    En utilisant un programme qui test intelligemment tous les quadruplets possibles en utilisant des boucles 'for',
    pourriez-vous déterminer quel est le quadruplet pour lequel la somme a^3 + b^3 = c^3 + d^3 est minimale ?
"""

print("""\

---------------------------------------
              Challenge 2
---------------------------------------
""")

# limit = 100
# number_of_solutions = 0
# solutions = []
# sums = 0
# for a in range(1, limit):
#     for b in range(1, limit):
#         for c in range(1, limit):
#             for d in range(1, limit):
#                 if (a**3 + b**3 == c**3 + d**3) and a != b and a != c and a != d and b != c and b != d and c != d:
#                     if sums == 0:
#                         sums = a**3+b**3
#                         solutions.append([a, b, c, d])
#                         number_of_solutions += 1
#                     elif sums == a**3+b**3:
#                         solutions.append([a, b, c, d])
#                         number_of_solutions += 1
#     if number_of_solutions == 8:
#         break
#
#
# if number_of_solutions == 0:
#     print("Aucune solutions trouvée")
# else:
#     print(number_of_solutions, "solutions trouvées")
#     print(f"solutions : {solutions}")
#     print(f"sums : {sums}")


# ======================================================
# ==================  chatGPT  =========================
# ======================================================


# Limite de recherche
limite = 100

# Dictionnaire pour stocker les valeurs de a^3 + b^3
somme_cubes = {}

# Boucles pour tester les valeurs de a et b
for a in range(1, limite):
    for b in range(a, limite):  # b commence à a pour éviter les doublons
        somme = a**3 + b**3
        # Stocker les paires (a, b) correspondant à cette somme
        if somme not in somme_cubes:
            somme_cubes[somme] = [(a, b)]
        else:
            somme_cubes[somme].append((a, b))

# Variables pour la solution minimale
min_somme = float('inf')
quadruplet_min = None

# Recherche du quadruplet avec la somme minimale
for somme, paires in somme_cubes.items():
    if len(paires) > 1:  # Si on a plusieurs paires avec la même somme
        # Tester toutes les combinaisons possibles de paires
        for (a, b) in paires:
            for (c, d) in paires:
                if (a, b) != (c, d):  # éviter le même couple
                    if somme < min_somme:
                        min_somme = somme
                        quadruplet_min = (a, b, c, d)

# Affichage du résultat
if quadruplet_min:
    a, b, c, d = quadruplet_min
    print(f"Le quadruplet (a, b, c, d) = ({a}, {b}, {c}, {d}) a la somme minimale {min_somme}.")
else:
    print("Aucun quadruplet trouvé.")
