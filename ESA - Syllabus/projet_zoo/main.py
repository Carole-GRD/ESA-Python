"""
    Programme principal
"""
from utils.gui import afficher_animaux
from utils.gui import menu

from utils.utils import ajouter_animal
from utils.utils import modifier_animal
from utils.utils import open_file
from utils.utils import sauvegarder_animaux
from utils.utils import supprimer_animal


file_name = "ressources/zoo2025.csv"

animaux = open_file(file_name)

while True:
    choix = -1
    while choix < 0:
        choix = menu()
    match choix:
        case 1:
            ajouter_animal(animaux)
        case 2:
            nom = input("\nQuel est le nom de l'animal à modifier ? ")
            modifier_animal(animaux, nom)
        case 3:
            nom = input("\nQuel est le nom de l'animal à supprimer ? ")
            supprimer_animal(animaux, nom)
        case 4:
            sauvegarder_animaux(animaux, file_name)
        case 5:
            afficher_animaux(animaux)
        case _:
            exit("Bonne journée !")
