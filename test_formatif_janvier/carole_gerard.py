"""
Script Python pour inverser les paires de caractères dans un mot.

Ce script contient une fonction principale, `reorder_word`, qui permet de réorganiser
les caractères des mots en inversant chaque paire de caractères consécutifs.
Il gère également les cas où la longueur du mot est impaire, en conservant le dernier
caractère intact.

Le script fonctionne en deux étapes principales :
    1. Lecture d'un mot saisi par l'utilisateur.
    2. Utilisation de la fonction `reorder_word` pour réorganiser les caractères du mot.

Exemples d'utilisation :
    Entrée : "amgnre" -> Sortie : "manger"
    Entrée : "vaior" -> Sortie : "avoir"

Auteurs : Carole Gérard
Date : 20-01-2025
"""


def reorder_word(word):
    """
    Réorganise les caractères d'un mot en inversant chaque paire de caractères consécutifs.
    Si le mot a une longueur impaire, le dernier caractère reste inchangé.

    :param word: (str) Le mot dont les caractères doivent être réorganisés.
    :return: (str) Le mot avec les caractères correctement réorganisés.
    """
    if not word:
        return ''

    reordered = ''

    # Parcourt les caractères par paires, en évitant les dépassements d'indice.
    for i in range(0, len(word) - 1, 2):
        reordered += word[i + 1] + word[i]  # Inverse la paire

    # Gère le dernier caractère pour les mots impairs
    if len(word) % 2 != 0:
        reordered += word[-1]

    return reordered


input_word = input('Entrez un mot : ')
reordered = reorder_word(input_word)
print(f"Le mot réorganisé est : {reordered}")


"""

    Amélioration possible :
    ----------------------
    
    La partie de code...
    
        reordered = ''
        for i in range(0, len(word) - 1, 2):
            reordered += word[i + 1] + word[i]  # Inverse la paire

    Peut être remplacée par...
    
        1. Méthode avec join et compréhension de liste/générateur (la plus optimale) :
        ------------------------------------------------------------------------------
        
        reordered = ''.join(word[i+1] + word[i] for i in range(0, len(word) - 1, 2))
        
    
        2. Méthode avec une liste temporaire et join (alternative légèrement plus verbale) :
        ------------------------------------------------------------------------------------
        
        pairs = [word[i + 1] + word[i] for i in range(0, len(word) - 1, 2)]
        reordered = ''.join(pairs)
        
        
    Comparaison des performances (en pratique) :
    --------------------------------------------
    
    Pour des mots courts (par exemple, moins de 100 caractères), l
    a différence de performance entre les deux approches est négligeable. Cependant :
    
        - Avec des mots longs, la version avec join est bien plus performante 
          car elle évite la surcharge liée aux multiples concaténations.
          
        - Mesure indicative :
            Pour un mot de 1 000 000 de caractères :
                -> La version avec join s’exécute en une fraction de seconde.
                -> La version avec += peut prendre plusieurs secondes, 
                   en raison des nombreuses copies et allocations de mémoire.


    Conclusion :
    ------------
    
    - La version avec join est plus performante et plus adaptée à des chaînes longues.
    
    - La version avec la boucle for et += est acceptable pour des chaînes courtes 
      et peut être plus simple à comprendre pour un débutant.
 
"""
