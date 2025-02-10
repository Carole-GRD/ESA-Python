"""
    Un enregistrement (ou article) est une structure hétérogène d’éléments pouvant être de types différents.
    Ces éléments sont appelés champs.
"""

# =====================================================================================
# ================================== Les tulpes =======================================
# =====================================================================================

damier = {}
damier[(1, 0)] = 'noir'
damier[(3, 0)] = 'noir'
damier[0, 7] = 'blanc'

"""
    Vous remarquerez, au passage, que nous pouvons alléger l’écriture en omettant les parenthèses, mais prudence.

    Quand nous utilisons des tuples comme clés, il faut s’assurer d’avoir une valeur à la coordonnée pointée,
    sinon nous aurons une exception de type ?
"""

# Pour éviter ce problème, nous pouvons utiliser la méthode get() :
print(damier.get((3, 3), 'Néant'))  # Donne "Néant"
print(damier.get((1, 0), 'Néant'))  # Donne "Noir"

"""
    La seconde valeur est donc la valeur à retourner au cas où la clé n’est pas existante.
"""


"""
    Nous avons déjà rencontré les listes et les tuples de manière sommaire. 
    Ces types font partie de la famille des séquences et sont donc itérable sur bases d’un indice.
    La définition d’une liste se fait à l’aide de crochet, 
    tandis que la définition d’un tuple se fait à l’aide de parenthèse :
"""

ma_liste = []
mon_tuple = ()
# Nous pouvons utiliser ce que nous avons vu dans le chapitre des “Chaînes de caractères”
# pour la manipulation de ces types.

"""
    Listes :
    -------
        • Mutable (contrairement aux chaînes ;
        • Sont des objets ;
        • On peut utiliser les instructions del et remove ;
        • Slicing (découpage en tranche) :
            ma_liste[2] = 'xxx'      => remplace le second élément par "xxx"
            ma_liste[2:2] = 'xxx'    => insère l'élément "xxx" en troisième position de ma liste
            ma_liste[2:4] = []       => remplace la sous chaîne composé des éléments 2 et 3 par une chaîne vide.
            
    Tulpes :
    --------
        • Immutable (comme les chaînes) ;   -> partage de référence lors d'une copie  (a = b)
        • Sont des objets ;
        • On ne peut pas utiliser les instructions del et remove ;
"""
