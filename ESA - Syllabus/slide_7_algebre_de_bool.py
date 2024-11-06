
# ================================================================================
#                             Algèbre de bool (silde 7)
# ================================================================================


# ================================d
# Inverser deux variables avec XOR
# ================================d

# a = 2
# b = 5
# print('a = ', a, ' b = ', b)   # a =  2  b =  5
#
# a = a ^ b
# # 2 (en binaire : 010) XOR 5 (en binaire : 101) = 7 (en binaire : 111)
# print('a = ', a, ' b = ', b)   # a =  7  b =  5
#
# b = a ^ b
# # 7 (en binaire : 111) XOR 5 (en binaire : 101) = 2 (en binaire : 010)
# print('a = ', a, ' b = ', b)   # a =  7  b =  2
#
# a = a ^ b
# # 7 (en binaire : 111) XOR 2 (en binaire : 010) = 5 (en binaire : 101)
# print('a = ', a, ' b = ', b)   # a = 5  b = 2


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# ==================
# Règle de priorités
# ==================

# Ajouter des parenthèses pour rendre le code plus "lisible" et simplifier si possible

# a, b, c = 2, 3, 4
#
# exp = 2 * a % 5 * 4 + b - 3 / pow(c + 2, 2)            # 18.916666666666668
# exp = ((((2 * a) % 5) * 4) + b) - (3 / pow(c + 2, 2))  # 18.916666666666668
# exp = (((2 * a) % 5) * 4) + b - (3 / pow(c + 2, 2))    # 18.916666666666668
#
# print(exp)

# ----------------------------------------------

# a, b, c = 2, 3, 4
#
# exp = a or b or a and not b       # 2
# exp = a or b or (a and (not b))   # 2
# exp = a or b                      # 2
#
# print(exp)

# ----------------------------------------------

# a, b, c = 2, 3, 4
#
# exp = 2 * - a - 4 - - b / 4            # -7.25
# exp = ((2 * (- a)) - 4) - ((- b) / 4)  # -7.25
# exp = (2 * (- a)) - 4 - ((- b) / 4)    # -7.25
#
# print(exp)

# ----------------------------------------------

# a, b, c = 2, 3, 4
#
# exp = a < b - c * - b + a          # True
# exp = a < ((b - (c * (- b))) + a)  # True
# exp = a < (b - (c * (- b)) + a)    # True
#
# print(exp)

# ----------------------------------------------

# a, b, c = 2, 3, 4
#
# exp = a * a + a * a       # 8
# exp = (a * a) + (a * a)   # 8
# exp = 2 * (a * a)         # 8
# exp = 2 * pow(a, 2)       # 8
#
# print(exp)


