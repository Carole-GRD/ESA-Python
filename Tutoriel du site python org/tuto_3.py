
# -*- https://docs.python.org/fr/3/tutorial/introduction.html -*-
# -*- 3. Introduction informelle à Python -*-

# print("""\
# Usage: thingy [OPTIONS]
#      -h                        Display this usage message
#      -H hostname               Hostname to connect to
# """)


# ==================================================


# s1 = {1, 2, 3, 4, 5, 6}
# s2 = {6, 7, 8}
# s3 = '1, 2, 3, '

# print(s1 & s2)
# print(s1 | s2)
# print(s1, s2)
# print(s3 + '5, 6, 7')


# ==================================================


# rgb = ["Red", "Green", "Blue"]
# rgba = rgb
# print(f"id(rgb) : {id(rgb)}")
# print(f"id(rgba) : {id(rgba)}")
# print(id(rgb) == id(rgba))  # they reference the same object  -> True
#
# rgba.append("Alpha")
# # ATTENTION :
# # Si on ajoute "Alpha" uniquement à "rgba",
# # il sera également ajouter à "rgb" car ce sont des références vers le même objet
# # Si on ne veut l'ajouter qu'à "rgba", il faut alors faire une copie superficielle (voir ci-dessous)
#
# print(f"rgb : {rgb}")     # ["Red", "Green", "Blue", "Alpha"]
# print(f"rgba : {rgba}")     # ["Red", "Green", "Blue", "Alpha"]


# ----------------


# rgb = ["Red", "Green", "Blue"]
# rgba = rgb[:]                 # crée une copie superficielle du tableau rgb
#
# rgba.append("Alpha")          # ajoute uniquement à la copie superficielle
#
# print(f"rgb : {rgb}")  # la copie est modifiée
# print(f"rgba : {rgba}")  # la copie est modifiée


# ==================================================


# rgb = ["Red", "Green", "Blue"]
# rgba = rgb
# rgba.append("Alph")
#
#
# correct_rgba = rgba[:]   # crée une copie superficielle du tableau rgba
# print(f"correct_rgba : {correct_rgba}")
#
# correct_rgba[-1] = "Alpha"
# print(f"correct_rgba : {correct_rgba}")  # la copie est modifiée
# print(f"rgba : {rgba}")    # le tableau d'origine n'est aps modifié


# ==================================================


# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(letters)    # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(len(letters))
#
# # replace some values
# letters[2:5] = ['C', 'D', 'E']
# print(letters)     # ['a', 'b', 'C', 'D', 'E', 'f', 'g']
#
# # now remove them
# letters[2:5] = []
# print(letters)    # ['a', 'b', 'f', 'g']
#
# # clear the list by replacing all the elements with an empty list
# letters[:] = []
# print(letters)    # []
# print(len(letters))


# ==================================================


# a = ['a', 'b', 'c']
# n = [1, 2, 3]
# x = [a, n]
# print(x)        # [['a', 'b', 'c'], [1, 2, 3]]
# print(x[0])     # ['a', 'b', 'c']
# print(x[0][1])  # b


# ==================================================


# # Fibonacci series:
# # the sum of two elements defines the next
# a, b = 0, 1
# while a < 10:
#     print(a)
#     a, b = b, a+b


# a, b = 0, 1
# while a < 1000:
#     print(a, end=',')
#     a, b = b, a+b
