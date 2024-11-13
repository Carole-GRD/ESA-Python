from fpdf import FPDF
from unidecode import unidecode

pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", "", 12)

# Remplacer les caractères spéciaux avec leur version ASCII
texte = unidecode("""
Objectifs
- Décrire le rôle des protocoles de routage dynamique et leur place dans la conception moderne des réseaux.
- Identifier plusieurs façons de classer les protocoles de routage.
- Expliquer comment les métriques sont utilisées par les protocoles de routage et identifier les types de métriques employés par les protocoles de routage dynamique.
- Déterminer la distance administrative d'une route et décrire son importance dans le processus de routage.
- Identifier les différents éléments de la table de routage.

Protocoles de Routage Dynamique
Fonctions des Protocoles de Routage Dynamique :
- Partager dynamiquement les informations entre les routeurs.
- Mettre à jour automatiquement la table de routage lors de changements de la topologie.
- Déterminer le meilleur chemin vers une destination.

Composants d’un protocole de routage
- Algorithme : Les algorithmes sont utilisés pour faciliter l'information de routage et la détermination du meilleur chemin.
- Messages du protocole de routage : Ces messages servent à découvrir les voisins et à échanger des informations de routage.

Protocoles de Routage Statique
- Avantages du routage statique :
  - Facile à configurer
  - Ne nécessite pas de ressources supplémentaires
  - Plus sécurisé

- Inconvénients du routage statique :
  - Les changements du réseau nécessitent une reconfiguration manuelle
  - Ne s’adapte pas bien aux grandes topologies

Classification des Protocoles de Routage
- Les protocoles de routage dynamique sont regroupés selon leurs caractéristiques. Exemples : RIP, IGRP, EIGRP, OSPF, IS-IS, BGP.
- Un Système Autonome est un groupe de routeurs sous le contrôle d'une seule autorité.

Types de Protocoles de Routage :
- Protocoles de Passerelle Intérieure (IGP) : Utilisés pour le routage à l'intérieur d'un système autonome.
  - Exemples : RIP, EIGRP, OSPF.
- Protocoles de Passerelle Extérieure (EGP) : Utilisés pour le routage entre systèmes autonomes.
  - Exemple : BGPv4.

Comparaison des Protocoles de Routage à Vecteur de Distance et à État de Lien
- Vecteur de distance :
  - Les routes sont annoncées comme des vecteurs de distance et de direction, avec une vue incomplète de la topologie du réseau, généralement avec des mises à jour périodiques.
- État de lien :
  - Fournit une vue complète de la topologie du réseau, avec des mises à jour non périodiques.

Protocoles Classful et Classless
- Classful : N’envoie pas le masque de sous-réseau dans les mises à jour de routage.
- Classless : Envoie le masque de sous-réseau dans les mises à jour de routage.

Convergence
La convergence est atteinte lorsque toutes les tables de routage des routeurs sont cohérentes.

Métriques des Protocoles de Routage
- Métrique : Une valeur utilisée pour déterminer quelles routes sont préférables.
- Métriques utilisées : Bande passante, Coût, Délai, Nombre de sauts, Charge, Fiabilité.
- Champ de métrique dans la Table de Routage : Utilisation de métriques spécifiques pour chaque protocole, par exemple :
  - RIP : Nombre de sauts
  - IGRP & EIGRP : Bande passante (par défaut), Délai (par défaut), Charge, Fiabilité
  - IS-IS & OSPF : Coût, Bande passante (implémentation Cisco)

Équilibrage de Charge
Capacité d’un routeur à distribuer les paquets parmi plusieurs chemins de coût égal.

Distance Administrative d’une Route
- But d'une métrique : Une valeur calculée pour déterminer le meilleur chemin.
- But de la Distance Administrative : Une valeur numérique qui spécifie la préférence pour une route particulière.
- Les routes directement connectées ont une Distance Administrative par défaut de 0.
- Les routes statiques ont une Distance Administrative par défaut de 1.
""")

pdf.multi_cell(0, 10, texte)

output_path = "C:\\Users\\gerar\\OneDrive\\2022 Documents\\ESA\\Premiere\\Base-reseaux\\Cours-ESA\\Protocoles_de_routage_francais.pdf"
pdf.output(output_path)
