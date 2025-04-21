"""
     Module "utils" : gère les données
"""
from datetime import datetime
import os


def open_file(file_name):
    """
    :param file_name: le nom du fichier contenant les animaux du zoo
    :return: les données lues à partir du fichier existant (le créer si inexistant)
    """
    if not os.path.isfile(file_name):
        file = open(file_name, "w", encoding="utf-8")
        file.close()

    with open(file_name, "r", encoding="utf-8") as file:
        animaux = []
        lignes = file.readlines()
        for ligne in lignes:
            elements = ligne[:-2].split('|')
            animal = {
                "nom": elements[0],
                "espece": elements[1],
                "origine": elements[2],
                "date_de_naissance": elements[3],
                "caracteristiques": elements[4],
                "taille": elements[5],
                "poids": elements[6],
                "date_d_ajout": elements[7],
            }
            animaux.append(animal)
        return animaux


def creer_animal():
    """
    :return: (dict) un dictionnaire contenant les informations de l'animal créé
    """
    nom = input("Nom : ")
    espece = input("Espèce : ")
    origine = input("Origine : ")
    date_de_naissance = input("Date de naissance (format dd/mm/yyyy) : ")
    caracteristiques = input("Caractéristiques (séparés par une virgule) : ")
    taille = float(input("Taille (en mètre) : "))
    poids = float(input("Poids (en kg) : "))
    date_d_ajout = datetime.now().strftime("%d/%m/%Y")

    animal = {
        "nom": nom,
        "espece": espece,
        "origine": origine,
        "date_de_naissance": date_de_naissance,
        "caracteristiques": caracteristiques,
        "taille": taille,
        "poids": poids,
        "date_d_ajout": date_d_ajout
    }
    return animal


def ajouter_animal(animaux):
    """
    :param animaux: la liste des animaux
    :return: la liste des animaux mise à jour (avec le nouvel animal)
    """
    animal = creer_animal()
    animaux.append(animal)
    return animaux


def modifier_animal(animaux, nom):
    """
    :param animaux: (list) la liste des animaux
    :param nom: (str) le nom de l'animal à modifier
    :return: (list) la liste des animaux mise à jour
    """
    animal_a_modifier = {}
    cles = []
    for animal in animaux:
        if animal['nom'] == nom:
            animal_a_modifier = animal
            cles = animal.keys()
            break

    while True:
        cle = input(f'\nQue souhaitez-vous modifier ({', '.join(cles)}) ? ')
        valeur = input(f"{cle} : ")
        animal_a_modifier[cle] = valeur
        continuer = input('Modifier une autre valeur (o/n) ? ')
        if continuer == 'n':
            break

    return animaux


def supprimer_animal(animaux, nom):
    """
    :param animaux: (list) la liste des animaux
    :param nom: (str) le nom de l'animal à supprimer
    :return: (list) la liste des animaux mise à jour
    """
    for animal in animaux:
        if animal['nom'] == nom:
            animaux.remove(animal)
            break
    return animaux


def sauvegarder_animaux(animaux, file_name):
    """
    :param animaux: (list) la liste des animaux
    :param file_name: (str) le chemin vers le fichier
    :return: rien, permet d'écrire les données dans le fichier
    """
    with open(file_name, "w", encoding="utf-8") as file:
        lignes = []

        for animal in animaux:
            donnes = ''
            for value in animal.values():
                donnes += str(value) + "|"
            donnes += ("\n")
            lignes.append(donnes)

        file.writelines(lignes)


def calculer_age(date_naissance):
    """
    :param date_naissance: (str) la date de naissance
    :return: (int) l'âge
    """
    date_naissance = datetime.strptime(date_naissance, "%d/%m/%Y")
    today = datetime.today()
    return today.year - date_naissance.year - ((today.month, today.day) < (date_naissance.month, date_naissance.day))


"""
    Explication pour le calcul de l'âge
    -----------------------------------
    
        today.year - date_naissance.year - ((today.month, today.day) < (date_naissance.month, date_naissance.day))
    
    Cette ligne calcule l'âge d'une personne en soustrayant l'année de naissance de l'année actuelle. 
    
    Ensuite, elle vérifie si l'anniversaire de la personne a eu lieu cette année 
    en comparant le mois et le jour actuels avec ceux de la naissance. 
    
    La comparaison renvoie un booléen :
        - True (équivalent à 1) si l'anniversaire n'est pas encore passé, donc on soustrait 1 an.
        - False (équivalent à 0) si l'anniversaire est déjà passé ou est le jour-même, donc aucun ajustement.
"""