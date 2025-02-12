"""
Jeu de combat dans lequel un personnage affronte des boss de niveaux croissants.

Le programme permet de :
    1. Créer un ou deux personnage(s) avec des caractéristiques variées.
    2. Dans le cas où l'utilisateur aurait créé deux personnages : choisir le personnage qui va combattre le boss.
    3. Générer des boss aux points de vie croissants.
    4. Simuler des combats jusqu'à la victoire ou la défaite.

Le joueur peut progresser à travers plusieurs niveaux en battant les boss successifs.

Date : 10-02-2025
Auteurs : Gwenaël, Hyacinthe, Alfred, Edith, Franck, Boris, Carole, Christian
"""
import random


def creer_personnage():
    """
    Crée un personnage en demandant à l'utilisateur de saisir son nom, son genre, sa race
    et attribue une classe aléatoirement.
    :return: (dict) Un dictionnaire contenant les informations du personnage (nom, genre, race, classe, dv, avatar)
    """

    # Demande le nom du personnage
    nom = input('Nom du personnage : ')

    # Vérifie que le genre est valide (f/m)
    while (genre := input('Genre du personnage f/m : ')) not in ['f', 'm']:
        print('ERREUR: entrer "m" ou "f" !')
    genre = 'masculin' if genre == 'm' else 'féminin'

    # Sélection et validation de la race
    races = {'1': 'Humain', '2': 'Elfe', '3': 'Nain', '4': 'Gnome'}
    race_choix = input('Race du personnage (1: Humain, 2 : Elfe, 3: Nain, 4: Gnome) : ')
    while race_choix not in races:
        print('ERREUR: choisissez 1, 2, 3 ou 4 !')
        race_choix = input('Race du personnage (1: Humain, 2 : Elfe, 3: Nain, 4: Gnome) : ')
    race = races[race_choix]

    # Classe attribuée aléatoirement (+ points de vie)
    classes = {1: 'Magicien', 2: 'Voleur', 3: 'Prêtre', 4: 'Guerrier'}
    dv = {'Magicien': 4, 'Voleur': 6, 'Prêtre': 8, 'Guerrier': 10}
    num_classe = random.randint(1, 4)
    classe = classes[num_classe]

    # Création du dictionnaire personnage
    personnage = {
        'nom': nom,
        'genre': genre,
        'race': race,
        'classe': classe,
        'dv': dv[classe],
        # Avatar défini directement pour éviter l'affichage des codes Unicode bruts
        'avatar': '👩‍🦰' if genre == 'féminin' else '👨‍🦱'
    }

    return personnage


