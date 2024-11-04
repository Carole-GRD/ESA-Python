# print("hello world")
#
# age=50
#
# myAge=46
# name="Carole"
#
# print(f'Je m\'appelle {name} et j\'ai {age} ans.')
#
# def foo():
#     if myAge > age:
#         print(f"J'ai PLUS que {age} ans.")
#     else:
#         print(f"J'ai MOINS que {age} ans.")
#
# foo()
#
# print(type(age))
# print(type(name))


# ================================================================================


# from math import *

# a=float(0.01)
# for i in range(9):
#     a+=5
#     print(a)


# print(int(sqrt(25)))
# print(sqrt(12.5))

# ================================================================================

# import random
#
# # Lancer le dé et deviner sa valeur
# de = random.randint(1, 6)
# valeur = 0
# while valeur != de :
#     valeur = int(input("Devinez la valeur du dé (entre 1 et 6) : "))
#     # try:
#     #     valeur = int(input("Devinez la valeur du dé (entre 1 et 6) : "))
#     # except ValueError:
#     #     print("Veuillez entrer un nombre entier.")
#     #     continue
# print("Gagné")


# ================================================================================


# nombre_1 = 3.14159
# print(round(nombre_1))  # Affiche : 3
# print(round(nombre_1, 2 ))  # Affiche : 3.14
# print("{:.2f}".format(nombre_1))  # Affiche : 3.14
#
#
# nombre_2 = 3
# print(round(nombre_2))  # Affiche : 3
# print(f"{nombre_2:.2f}")  # Affiche : 3.00
# print("{:.2f}".format(nombre_2))  # Affiche : 3.00


# ================================================================================


# TESTS ENCODING

# # initializing string
# String = "geeksforgeeks"
#
# encoded_string = String.encode('utf-8')
# print('The encoded string in base64 format is :')
# print(encoded_string)
#
# decoded_string = encoded_string.decode('utf-8')
# print('The decoded string is :')
# print(decoded_string)




# # initializing string
# string = "é - @ - # 52 - §"
#
# print(string)
#
# encoded_string = string.encode('utf-8')
# print('The encoded string in base64 format is :')
# print(encoded_string)
#
# decoded_string = encoded_string.decode('utf-8')
# print('The decoded string is :')
# print(decoded_string)





txt = "My name is Ståle"

# print(txt)
# print(txt.encode("UTF-8"))
# print(txt.encode("UTF-8").decode("UTF-8"))



# str="Hello! Welcome to Tutorialspoint."
# str_encoded = str.encode('utf_16','strict')
# print("The encoded string is: ", str_encoded)
# str_decoded = str_encoded.decode('utf_16', 'strict')
# print("The decoded string is: ", str_decoded)




# string = "Café"
#
# encoded_bytes = string.encode('utf-8')
# print(encoded_bytes)  # Affiche : b'Caf\xc3\xa9'
#
# decoded_string = encoded_bytes.decode('utf-8')
# print(decoded_string)  # Affiche : Café


# ================================================================================

# print(1, end = '\t')
# print(2)
#
# print(range(3))
#
# print(print.__doc__)



# Pour documenter le code : taper 3 guillemets puis enter cela propose
def toto(a, b, c):
    """

        :param a:
        :param b:
        :param c:
        :return:
        """

# help(toto)
# print(toto.__name__)
# print(toto.__doc__)





