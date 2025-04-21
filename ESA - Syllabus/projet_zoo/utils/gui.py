"""
    Module "gui" : gère l'interface
"""
from .utils import calculer_age


def menu():
    """
    :return: -1 si le choix est problématique sinon le choix de l'utilisateur
    """
    print("\nQue voulez-vous faire ? ")
    try:
        while True:
            choix = int(input("1 Créer, 2 Modifier, 3 Supprimer, 4 Sauvegarder, 5 Afficher, 6 Quitter : "))
            if choix < 1 or choix > 6:
                print("ERREUR : Entrer un nombre entre 1 et 6 !")
                continue
            break
    except ValueError:
        print("ERREUR : Entrer un nombre !")
        return -1
    return choix


def afficher_animaux(animaux):
    """
    :param animaux: la liste des animaux
    :return: rien, permet d'afficher les données
    """
    # Affichage de l'en-tête
    print(f"\n{'Nom':<15}| {'Espèce':<15}| {'Origine':<18}| {'Age':<8}| {'Caractéristiques':<30}"
          f"| {'Taille (en m)':<15}"
          f"| {'Poids (en kg)':<15}"
          f"| {'Date d\'ajout':<15}")
    # Ligne de séparation
    print("=" * 150)

    # Affichage des animaux
    for animal in animaux:
        print(
            f"{animal['nom']:<15}| {animal['espece']:<15}| {animal['origine']:<18}"
            f"| {calculer_age(animal['date_de_naissance']):<8}"
            f"| {animal['caracteristiques']:<30}| {animal['taille']:<15}"
            f"| {animal['poids']:<15}| {animal['date_d_ajout']:<15}")
