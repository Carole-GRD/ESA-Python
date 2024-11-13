"""
    Exercice 1 :

    Écrire un programme réalisant la facturation d’un article livré en N exemplaires.
    On fournira en données le nombre d’articles et leur prix hors-taxe.
    Le taux TVA sera toujours de 21 %.
    Si le montant dépasse 250 €, on établira une remise de 5 %.

    Le rendu se fera comme suit :
        ● nombre d’articles : n
        ● prix unitaire ht : xxx €
        ● montant ttc : xxx €
        ● remise : xxx €
        ● net à payer : xxx €
"""

# Encodage des valeurs par l'utilisateur
price_excl_vat = float(input("Introduisez le prix hors tva : "))
number_of_copies = int(input("Introduisez le nombre d'exemplaires : "))

# Calcul des différents montants
price_incl_vat = price_excl_vat * number_of_copies * 1.21
if price_incl_vat >= 250:
    discount = price_incl_vat * 0.05
else:
    discount = 0

# Affichage des résultats
print("Nombre d'articles : ", number_of_copies)
print("Prix unitaire htva : %.2f euros" % price_excl_vat)
print("Montant ttc : %.2f euros" % price_incl_vat)
print("Remise : %.2f euros" % discount)
print("Net à payer : %.2f euros" % (price_incl_vat-discount))
