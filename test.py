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


# print(1, end='\t')
# print(2)              # 1	2   (1 et 2 sur la même ligne, espacés d'une tabulation
#
# print(range(3))       # range(0, 3)
#
# print(print.__doc__)


# ================================================================================


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


# ================================================================================


# Erreurs PEP 8 intentionnelles afin de tester "Inspect Code... et les inspections PEPE 8"


# import os, sys
#
# MaVar = 5
# a = 7
#
# def exemple():
#     MaVar = 5
#     my_var = 10
#     anotherVar = 15
#
#
# print(os.path)
# print(sys.version)
#
# import math
# print(      math.pi)
# math.sqrt(25)
#
#
# class Solver:
#     def demo(self,demo1,demo2,demo3):
#         print(self,demo1,demo2,demo3)

"""
     Pour ajuster les inspections PEP 8
     
        Raccourci pour ouvrir les "Settings" : Ctrl + Alt + S
     
    ->  Allez dans File|Settings|Editor et sur la page Inspections, 
        tapez PEP 8 pour trouver toutes les inspections liées à PEP 8. 
        Par défaut, les violations de style de code PEP 8 ne sont pas mises en évidence.
    
    ->  Dans la liste déroulante Severity, choisissez Warning.
"""
