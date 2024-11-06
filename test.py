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


# txt = "My name is Ståle"
#
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


"""
    Point d'arrêt pour déboguer

        ->  Utilisation du point-virgule : 
            Le point-virgule est nécessaire ici car nous plaçons deux instructions sur la même ligne, 
            ce qui est courant lors de l'utilisation de pdb pour insérer un point d'arrêt.
            
        ->  Placement du point d'arrêt : 
            On place l'arrêt en une seule ligne au-dessus de l'instruction ou de la variable 
            dont on veut connaître la valeur.
"""

# aaa = 5
# bbb = 10
#
# # Arrête le code ici, permet d'inspecter les variables avant d'exécuter les lignes suivantes.
# # ATTENTION : Après le débogage, n'oubliez pas de supprimer cette ligne pour éviter un arrêt involontaire.
# import pdb; pdb.set_trace()
#
# ccc = aaa + bbb
# print(ccc)


# ------AUTRE EXEMPLE -----


# def add(a, b):
#     somme = a + b
#     return somme
#
# x = 10
# y = '20'  # Erreur : addition d'un int et d'un str
#
# import pdb; pdb.set_trace()  # Point d'arrêt pour examiner `x` et `y`
#
# result = add(x, y)  # Cela va provoquer une erreur
# print(result)

"""
    Comment fonctionne pdb.set_trace() ?

        ->  pdb.set_trace() démarre le débogueur Python 
            et arrête l'exécution du code à l'endroit où il est inséré. 
            
        ->  Cela te permet de voir les valeurs des variables 
            et d'exécuter le code ligne par ligne à partir de cet endroit.
    
    
    Commandes de base dans pdb :
    
        ->  n (next) : Exécute la ligne actuelle et passe à la suivante.
        ->  c (continue) : Continue l'exécution jusqu'à la fin ou jusqu'au prochain point d'arrêt.
        ->  s (step) : Entre dans une fonction si la ligne actuelle en appelle une.
        ->  Tu peux également taper directement le nom d'une variable (par exemple ccc) pour obtenir sa valeur.
        ->  p <nom_de_variable> (print) : Affiche la valeur d'une variable spécifique.
        ->  q (quit) : Quitte le débogueur.

    ATTENTION : 
        
        Après avoir fini le débogage, il est important de supprimer ou de commenter la ligne 
        contenant pdb.set_trace() pour éviter que le programme ne s'arrête lors de son exécution normale.
"""


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



