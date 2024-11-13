from fpdf import FPDF
from unidecode import unidecode

# Créer un objet PDF avec orientation paysage
pdf = FPDF(orientation='L', unit='mm', format='A4')
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

pdf.ln(10)
# Définir la police pour le titre (plus grand et en gras)
pdf.set_font("Helvetica", 'B', 24)
pdf.cell(297, 10, txt="Objectif", new_x='LMARGIN', new_y='NEXT', align='C')

# Ajouter un saut de ligne pour espacement
pdf.ln(10)

# Contenu du premier objectif (plus grand et plus espacé)
pdf.set_font("Helvetica", '', 18)
texte_1 = unidecode("""
- Décrire le rôle des protocoles de routage dynamique et leur place dans la conception moderne des réseaux.
- Identifier plusieurs façons de classer les protocoles de routage.
- Expliquer comment les métriques sont utilisées par les protocoles de routage et identifier les types de métriques employés par les protocoles de routage dynamique.
- Déterminer la distance administrative d'une route et décrire son importance dans le processus de routage.
- Identifier les différents éléments de la table de routage.
""")
pdf.multi_cell(0, 12, texte_1)

# Ajouter une nouvelle page pour simuler une nouvelle diapo
pdf.add_page()

pdf.ln(10)
pdf.set_font("Helvetica", 'B', 24)
pdf.cell(297, 10, txt="Protocoles de Routage Dynamique", new_x='LMARGIN', new_y='NEXT', align='C')

pdf.ln(10)  # Saut de ligne
pdf.set_font("Helvetica", 'B', 20)
pdf.cell(297, 5, txt="Fonctions des Protocoles de Routage Dynamique", new_x='LMARGIN', new_y='NEXT', align='C')

# pdf.ln(5)  # Saut de ligne
pdf.set_font("Helvetica", '', 18)
texte_2 = unidecode("""
- Partager dynamiquement les informations entre les routeurs.
- Mettre à jour automatiquement la table de routage lors de changements de la topologie.
- Déterminer le meilleur chemin vers une destination.
""")
pdf.multi_cell(0, 12, texte_2)

# pdf.ln(5)  # Saut de ligne
pdf.set_font("Helvetica", 'B', 20)
pdf.cell(297, 5, txt="Composants d'un protocole de routage", new_x='LMARGIN', new_y='NEXT', align='C')

# pdf.ln(5)  # Saut de ligne
pdf.set_font("Helvetica", '', 18)
texte_3 = unidecode("""
- Algorithme : Les algorithmes sont utilisés pour faciliter l'information de routage et la détermination du meilleur chemin.
- Messages du protocole de routage : Ces messages servent à découvrir les voisins et à échanger des informations de routage.
""")
pdf.multi_cell(0, 12, texte_3)

# Ajouter une autre diapo/page
pdf.add_page()

# Titre de la troisième diapo (plus grand et centré)
pdf.set_font("Helvetica", 'B', 24)
pdf.cell(297, 10, txt="Métriques Utilisées", new_x='LMARGIN', new_y='NEXT', align='C')

# Contenu de la troisième diapo (plus grand et plus espacé)
pdf.ln(20)  # Saut de ligne
pdf.set_font("Helvetica", '', 18)
texte_4 = unidecode("""
Les métriques de routage sont des valeurs utilisées pour évaluer la qualité des différentes routes. 
Elles peuvent être basées sur divers critères comme :
- Le nombre de sauts (hops)
- La bande passante
- La latence
- La charge du réseau
""")
pdf.multi_cell(0, 12, texte_4)

# Enregistrer le PDF
output_path = "C:\\Users\\gerar\\OneDrive\\2022 Documents\\ESA\\Premiere\\Base-reseaux\\Cours-ESA\\Routage_Dynamique.pdf"

pdf.output(output_path)

print(f"PDF créé avec succès : {output_path}")
