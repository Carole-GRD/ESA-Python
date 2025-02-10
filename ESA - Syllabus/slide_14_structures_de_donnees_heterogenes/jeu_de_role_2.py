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

    while (genre := input('Genre du personnage f/m : ')) not in ['f', 'm']:
        print('ERREUR: entrer "m" ou "f" !')
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

    boss_data = {
        1: ('Malakar', 1),
        2: ('Déméthius', 20),
        3: ('Vortex 9', 40),
        4: ('Dr. Vexenstein', 70),
        5: ('Azael\'Xoth, [L\'ombre-éternelle]', 200)
    }

    nom, dv = boss_data[niveau]

    boss = {
        'nom': nom,
        'pdv': dv
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
    print(f'{personnage['nom']} : {pdv_personnage} pdv - {boss['nom']} : {boss['pdv']} pdv')

    avatar_personnage = '👨‍🦱' if personnage['genre'] == 'masculin' else '👩‍🦰'
    avatars_boss = {
        'Malakar': '🤖',
        'Déméthius': '👾',
        'Vortex 9': '🧌',
        'Dr. Vexenstein': '👻',
        'Azael\'Xoth, [L\'ombre-éternelle]': '👺'
    }
    avatar_boss = avatars_boss.get(boss['nom'], '👹')

    joueur = False
    while boss['pdv'] > 0 and pdv_personnage > 0:
        joueur = not joueur
        defense = random.randint(0, niveau * 3)

        attaque = random.randint(niveau * 1, niveau * (5 if joueur else 3))

        # Ajout d'un coup critique avec 10% de chance
        if random.random() < 0.1:
            attaque *= 2
            print(f'\n💥 COUP CRITIQUE ! {attaque} dégâts infligés !')

        if attaque > defense:
            point_perdu = attaque - defense
            if joueur:
                boss['pdv'] -= point_perdu
                print(f'\n{avatar_personnage} {personnage['nom']} attaque de {attaque}')
                print(f'{avatar_boss} {boss['nom']}  perd : {point_perdu} points de vie,'
                      f' il lui reste {boss['pdv']}')
            else:
                pdv_personnage -= point_perdu
                print(f'\n{avatar_boss} {boss['nom']} attaque de {attaque}')
                print(f'{avatar_personnage} {personnage['nom']}  perd : {point_perdu} points de vie,'
                      f' il lui reste {pdv_personnage}')
        else:
            print(f'\n🛡️ La défense de {personnage['nom'] if joueur else boss['nom']} est trop forte !')

    if boss['pdv'] <= 0:
        print(f'{avatar_personnage} {personnage['nom']} a gagné ! 🎉')
        return True
    elif pdv_personnage <= 0:
        print(f'{avatar_personnage} {personnage['nom']}  a perdu ! 😢')
        return False


def afficher_personnage(personnage):
    """
    Affiche les détails d'un personnage de manière formatée.
    # TODO :
    :param personnage:
    :return: /
    """
    print(f"--- Détails du personnage ---\n"
          f"Nom      : {personnage['nom']}\n"
          f"Genre    : {personnage['genre']}\n"
          f"Race     : {personnage['race']}\n"
          f"Classe   : {personnage['classe']}\n"
          f"Dés de vie : {personnage['dv']}\n")


choix_menu = ''
choix_combat = ''
personnage_2 = ""
premiere_partie = True
rejouer = ''
while choix_menu != 'q':
    if not premiere_partie and choix_combat != 'q':
        rejouer = input('Rejouer (r) - Quitter (q) : ')
    else:
        premiere_partie = False
    if rejouer == 'q':
        choix_menu = 'q'
        print('A bientôt 👋')
        break
    else:
        rejouer = ''
        choix_combat = ''

    print('\n------- Bienvenu sur la jeu "baldur\'s gate 4" -------\n')
    personnage_1 = creer_personnage()
    personnage_principal = personnage_1
    afficher_personnage(personnage_1)

    while personnage_2 == '':
        choix_creation = input('Créer un deuxième personnage ? o/n :  ')
        if choix_creation == 'o':
            personnage_2 = creer_personnage()
            afficher_personnage(personnage_2)
        if choix_creation == 'n':
            break

    if personnage_2 != '':
        choix_personnage = int(input(f'Choisis ton personnage : {personnage_1['nom'].upper()} (1) '
                                     f'ou  {personnage_2['nom'].upper()} (2) : '))
        if choix_personnage == 2:
            personnage_principal = personnage_2

    choix_menu = input(f'Voulez-vous combattre avec {personnage_principal['nom']} (c) ou quitter (q) : ')
    if choix_menu == 'q':
        print('A bientôt 👋')

    niveau = 1

    if choix_menu == 'c':
        while choix_combat != 'q' and niveau <= 5:
            print(f'\nNiveau : {niveau}')
            resultat = lancer_combat(personnage_principal, niveau)
            if resultat:
                niveau += 1
                print(f'Bravo tu as atteint le niveau {niveau} !')
                choix_combat = input(f'Pour continuer (c) ou choisir un autre personnage (q) : ')
            else:
                break
