"""
    Exercice 3 :

    Écrire un programme permettant de spécifier si l’étudiant à réussi ou pas et avec quelle mention :

    (la cote devra être comprise entre 0 et 20 et retourner une erreur si c'est pas le cas)

        ● 0 à 9 : échec ;
        ● 10 à 11 : réussite sans mention ;
        ● 12 à 13 : réussis avec satisfaction ;
        ● 14 à 15 : réussis avec distinction ;
        ● 16 à 17 : réussis avec grande distinction ;
        ● 18 à 20 : réussis avec la plus grande distinction.


    En cas de point avec décimal, faite l’arrondi comme vu au cours.
"""

# # Encodage de la cote par l'utilisateur
# cote = round(float(input("Entrez une cote comprise entre 0 et 20 : ")))
#
# # Vérification de la cote et affichage du résultat
# if cote < 0 or cote > 20:
#     print("La côte introduite est mauvaise (%s)" % cote)
# elif cote < 10:
#     print("échec (%s)" % cote)
# elif cote < 12:
#     print("réussite sans mention (%s)" % cote)
# elif cote < 14:
#     print("réussis avec satisfaction (%s)" % cote)
# elif cote < 16:
#     print("réussis avec distinction (%s)" % cote)
# elif cote < 18:
#     print("réussis avec grande distinction (%s)" % cote)
# else:
#     print("réussis avec la plus grande distinction (%s)" % cote)


"""
    Reprenez l'exercice précédent et transformez-le en utilisant le match … case
"""

try:
    # Encodage de la cote par l'utilisateur
    cote = round(float(input("Entrez une cote comprise entre 0 et 20 : ")))

    # Vérification de l'intervalle
    if cote < 0 or cote > 20:
        print("Erreur : La cote doit être comprise entre 0 et 20.")
    else:
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
except ValueError:
    print("Erreur : Veuillez entrer un nombre valide.")

