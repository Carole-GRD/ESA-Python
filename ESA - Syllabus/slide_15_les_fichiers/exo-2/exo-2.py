"""
    Exercice 2 :

    Faites un programme permettant de lire un fichier csv contenant 3 “colonnes” :
        ● libellé de l’article
        ● prix (HTVA)
        ● quantité
        ● Calculez le prix total pour chaque article et sauvez le résultat dans un fichier facture.txt
          qui aura la forme suivante :
        ● Pour chaque article : Vous avez commandé “quantité” unité(s) de l’article “Libellé de l’article”
          au prix unitaire de “prix”, ce qui revient à un prix total, pour l’article,
          de “prix_majoré” (la TVA sera de 21 % pour tous les articles).
        ● En dernière ligne, vous indiquerez ceci : Le prix total de la facture s’élève à “montant total”

    RMQ :  fichier csv (excel -> enregistrer sous -> format csv -> séparateur : pipe)
"""

# ==============================================================================================================
# ===========================================  MA VERSION  =====================================================
# ==============================================================================================================

# # ATTENTION : commencer par créer le fichier articles.csv s'il n'existe pas (voir creer_fichier_csv.py)
#
# with open('articles.csv', 'r', encoding="UTF-8") as fichier:
#     articles = fichier.read().split('\n')
# # Le fichier est automatiquement fermé ici, à la fin du bloc `with`
#
#
# facture = open('facture.txt', 'w', encoding="UTF-8")
#
# prix_total = 0
# for i in range(1, len(articles) - 1):
#     article = articles[i].split(',')
#
#     libelle = article[0]
#     prix_unitaire = float(article[1])
#     quantite = article[2]
#     prix_majore = prix_unitaire * float(quantite) * 1.21
#     prix_total += prix_majore
#
#     facture.write(f'Vous avez commandé {quantite} unité(s) de l’article "{libelle}"'
#                   f' au prix unitaire de {"{:.2f}".format(prix_unitaire)}€,'
#                   f' ce qui revient à un prix total, pour l’article,'
#                   f' de {"{:.2f}".format(prix_majore)}€ (TVA de 21%).\n')
#
# facture.write(f"Le prix total de la facture s’élève à {"{:.2f}".format(prix_total)}€.")
#
# facture.close()
#
# print(f"La facture a été créé avec succès !")


# ==============================================================================================================
# ========================================  VERSION AMELIOREE  =================================================
# ==============================================================================================================

# ATTENTION : commencer par créer le fichier articles.csv s'il n'existe pas (voir creer_fichier_csv.py)

import csv

# Constantes
TVA = 0.21  # TVA de 21%

# Ouvrir le fichier CSV en lecture
with open('articles.csv', 'r') as fichier_csv:
    # Créer un lecteur CSV
    lecteur = csv.reader(fichier_csv)
    # Sauter l'en-tête si présent (à adapter selon le fichier)
    next(lecteur, None)

    # Initialiser le montant total
    montant_total = 0

    # Ouvrir le fichier facture.txt en écriture
    with open('facture.txt', 'w', encoding='utf-8') as facture:
        # Traiter chaque ligne du CSV
        for ligne in lecteur:
            # Récupérer les valeurs
            libelle, prix_htva, quantite = ligne
            prix_htva = float(prix_htva)
            quantite = int(quantite)

            # Calculer le prix total pour cet article avec TVA
            prix_total_article_tva = prix_htva * quantite * (1 + TVA)

            # Ajouter au montant total
            montant_total += prix_total_article_tva

            # Écrire la ligne dans le fichier facture
            facture.write(
                f"Vous avez commandé {quantite} unité(s) de l’article \"{libelle}\" "
                f"au prix unitaire de {prix_htva:.2f}€, ce qui revient à un prix total, "
                f"pour l’article, de {prix_total_article_tva:.2f}€.\n"
            )

        # Écrire la ligne finale avec le montant total
        facture.write(f"\nLe prix total de la facture s’élève à {montant_total:.2f}€.")

print("La facture a été générée dans le fichier facture.txt")
