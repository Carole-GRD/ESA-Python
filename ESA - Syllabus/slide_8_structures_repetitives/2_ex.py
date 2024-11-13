"""
    Exercice 2 :

    Écrire un programme permettant de spécifier si, pour une côte lue
    (qui devra être comprise entre 0 et 20, répéter la lecture jusqu’à obtention d’une cote adéquate),
    l’étudiant à réussi ou pas et avec uelle mention :
        0 à 9 : échec ;
        10 à 11 : réussite sans mention ;
        12 à 13 : réussis avec satisfaction ;
        14 à 15 : réussis avec distinction ;
        16 à 17 : réussis avec grande distinction ;
        18 à 20 : réussis avec la plus grande distinction.

    En cas de point avec décimal, faite l’arrondi comme vu au cours.
"""


# prompt = Message spécifique pour la demande d'entrée (si premier input ou suite à une erreur)
prompt = "Entrez une cote sur 20 : "

# Encodage de la cote par l'utilisateur
while True:
    cote = input(prompt)
    try:
        # Essayer de convertir en entier (si échoue, une exception est levée -> ValueError)
        cote = float(cote)
        # Vérifier si la cote est dans l'intervalle valide
        if 0 <= cote <= 20:
            cote = round(cote)
            break
        else:
            prompt = "Entrez une cote comprise entre 0 et 20 : "

    except ValueError:
        # Si la conversion échoue, c'est que l'entrée n'est pas un nombre
        prompt = "Entrez un nombre : "

# Utilisation du bloc match pour afficher les messages
match cote:
    case 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9:
        print(f"échec ({cote})")
    case 10 | 11:
        print(f"réussite sans mention ({cote})")
    case 12 | 13:
        print(f"réussis avec satisfaction ({cote})")
    case 14 | 15:
        print(f"réussis avec distinction ({cote})")
    case 16 | 17:
        print(f"réussis avec grande distinction ({cote})")
    case 18 | 19 | 20:
        print(f"réussis avec la plus grande distinction ({cote})")


