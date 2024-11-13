"""
    Exercice 2 :

    Même énoncé qu’à l'exercice précédent (1_tva.py)
    mais avec un taux TVA variable à choisir parmi 5 possibilités : 0 %, 6 %, 12 %, 18 % et 21 %.
    N’oubliez-pas d’afficher le taux lors du résultat final.
"""

# Encodage des valeurs par l'utilisateur
vat = int(input("Choississez la tva (0%, 6%, 12%, 18% ou 21%) : "))
if vat in (0, 6, 12, 18, 21):
    print("Nous aurons une tva de %s%%" % vat)
else:
    print("La tva encodée est incorrect, le programme va s'auto-détruire")
    exit()
price_excl_vat = float(input("Introduisez le prix hors tva : "))
number_of_copies = int(input("Introduisez le nombre d'exemplaires : "))

# Calcul des différents montants
price_incl_vat = price_excl_vat * number_of_copies * (100+vat)/100
if price_incl_vat >= 250:
    discount = price_incl_vat * 0.05
else:
    discount = 0

# Affichage des résultats
print("Nombre d'articles : ", number_of_copies)
print("Prix unitaire htva : %.2f euros" % price_excl_vat)
# print("TVA : %s%%" % vat)
print("Montant ttc : %.2f euros" % price_incl_vat)
print("Remise : %.2f euros" % discount)
print("Net à payer : %.2f euros" % (price_incl_vat-discount))

