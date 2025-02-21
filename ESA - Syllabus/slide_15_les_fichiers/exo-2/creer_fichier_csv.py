"""
    Le script crée un fichier articles.csv contenant les colonnes suivantes :
        ✅ le libellé de l’article
        ✅ le prix (HTVA)
        ✅ la quantité.

    Remarque :
    Tu peux l'ouvrir avec Excel ou un éditeur de texte pour voir le contenu !
"""

import csv

# Nom du fichier CSV
nom_fichier = "articles.csv"

# Données des courses
donnees = [
    ["libellé de l’article", "prix (HTVA)", "quantité"],
    ["Ballon Mikasa", 45.99, 1],
    ["Chaussures Mizuno", 76.75, 1],
    ["Short", 10.00, 2],
    ["T-shirt", 20.14, 3],
    ["Gourde", 7.50, 1]
]

# Écriture du fichier CSV
with open(nom_fichier, "w", newline="", encoding="utf-8") as fichier:
    writer = csv.writer(fichier)
    writer.writerows(donnees)

print(f"Fichier {nom_fichier} créé avec succès !")
