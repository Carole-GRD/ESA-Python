from sympy.ntheory.primetest import is_square

from check_square_matrix import is_square_matrix

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++  TESTS  ++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# =============
# SQUARE MATRIX
# =============
matrix = [[1, 2], [3, 4]]
# matrix = [[-1, 3], [-2, 1]]
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matrix = [[1, 2, 3, 10], [-5, 4, 5, 6], [7, 12, 8, 0], [0.5, 4, -5, 7]]

# ================
# NO SQUARE MATRIX
# ================
# matrix = [[1, 2], [3, 4], [5, 6]]
# matrix = [[1, 2], [3]]
# matrix = [[1, 2, 3], [3, 4], [5, 6]]
# matrix = [[1, 2], [3, 4, 7], [6, 7, 8]]
# matrix = [[1, 2, 3, 10], [-5, 4, 5, 6], [7, 12, 8, 0]]

# print(is_square_matrix(matrix))

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def calcul_det(m):
    is_square_m = is_square_matrix(m)
    # print(f"is_square = {is_square_m}")

    # Vérifie si la matrice est carrée
    if not is_square_m:
        return "La matrice n'est pas carrée !"

    # Vérifie si la matrice est d'ordre 2
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    else:
        return "La matrice n'est pas d'ordre 2 !"


det = calcul_det(matrix)
print(f"calcul_det : {det}")


