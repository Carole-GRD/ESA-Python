# ==================================================================================================================

# Exercice 8 : qui calcul le pgcd de 2 entiers strictement positifs [à l’aide de structures alternatives et
# répétitives uniquement]

# ==================================================================================================================


# ===========
# MA VERSION
# ===========


# n_1 = int(input('Premier nombre : '))
# n_2 = int(input('Deuxième nombre : '))
#
#
# def euclide(max_value, min_value):
#     while min_value != 0:
#         r = max_value % min_value
#         max_value = min_value
#         min_value = r
#     return max_value
#
#
# def find_pgcd(n1, n2):
#
#     # Détermine le plus petit et le plus grand nombre
#     # if n1 < n2:
#     #     max_value = n2
#     #     min_value = n1
#     # else:
#     #     max_value = n1
#     #     min_value = n2
#
#     # pgcd = euclide(max_value,min_value)
#
#     pgcd = euclide(n1, n2)
#
#     print(f'Le PGCD de {n1} et {n2} est {pgcd}')
#
#
# find_pgcd(n_1, n_2)



"""
    REMARQUE :
    
    Pas besoin de vérifier le plus grand et le plus petit,
    l'algorithme d'Euclide fonctionne sans cela.
    
    EXEMPLE =>   VOIR IMAGE :    pgcd-algorithme-euclide.png
        
"""




# =====================
# VERSION DE GEMINI AI     -    Algorithme d'Euclide
# =====================

"""
    Soient a et b sont deux entiers naturels non nuls avec a > b et r le reste de la division euclidienne de a par b.

        Si r ≠ 0 alors :   PGCD(a ; b) = PGCD(b ; r)
"""

# def pgcd(a, b):
#   while b != 0:
#     a, b = b, a % b
#   return a
#
# # Demande à l'utilisateur de saisir deux nombres
# nombre1 = int(input("Entrez le premier nombre : "))
# nombre2 = int(input("Entrez le deuxième nombre : "))
#
# # Appel de la fonction et affichage du résultat
# resultat = pgcd(nombre1, nombre2)
# print("Le PGCD de", nombre1, "et", nombre2, "est :", resultat)






# ===================
# VERSION DE chatGPT   -   Méthode des soustractions successives
# ===================

"""
    Cet algorithme est une version simplifiée de l'algorithme d'Euclide,
    qui se base sur des soustractions répétées plutôt que des divisions pour trouver le PGCD.

    Soient a et b sont deux entiers naturels non nuls 
                            
                            avec a > b alors :

                                  PGCD( a ; b ) = PGCD( a - b ; b )
                                  
                            avec a < b alors :
                            
                                PGCD( a ; b ) = PGCD( a ; b - a )
"""


# def pgcd(a, b):
#     while b != 0:
#         if a > b:
#             a = a - b
#         else:
#             b = b - a
#     return a
#
# # Exemple d'utilisation
# a = int(input("Entrez le premier entier strictement positif: "))
# b = int(input("Entrez le deuxième entier strictement positif: "))
#
# if a > 0 and b > 0:
#     result = pgcd(a, b)
#     print(f"Le PGCD de {a} et {b} est : {result}")
# else:
#     print("Les deux nombres doivent être strictement positifs.")