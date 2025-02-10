"""
    Exercice 1 :

    Écrire un programme permettant de ranger dans une liste des éléments représentant des étudiants
    qui seront représentés par le dictionnaire “dico_etudiant” (à vous de définir les champs utiles).
    Le programme devra permettre de rajouter/supprimer/afficher des étudiants. Ainsi que de modifier la
    structure du dictionnaire (supprimer/ajouter des clés).
"""

from datetime import date


# ==============================================================================================
# ===================================  Liste des étudiants  ===================================
# ==============================================================================================

liste_etudiants = [
    {
        "id": "ETU001",
        "nom": "Lamy",
        "prenom": "Alexandra",
        "date_de_naissance": date(1980, 5, 26),
        "email": "alex@test.be",
        "telephone": "+32 478 12 34 56",
        "cursus": "Informatique",
        "niveau": "Licence 2",
        "moyenne": 14.8,
        "notes": [15, 14, 16, 14.5]
    },
    {
        "id": "ETU002",
        "nom": "Martin",
        "prenom": "Lucas",
        "date_de_naissance": date(1999, 11, 3),
        "email": "lucas@test.be",
        "telephone": "+32 465 78 90 12",
        "cursus": "Mathématiques",
        "niveau": "Master 1",
        "moyenne": 16.2,
        "notes": [17, 15, 16, 16.5]
    }
]

# Affichage formaté de la date
# print(dico_etudiant["date_de_naissance"].strftime("%d/%m/%Y"))  # 26/05/1980
# print(dico_etudiant["date_de_naissance"].strftime("%d-%m-%Y"))  # 26-05-1980


# ==============================================================================================
# ==================================  Afficher les étudiants  ==================================
# ==============================================================================================

for i, etudiant in enumerate(liste_etudiants):
    print(f"\nEtudiant {i + 1}")
    print("----------")
    for j, value in etudiant.items():
        print(f"{j}: {value}")


# ==============================================================================================
# ===================================  Ajouter un étudiant  ===================================
# ==============================================================================================

nouvel_etudiant = {
    "id": "ETU003",
    "nom": "Dupont",
    "prenom": "Sophie",
    "date_de_naissance": date(2001, 7, 15),
    "email": "sophie@test.be",
    "telephone": "+32 499 55 44 33",
    "cursus": "Physique",
    "niveau": "Licence 1",
    "moyenne": 13.5,
    "notes": [14, 12, 13, 15]
}

liste_etudiants.append(nouvel_etudiant)


# for i, etudiant in enumerate(liste_etudiants):
#     print(f"\nEtudiant {i + 1}")
#     print("----------")
#     for k, value in etudiant.items():
#         print(f"{k}: {value}")


# ==============================================================================================
# ===============================  Supprimer un étudiant par ID  ===============================
# ==============================================================================================

id_a_supprimer = "ETU002"
liste_etudiants = [etu for etu in liste_etudiants if etu["id"] != id_a_supprimer]


# for i, etudiant in enumerate(liste_etudiants):
#     print(f"\nEtudiant {i + 1}")
#     print("----------")
#     for k, value in etudiant.items():
#         print(f"{k}: {value}")


# ==============================================================================================
# =======================  Ajouter une clé dans tous les dictionnaires  ========================
# ==============================================================================================

for etudiant in liste_etudiants:
    etudiant["adresse"] = "Non renseignée"  # Nouvelle clé avec une valeur par défaut

# for i, etudiant in enumerate(liste_etudiants):
#     print(f"\nEtudiant {i + 1}")
#     print("----------")
#     for k, value in etudiant.items():
#         print(f"{k}: {value}")


# ==============================================================================================
# ======================  Supprimer une clé dans tous les dictionnaires  =======================
# ==============================================================================================

for etudiant in liste_etudiants:
    etudiant.pop("telephone", None)

# ou bien...
for etudiant in liste_etudiants:
    if 'telephone' in etudiant:
        del etudiant['telephone']

"""
    - Si tu n'as pas besoin de vérifier si la clé existe, 
      et que tu préfères une solution simple et sécurisée, 
      pop() est préférable.
      
    - Si tu veux un contrôle plus précis sur la présence de la clé, 
      ou si tu as besoin de réaliser des actions supplémentaires 
      (comme des logs ou des traitements spécifiques si la clé n'existe pas), 
      alors la méthode avec if et del est mieux.
"""

# for i, etudiant in enumerate(liste_etudiants):
#     print(f"\nEtudiant {i + 1}")
#     print("----------")
#     for k, value in etudiant.items():
#         print(f"{k}: {value}")


# ==============================================================================================
# ==============================  Amélioration de l'affichage  =================================
# ==============================================================================================

# Fonction pour formater les clés
def format_key(key):
    """
    Formate la clé en une version plus lisible pour l'affichage.

    :param key: (str) La clé à formater.
    :return: (str) La clé formatée pour l'affichage.
    """
    key_mapping = {
        "id": "ID",
        "nom": "Nom",
        "prenom": "Prénom",
        "date_de_naissance": "Date de naissance",
        "email": "Email",
        "telephone": "Téléphone",
        "cursus": "Cursus",
        "niveau": "Niveau",
        "moyenne": "Moyenne",
        "notes": "Notes"
    }
    return key_mapping.get(key, key)


# Affichage des étudiants avec les améliorations
for i, etudiant in enumerate(liste_etudiants):
    print(f"\nEtudiant {i + 1}")
    print("----------")
    for k, value in etudiant.items():
        if isinstance(value, date):  # Si la valeur est une date
            print(f"{format_key(k)}: {value.strftime('%d/%m/%Y')}")
        else:
            print(f"{format_key(k)}: {value}")


"""
    Explications des deux "key" dans :   key_mapping.get(key, key)
    --------------------------------------------------------------
        - Premier key : 
            La clé recherchée dans key_mapping.
        
        - Second key : 
            La valeur de retour par défaut, c'est-à-dire la clé elle-même, 
            si elle n'est pas trouvée dans le dictionnaire.


    Dans mon cas :
    --------------
        - La clé "nom" existe dans key_mapping, on retourne "Nom".
        
        - La clé "adresse" n'existe pas, on retourne simplement la clé "adresse".
"""