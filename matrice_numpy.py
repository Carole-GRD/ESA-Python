

# ================================================================================


import numpy as np

# print("===========================================")
# print("version de numpy :", np.__version__)
# print("===========================================")



# print("===========================================")
# # Définir les nouvelles matrices 3x3 A12, A13, A14
# A12_new = np.array([[3, 2, 0],
#                     [1, -2, -2],
#                     [0, -3, 1]])
#
# A13_new = np.array([[3, 1, 0],
#                     [1, 3, -2],
#                     [0, 1, 1]])
#
# A14_new = np.array([[3, 1, 2],
#                     [1, 3, -2],
#                     [0, 1, -3]])
#
# # Calculer les déterminants des sous-matrices
# det_A12_new = np.linalg.det(A12_new)
# det_A13_new = np.linalg.det(A13_new)
# det_A14_new = np.linalg.det(A14_new)
#
# print("Les déterminants des sous-matrices sont : ")
# print(f"det_A12_new : {det_A12_new:.2f}")
# print(f"det_A13_new : {det_A13_new:.2f}")
# print(f"det_A14_new : {det_A14_new:.2f}")
# print(f"Calcul du déterminant : -6 * -26 + 1 * 14 + 2 * (-16) : {-6 * det_A12_new + det_A13_new + 2 * det_A14_new}" )
# print("===========================================")





# print("===========================================")
# # Définir la matrice 4x4
# A = np.array([[0, 6, 1, -2],
#               [3, 1, 2, 0],
#               [1, 3, -2, -2],
#               [0, 1, -3, 1]])
#
# # Calculer le déterminant de la matrice 4x4
# determinant = np.linalg.det(A)
#
# # Afficher le déterminant
# print(f"Le déterminant de la matrice est : {determinant:.2f}")
# print("===========================================")





# print("===========================================")
# # Définir la matrice d'origine
# A = np.array([[0, 6, 1, -2],
#               [3, 1, 2, 0],
#               [1, 3, -2, -2],
#               [0, 1, -3, 1]])
#
# # Fonction pour calculer le déterminant d'une matrice 3x3
# def det_3x3(mat):
#     return (mat[0, 0] * (mat[1, 1] * mat[2, 2] - mat[1, 2] * mat[2, 1]) -
#             mat[0, 1] * (mat[1, 0] * mat[2, 2] - mat[1, 2] * mat[2, 0]) +
#             mat[0, 2] * (mat[1, 0] * mat[2, 1] - mat[1, 1] * mat[2, 0]))
#
# # Calcul des mineurs
# def minor(mat, row, col):
#     return np.delete(np.delete(mat, row, axis=0), col, axis=1)
#
# # Calcul des cofacteurs
# cofactors = np.zeros(A.shape)
#
# for i in range(A.shape[0]):
#     for j in range(A.shape[1]):
#         # Calculer le mineur
#         minor_matrix = minor(A, i, j)
#         # Calculer le déterminant du mineur
#         minor_det = det_3x3(minor_matrix)
#         # Calculer le cofacteur
#         cofactors[i, j] = ((-1) ** (i + j)) * minor_det
#
# print("Cofacteurs : ")
# print(cofactors)
# print("===========================================")





print("===========================================")
# Matrice des cofacteurs fournie
cofactors_matrix = np.array([
    [-18, 26, 14, 16],
    [39, 5, 8, 19],
    [21, -15, -24, -57],
    [6, 22, -20, 56]
])

# Déterminant
det_A = 138

# Calcul de l'inverse de la matrice A
inverse_A = (1 / det_A) * cofactors_matrix


print("Inverse : ")
print(inverse_A)
print("===========================================")




# print("===========================================")
# # MATH
# # Algèbre linéaire - Partie 4
# # Diapo 1- / Exercice - 8
#
# # Importer numpy à nouveau après la réinitialisation
# # import numpy as np
#
# # Définir la matrice A et le vecteur b
# A = np.array([[0.15, 0.75, 0.25], [9, 24, 15], [1, 1, 1]])
# b = np.array([35.6, 1590, 108])
#
# # Résoudre le système Ax = b
# x_values = np.linalg.solve(A, b)
# print(f'x = {x_values}')
# # print(x_values[0])
# # print(x_values[1])
# # print(x_values[2])
# print(f'La valeur marchande est : {(44 * 402) + (26 * 1462) + (38 * 749)} €')
# print("===========================================")