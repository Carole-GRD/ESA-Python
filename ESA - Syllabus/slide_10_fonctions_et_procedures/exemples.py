# def addition(x, y):
#     return x + y
#
#
# print(addition(5, 10))
# print(addition(7, 9))


# def subtraction(x, y):
#     return x - y
#
#
# print(subtraction(5, 9))
# print(subtraction(7, 9))


# def double_subtraction(x, y=10):
#     double = 2
#     # double = a
#     return x - (double * y)
#
#
# a = 5
# print(double_subtraction(a))
# print(double_subtraction(7, 9))


# def toto():
#     print("toto")
#
#
# toto()
# a = 5
# toto()


# def je_change(x):
#     x = "dede"
#
#
# a = 5           # Un integer est immutable ????
# je_change(a)    # x reçoit une copie de la valeur "a" (une autre case mémoire)
#                 # une fois sortie de la procédure x n'existe plus
# print(a)        # 5
#
#
# def je_change2(x):
#     x.append(2)
#
#
# a = [5]           # Une liste est mutable.
# je_change2(a)     # x reçoit la valeur de "a" (la même case mémoire)
# print(a)          # [5, 2]


# def mutabilite(x):
#     x = [5]  # Crée une nouvelle liste locale et redéfinit x pour qu'il pointe vers cette liste.
#     print(x)  # Affiche la nouvelle liste [5].
#
#
# a = [2]
# mutabilite(a)
# print(a)  # Affiche [2], car l'objet original n'est pas modifié.
#
# """
#     Explication :
#     - x = [5] redéfinit localement la référence de x pour qu'il pointe vers une nouvelle liste.
#     - Cela n'affecte pas l'objet original référencé par a, car seule la référence locale x change.
#     - L'objet original (la liste [2]) reste inchangé.
# """
#
#
# def mutabilite2(x):
#     x.append(5)  # Modifie directement la liste existante.
#     print(x)  # Affiche la liste modifiée [2, 5].
#
#
# a = [2]
# mutabilite2(a)
# print(a)  # Affiche [2, 5], car l'objet original est modifié.
#
# """
#     Explication :
#     - x.append(5) modifie directement l'objet mutable (la liste).
#     - x et a pointent vers le même objet, donc la modification persiste après la sortie de la fonction.
# """


# =================================================

# print(1, end=" ")
# print(2, end=" ")
# print(3)                     # 1 2 3
#
# print(1, 5, 7, end="toto")   # 1 5 7toto
# print('')
# print(1, 5, 7, sep="toto")   # 1toto5toto7
# print('')
#
# print(print.__doc__)

# =================================================


# def tri(tab):
#     tab.sort()
#
#
# mon_tab = [5, 4, 9]
# print(mon_tab)
# tri(mon_tab)
# print(mon_tab)


# def foo(premier, second, troisieme, *args):
#     print("Premier: %s" % premier)
#     print("second: %s" % second)
#     print("Troisième: %s" % troisieme)
#     print("And all the rest... {0}".format(list(args)))
#     print(args)
#
# foo(1, 2, 3, 4, 5, 6)
