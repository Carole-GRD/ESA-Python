"""
Jeu de combat dans lequel un personnage affronte des boss de niveaux croissants.

Le programme permet de :
    - Créer un ou plusieurs personnages avec des caractéristiques variées.
    - Générer des boss aux points de vie croissants.
    - Simuler des combats jusqu'à la victoire ou la défaite.

Le joueur peut progresser à travers plusieurs niveaux en battant les boss successifs.

Date : 10-02-2025
Auteurs : Gwenaël, Hyacinthe, Alfred, Edith, Franck, Boris, Carole, Christian
"""
import random


def creer_personnage():
    """
        Crée un personnage en demandant à l'utilisateur de saisir son nom, son genre, sa race
        et attribue une classe aléatoirement.

        :return:
            (dict) Un dictionnaire contenant les informations du personnage :
                - 'nom' (str) : Nom du personnage
                - 'genre' (str) : 'masculin' ou 'féminin'
                - 'race' (str) : Une des races disponibles ('Humain', 'Elfe', 'Nain', 'Gnome')
                - 'classe' (str) : Une des classes attribuées aléatoirement ('Magicien', 'Voleur', 'Prêtre', 'Guerrier')
                - 'dv' (int) : Dés de vie correspondant à la classe (4, 6, 8 ou 10)
        """

    nom = input('Nom du personnage : ')

    genre = input('Genre du personnage f/m : ')
    while genre != 'f' and genre != 'm':
        print('ERREUR: entrer "m" ou "f" !')
        genre = input('Genre du personnage f/m : ')
    genre = 'masculin' if genre == 'm' else 'féminin'

    races = {'1': 'Humain', '2': 'Elfe', '3': 'Nain', '4': 'Gnome'}
    race_choix = input('Race du personnage (1: Humain, 2 : Elfe, 3: Nain, 4: Gnome) : ')
    while race_choix not in ['1', '2', '3', '4']:
        print('ERREUR: choisissez 1, 2, 3 ou 4 !')
        race_choix = input('Race du personnage (1: Humain, 2 : Elfe, 3: Nain, 4: Gnome) : ')
    race = races[race_choix]

    classes = {1: 'Magicien', 2: 'Voleur', 3: 'Prêtre', 4: 'Guerrier'}
    dv = {'Magicien': 4, 'Voleur': 6, 'Prêtre': 8, 'Guerrier': 10}
    num_classe = random.randint(1, 4)
    classe = classes[num_classe]

    personnage = {
        'nom': nom,
        'genre': genre,
        'race': race,
        'classe': classe,
        'dv': dv[classe]
    }

    return personnage


def creer_boss(niveau):
    """
    Génère un boss en fonction du niveau donné.

    :param niveau: (int) Niveau du jeu (entre 1 et 5).

    :return:
        (dict) Un dictionnaire contenant les informations du boss :
            - 'nom' (str) : Nom du boss en fonction de son niveau.
            - 'pdv' (int) : Points de vie du boss selon son niveau.
    """

    nom = {
        1: 'Malakar',
        2: 'Déméthius',
        3: 'Vortex 9',
        4: 'Dr. Vexenstein',
        5: 'Azael\'Xoth, [L\'ombre-éternelle]'
    }

    dv = {
        1: 1,
        2: 20,
        3: 40,
        4: 70,
        5: 200
    }

    boss = {
        'nom': nom[niveau],
        'pdv': dv[niveau]
    }
    return boss


def lancer_combat(personnage, niveau=1):
    """
    Lance un combat entre un personnage et un boss du niveau donné.

    :param personnage: (dict) Dictionnaire contenant les informations du personnage combattant.
    :param niveau: (int) Niveau du combat (par défaut : 1).

    :return: (bool) True si le personnage gagne le combat, False sinon.
    """

    boss = creer_boss(niveau)
    pdv_personnage = personnage['dv'] * niveau

    avatar_personnage = '👨‍🦱' if personnage['genre'] == 'masculin' else '👩‍🦰'
    avatar_boss = ''
    if boss['nom'] == 'Malakar':
        avatar_boss = '🤖'
    elif boss['nom'] == 'Déméthius':
        avatar_boss = '👾'
    elif boss['nom'] == 'Vortex 9':
        avatar_boss = '🧌'
    elif boss['nom'] == 'Dr. Vexenstein':
        avatar_boss = '👻'
    elif boss['nom'] == 'Azael\'Xoth, [L\'ombre-éternelle]':
        avatar_boss = '👺'

    joueur = False
    while boss['pdv'] > 0 and pdv_personnage > 0:
        joueur = not joueur
        defense = random.randint(0, niveau * 3)

        if joueur:
            attaque = random.randint(niveau * 1, niveau * 5)
            if attaque > defense:
                point_perdu = attaque - defense
                print(f"\n{avatar_personnage} {personnage['nom']} attaque de {attaque}")
                print(f"{avatar_boss} {boss['nom']}  perd : {point_perdu} points de vie,"
                      f" il lui reste {boss['pdv'] - point_perdu}")
                boss['pdv'] = boss['pdv'] - point_perdu
            else:
                print('\nLa défense du boss est trop forte')
        else:
            attaque = random.randint(niveau * 1, niveau * 3)
            if attaque > defense:
                point_perdu = attaque - defense
                print(f"{avatar_boss} {boss['nom']} attaque de {attaque}")
                print(f"{avatar_personnage} {personnage['nom']}  perd : {point_perdu} points de vie, "
                      f"il lui reste {pdv_personnage - point_perdu}")
                pdv_personnage = pdv_personnage - point_perdu
            else:
                print('La défense du joueur est trop forte')

    if boss['pdv'] <= 0:
        print('Tu as gagné !')
        return True
    elif pdv_personnage <= 0:
        print('Tu as perdu !')
        return False


choix_menu = ''
personnage_2 = ""
while choix_menu != 'q':
    print("-------bienvenu sur la jeu \"baldur's gate 4\"-------")
    print('Pour quitter le jeu tape (q)')
    personnage_1 = creer_personnage()
    personnage_principal = personnage_1
    print("Votre personnage est :", personnage_1)

    while personnage_2 == "":
        choix_creation = int(input("Pour créer un deuxième personnage tape (1) -- sinon tape (2) "))
        if choix_creation == 1:
            personnage_2 = creer_personnage()
            print("Votre personnage est :", personnage_2)
        if choix_creation == 2:
            break

    if personnage_2 != "":
        choix_personnage = int(input(f"Choisis ton personnage : {personnage_1['nom'].upper()} (1) "
                                     f"ou  {personnage_2['nom'].upper()} (2) : "))
        if choix_personnage == 2:
            personnage_principal = personnage_2

    choix_menu = input(f'Voulez-vous combattre avec {personnage_principal['nom']} (c) ou quitter (q) : ')
    choix_combat = ''
    niveau = 1

    if choix_menu == 'c':
        while choix_combat != 'q' and niveau <= 5:
            print(f"\nNiveau : {niveau}")
            resultat = lancer_combat(personnage_principal, niveau)
            if resultat:
                niveau += 1
                print(f'Bravo tu as atteint le niveau {niveau} !')
                choix_combat = input(f'Pour continuer (c) ou quitter (q) : ')
            else:
                break
