# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++  TESTS  ++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# =============
# SQUARE MATRIX
# =============
# matrix = [[1, 2], [3, 4]]
# matrix = [[-1, 3], [-2, 1]]
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = [[1, 2, 3, 10], [-5, 4, 5, 6], [7, 12, 8, 0], [0.5, 4, -5, 7]]

# ================
# NO SQUARE MATRIX
# ================
# matrix = [[1, 2], [3, 4], [5, 6]]
# matrix = [[1, 2], [3]]
# matrix = [[1, 2, 3], [3, 4], [5, 6]]
# matrix = [[1, 2], [3, 4, 7], [6, 7, 8]]
# matrix = [[1, 2, 3, 10], [-5, 4, 5, 6], [7, 12, 8, 0]]

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def is_square_matrix(m):
    """
    Checks if a given matrix is square.

    A square matrix has the same number of rows and columns. This function
    verifies that each row in the matrix has a length equal to the number of rows.

    Parameters:
    m (list of lists): The matrix to check, represented as a list of lists where
                       each inner list represents a row of the matrix.

    Returns:
    bool: True if the matrix is square, False otherwise.
    """
    len_m = len(m)
    for row in m:
        if len(row) != len_m:
            return False
    return True


if __name__ == '__main__':
    print(is_square_matrix(matrix))

