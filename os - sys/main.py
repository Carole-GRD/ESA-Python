# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# print("===============")
# import file_4
# print("===============")
from file_4 import print_file_4


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(f"main.py -> __name__ : {__name__}")  # __name__ : __main__
    print_hi('PyCharm')

    print_file_4()
    '''
        « __name__ » est une variable spéciale gérée par Python et qui prend 
        automatiquement la valeur de “__main__” si le script est exécuté directement 
        et le nom du module, c'est-à-dire son nom de fichier, s'il est simplement 
        exécuté automatiquement dans le cadre d'une déclaration d'importation.
    '''



# See PyCharm help at https://www.jetbrains.com/help/pycharm/




# ====================================
# ====================================
# ====================================

# import os

# Afficher le répertoire de travail actuel
# print("Répertoire courant :", os.getcwd())

# Créer un nouveau répertoire
# os.mkdir('nouveau_dossier')

# Lister les fichiers et dossiers
# print("Contenu du répertoire :", os.listdir('.'))

# Changer de répertoire
# os.chdir('Directory 1')
# print("Nouveau répertoire courant :", os.getcwd())

# Lister les fichiers et dossiers
# print("Contenu du répertoire :", os.listdir('.'))

# Revenir au répertoire parent
# os.chdir('..')
# print("Nouveau répertoire courant :", os.getcwd())

# Supprimer le répertoire créé
# os.rmdir('nouveau_dossier')

# Lister les fichiers et dossiers
# print("Contenu du répertoire :", os.listdir('.'))


# ====================================
# ====================================
# ====================================

# import sys
# print("Version : ", sys.version)
# print("Système : ", sys.platform)
# print("Executable : ", sys.executable)
# print("Modules : ", sys.modules)