def creer_boss(niveau):
    """
    Génère un boss en fonction du niveau donné.
    :param niveau: (int) Niveau du jeu (entre 1 et 5).
    :return: (dict) Un dictionnaire contenant les informations du boss (nom, pdv, avatar)
    """

    boss_data = {
        1: ('Malakar', 1, '🤖'),
        2: ('Déméthius', 20, '👾'),
        3: ('Vortex 9', 40, '👻'),
        4: ('Dr. Vexenstein', 70, '🧌'),
        5: ('Azael\'Xoth, [L\'ombre-éternelle]', 200, '👺')
    }

    nom, dv, avatar = boss_data[niveau]

    boss = {
        'nom': nom,
        'pdv': dv,
        'avatar': avatar
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

    # Calcul des points de vie du personnage en fonction du niveau
    pdv_personnage = personnage['dv'] * niveau

    # Affichage des adversaires
    avatar_nom_personnage = personnage['avatar'] + ' ' + personnage['nom']
    avatar_nom_boss = boss['avatar'] + ' ' + boss['nom']
    print(f'{avatar_nom_personnage} ({pdv_personnage} pdv)   🆚   {avatar_nom_boss} ({boss['pdv']} pdv)')
    print('--------------------------------------')

    # Booléen qui alterne entre joueur et boss à chaque tour
    joueur = False

    # Boucle de combat principal : le joueur et le boss alternent entre attaque et défense
    while boss['pdv'] > 0 and pdv_personnage > 0:
        joueur = not joueur
        defense = random.randint(0, niveau * 3)

        # Attaque plus puissante pour le joueur, moins forte pour le boss
        attaque = random.randint(niveau * 1, niveau * (5 if joueur else 3))

        # Si l'attaque dépasse la défense, un coup est porté
        if attaque > defense:
            coup_critique = False
            # 10% de chance de coup critique (x2 dégâts)
            if random.random() < 0.1:
                attaque *= 2
                coup_critique = True
            point_perdu = attaque - defense
            if joueur:
                # Attaque du joueur
                boss['pdv'] -= point_perdu
                print(f'\n{'💥 COUP CRITIQUE ! ' if coup_critique else ''}{avatar_nom_personnage} attaque de {attaque}')
                print(f'{avatar_nom_boss} perd {point_perdu} point{'s' if point_perdu > 1 else ''} de vie,'
                      f' il lui reste {boss['pdv']}')
            else:
                # Attaque du boss
                pdv_personnage -= point_perdu
                print(f'\n{'💥 COUP CRITIQUE ! ' if coup_critique else ''}{avatar_nom_boss} attaque de {attaque}')
                print(f'{avatar_nom_personnage} perd {point_perdu} point{'s' if point_perdu > 1 else ''} de vie,'
                      f' il lui reste {pdv_personnage}')
        else:
            print(f'\n🛡️ BOUCLIER : {avatar_nom_personnage if joueur else avatar_nom_boss} attaque, '
                  f'mais la défense de {avatar_nom_boss if joueur else avatar_nom_personnage} est trop forte !')

    if boss['pdv'] <= 0:
        print(f'\n{avatar_nom_personnage} a gagné{'e' if personnage['genre'] == 'féminin' else ''} ! 🎉')
        return True
    elif pdv_personnage <= 0:
        print(f'\n{avatar_nom_personnage} a perdu{'e' if personnage['genre'] == 'féminin' else ''} ! 😢')
        return False


def afficher_personnage(personnage):
    """
    Affiche les détails d'un personnage de manière formatée.
    :param personnage: (dict) Un dictionnaire contenant les détails du personnage.
    :return: /
    """
    print(f"--- Détails du personnage ---\n"
          f"Nom        : {personnage['nom']}\n"
          f"Genre      : {personnage['genre']}\n"
          f"Avatar     : {personnage['avatar']}\n"
          f"Race       : {personnage['race']}\n"
          f"Classe     : {personnage['classe']}\n"
          f"Dés de vie : {personnage['dv']}\n")


# Programme principal
choix_menu = ''
choix_combat = ''
personnage_2 = ''
premiere_partie = True
rejouer = ''
while choix_menu != 'q':
    if not premiere_partie and choix_combat != 'a':
        rejouer = input('Rejouer (r) - Quitter (q) : ')
    else:
        premiere_partie = False
    if rejouer == 'q':
        print('\nA bientôt 👋')
        break
    else:
        # Si le joueur veut rejouer, on réinitialise choix_combat pour la prochaine itération.
        choix_combat = ''

    print('\n------- Bienvenue sur le jeu "baldur\'s gate 4" -------\n')

    personnage_1 = creer_personnage()

    # Attribution du personnage 1 par défaut
    personnage_principal = personnage_1

    afficher_personnage(personnage_1)

    while personnage_2 == '':
        choix_creation = input('Créer un deuxième personnage ? o/n :  ')
        if choix_creation == 'o':
            personnage_2 = creer_personnage()
            afficher_personnage(personnage_2)
        elif choix_creation == 'n':
            break

    if personnage_2 != '':
        choix_personnage = int(
            input(f'Choisis ton personnage... \n'
                  f'{personnage_1['avatar']} {personnage_1['nom']} : {personnage_1['dv']} pdv (1) '
                  f'ou {personnage_2['avatar']} {personnage_2['nom']} : {personnage_2['dv']} pdv (2) : '))

        # Attribution du personnage choisi par l'utilisateur
        personnage_principal = personnage_2 if choix_personnage == 2 else personnage_1

    choix_menu = input(f'Voulez-vous combattre avec {personnage_principal['avatar']} {personnage_principal['nom']} (c)'
                       f' ou quitter le jeu (q) : ')
    if choix_menu == 'q':
        print('\nA bientôt 👋')

    niveau = 1

    if choix_menu == 'c':
        while choix_combat != 'a' and niveau <= 5:
            print(f'\n-------------  Niveau {niveau}  -------------')
            resultat = lancer_combat(personnage_principal, niveau)
            if resultat:
                niveau += 1
                print(f'Bravo tu as atteint le niveau {niveau} !')
                choix_combat = input(f'Pour continuer (c) ou choisir un autre personnage (a) : ')
            else:
                break
