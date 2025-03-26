"""
    Exercice2 :

    Reprenez l’implémentation de la pile en ajoutant la notion de taille maximum.
    La pile devra contenir les fonctionnalités supplémentaires suivantes :
        ● Connaître la taille maximum ;
        ● Savoir si la pile est pleine ;
        ● Copier une pile vers une pile qui est au minimum de la même taille.
"""

from utils.pile_file import *

# ma_pile = creer_pile()
#
# print(est_vide(ma_pile))
#
# for caractere in 'Hello':
#     empiler(ma_pile, caractere)
#
# affiche_pile(ma_pile)
#
# print(est_vide(ma_pile))
#
# depiler(ma_pile)
#
# affiche_pile(ma_pile)
#
# for i in range(5):
#     depiler(ma_pile)
#
# affiche_pile(ma_pile)


# Création d'une pile avec une taille maximum de 3
ma_pile = creer_pile(taille_max=3)

# Vérification si la pile est vide
print("Est vide :", est_vide(ma_pile))

# Empiler des éléments
print("\nEmpilage d'éléments...")
for caractere in 'Hello':
    empiler(ma_pile, caractere)

# Afficher la pile
print("\nPile après empilement :")
afficher_pile(ma_pile)

# Vérification si la pile est pleine
print("\nEst pleine :", est_pleine(ma_pile))

# Dépiler un élément
print("\nDépilement d'un élément...")
depiler(ma_pile)
afficher_pile(ma_pile)

# Dépiler plusieurs fois (pour tester l'erreur)
print("\nTentative de dépiler plusieurs fois...")
for _ in range(5):
    depiler(ma_pile)

# Taille maximum de la pile
print("\nTaille maximum :", taille_maximum(ma_pile))

# Copier la pile dans une autre
print("\nCopie de la pile...")
autre_pile = creer_pile(taille_max=2)  # Pile cible trop petite
copier(ma_pile, autre_pile)
print("\nAutre pile après tentative de copie :")
afficher_pile(autre_pile)

# -------------------

print("\n====================================")
print("========== AUTRE TEST ==============")
print("====================================")

# Création d'une pile avec une taille maximum de 3
nouvelle_pile = creer_pile(taille_max=5)

# Afficher la pile
print("\nNouvelle pile vide :")
afficher_pile(nouvelle_pile)

# Empiler des éléments
print("\nEmpilage d'éléments...")
for caractere in 'Hello':
    empiler(nouvelle_pile, caractere)

# Afficher la pile
print("\nNouvelle pile remplie :")
afficher_pile(nouvelle_pile)

# Taille maximum de la nouvelle pile
print("\nTaille maximum :", taille_maximum(nouvelle_pile))

# Copier la pile dans une autre
print("\nCopie de la nouvelle pile...")
autre_nouvelle_pile = creer_pile()
# Taille maximum de l'autre nouvelle pile
print("\nTaille maximum de l'autre pile :", taille_maximum(autre_nouvelle_pile))
copier(nouvelle_pile, autre_nouvelle_pile)

print("\nAutre nouvelle pile après tentative de copie :")
afficher_pile(autre_nouvelle_pile)
# Taille maximum de l'autre nouvelle pile
print("\nTaille maximum de l'autre pile :", taille_maximum(autre_nouvelle_pile))