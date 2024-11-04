

# ==================================================================================================================

# Exercice 2 : qui calcul la TVA et le prix net à partir du prix hors taxe et du taux à appliquer (en %)

# ==================================================================================================================


# VERSION 1


# taux = int(input("Taux en % : "))
#
# prix_ht = float(input("Prix en € : "))
#
# tva = prix_ht * taux / 100
#
# prix_ttc = prix_ht + tva
#
#
# print(f"Montant de la TVA {tva:.2f}€ - Prix net {prix_ttc:.2f}€")




# ==================================================================================================================


# VERSION 2


# Fonction pour calculer la TVA et le prix TTC
def calculer_tva_et_prix_ttc(prix_ht, taux_tva):
    # Calcul de la TVA
    montant_tva = prix_ht * (taux_tva / 100)

    # Calcul du prix TTC (prix HT + TVA)
    prix_ttc = prix_ht + montant_tva

    return montant_tva, prix_ttc


# Exemple d'utilisation :
prix_ht = float(input("Entrez le prix hors taxe : "))
taux_tva = float(input("Entrez le taux de TVA en pourcentage : "))

tva, prix_ttc = calculer_tva_et_prix_ttc(prix_ht, taux_tva)

print(f"Montant de la TVA : {tva:.2f} €")
print(f"Prix TTC : {prix_ttc:.2f} €")
