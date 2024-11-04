# Recherche des racines d'une équation x^a + y^b = z^c


print("""\

-------------------------------------------------------
Recherche des racines d'une équation x^a + y^b = z^c            
-------------------------------------------------------
""")

# solutions = 0
# a = int(input("Entrez la valeur du coefficient a : "))
# b = int(input("Entrez la valeur du coefficient b : "))
# c = int(input("Entrez la valeur du coefficient c : "))
# max_val = int(input("Entrez la valeur maximale pour x et y et z : "))

# for x in range(1, max_val+1):
#     for y in range(1, max_val+1):
#         for z in range(1, max_val+1):
#             if x**a + y**b == z**c:
#                 print("x = ", x, " y = ", y, " z = ", z)
#                 solutions += 1
#
# if solutions == 0:
#     print("Aucune solutions trouvée")
# else:
#     print(solutions, "solutions trouvées")



def find_power_solutions(a, b, c, max_v):

    solutions = []

    for x in range(1, max_v+1):
        for y in range(1, max_v+1):
            for z in range(1, max_v+1):
                if x**a + y**b == z**c:
                    print("x =", x, " y =", y, " z =", z)
                    solutions.append((x, y, z))

    if solutions == 0:
        print("Aucune solutions trouvée")
    else:
        print(len(solutions), "solutions trouvées", solutions)

    return solutions, len(solutions)


if __name__ == '__main__':

    a_var = int(input("Entrez la valeur du coefficient a : "))
    b_var = int(input("Entrez la valeur du coefficient b : "))
    c_var = int(input("Entrez la valeur du coefficient c : "))
    max_val = int(input("Entrez la valeur maximale pour x et y et z : "))

    result = find_power_solutions(a_var, b_var, c_var, max_val)

    print(f"result : {result}")



# a = 3, b = 2, c = 9  =>  x =  7  y =  13  z =  2
# 7**3 + 13**2 = 2**9
# 343 + 169 = 512


# a = 7, b = 3, c = 2, max_v = 100
# =>  x =  1  y =  2  z =  3  =>  1**7 + 2**3 = 3**2  => 1 + 8 = 9
# =>  x =  2  y =  17  z =  71
# =>  x =  3  y =  9  z =  54
# result : ([(1, 2, 3), (2, 17, 71), (3, 9, 54)], 3)


# a = 5, b = 4, c = 2, max_v = 100
# =>  x =  3  y =  3  z =  18
# 3**5 + 3**4 = 18**2
# 243 + 81 = 324


# a = 3, b = 2, c = 7  =>  x =  4  y =  8  z =  2
# 4**3 + 8**2 = 2**7
# 64 + 64 = 128

