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

from numpy.ma.core import append


def creer_personnage(id):
    """
    Crée un personnage en demandant à l'utilisateur de saisir son nom, son genre, sa race
    et attribue une classe aléatoirement.
    :return: (dict) Un dictionnaire contenant les informations du personnage (nom, genre, race, classe, dv, avatar)
    """

    # Demande le nom du personnage
    nom = input('\nNom du personnage : ')

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
        'id': id,
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


def generer_personnages(n=10):
    """
    Génère une liste de personnages avec des attributs aléatoires.
    :param n: (int) Nombre de personnages à générer (par défaut 10).
    :return: (list) Une liste de dictionnaires représentant les personnages générés.
    """
    races = {'1': 'Humain', '2': 'Elfe', '3': 'Nain', '4': 'Gnome'}
    classes = {1: 'Magicien', 2: 'Voleur', 3: 'Prêtre', 4: 'Guerrier'}
    dv = {'Magicien': 4, 'Voleur': 6, 'Prêtre': 8, 'Guerrier': 10}
    avatars = {'Magicien': '🧙', 'Voleur': '🧝‍♂️', 'Prêtre': '👨‍🦱', 'Guerrier': '🥷'}
    noms_possibles = ["Aragorn", "Luthien", "Gimli", "Merlin", "Thorin", "Elrond", "Gandalf", "Legolas", "Eowyn",
                      "Tauriel"]

    noms_utilises = set()  # Stocke les noms déjà utilisés

    personnages = []

    for i in range(n):
        # Choix d'un nom unique
        nom = random.choice(noms_possibles)
        while nom in noms_utilises:
            nom = random.choice(noms_possibles)
        noms_utilises.add(nom)

        genre = random.choice(["masculin", "féminin"])
        race = races[random.choice(list(races.keys()))]
        classe = classes[random.randint(1, 4)]

        personnage = {
            'id': i,
            'nom': nom,
            'genre': genre,
            'race': race,
            'classe': classe,
            'dv': dv[classe],
            'avatar': avatars[classe]
        }
        personnages.append(personnage)

    return personnages


def afficher_personnages(personnages):
    """
    Affiche les personnages en colonnes bien alignées sans bibliothèque externe.
    TODO : compléter doctsrting
    """
    # Définition des largeurs de colonnes
    col_widths = {
        "Id": 4, "Nom": 10, "Genre": 10, "Race": 10, "Classe": 10, "DV": 4, "Avatar": 6
    }

    # Affichage de l'en-tête
    header = (f" {'Id'.ljust(col_widths['Id'])}"
              f" | {'Nom'.ljust(col_widths['Nom'])} | {'Genre'.ljust(col_widths['Genre'])}"
              f" | {'Race'.ljust(col_widths['Race'])} | {'Classe'.ljust(col_widths['Classe'])}"
              f" | {'DV'.ljust(col_widths['DV'])} | {'Avatar'.ljust(col_widths['Avatar'])}")
    print('\n' + header)
    print("-" * len(header))

    # Affichage des personnages
    for i, personnage in enumerate(personnages):
        row = (f"  {str(i + 1).ljust(col_widths['Id'])}"
               f"| {personnage['nom'].ljust(col_widths['Nom'])}"
               f" | {personnage['genre'].ljust(col_widths['Genre'])}"
               f" | {personnage['race'].ljust(col_widths['Race'])}"
               f" | {personnage['classe'].ljust(col_widths['Classe'])}"
               f" | {str(personnage['dv']).ljust(col_widths['DV'])}"
               f" | {personnage['avatar'].ljust(col_widths['Avatar'])}")
        print(row)


def choisir_personnage(personnages):
    """
    Permet à l'utilisateur de choisir un personnage existant ou d'en créer un nouveau.
    TODO : compléter doctsrting
    """
    print('\nVos personnages :')
    afficher_personnages(personnages)

    while True:
        # choix = int(input('\nCombattre avec : '))
        choix = int(input('\nEntrer l\'identifiant du personnage ou (0) pour revenir au menu : '))

        # Sélection d'un personnage existant
        if 1 <= choix <= len(personnages):
            return personnages[choix - 1]

        elif choix == 0:
            return 0

        else:
            print("Veuillez entrer un numéro valide.")


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


def lancer_phase_de_combat(personnage_en_jeu):
    """
    Gère la phase de combat.
    TODO : compléter doctsrting
    """
    niveau = 1
    choix_combat = ''

    while choix_combat != 'n' and niveau <= 5:
        print(f"\n-------------  Niveau {niveau}  -------------")
        resultat = lancer_combat(personnage_en_jeu, niveau)

        if resultat:
            niveau += 1
            print(f"Bravo, tu as atteint le niveau {niveau} !")
            choix_combat = input("Continuer ? o/n : ").lower()
        else:
            print("\n--------  Fin du combat  --------")
            break


def lancer_jeu():
    """
    Affiche le menu principal et gère les choix de l'utilisateur.
    TODO : compléter doctsrting
    """
    action_principale = ''
    personnages = []
    # TODO: créer des personnages -> generer_personnages(2)
    personnage_en_jeu = None
    premier_lancement = True
    decision_rejouer = ''

    while action_principale != 'q':
        if premier_lancement:
            premier_lancement = False
            print('\n------------ Bienvenue sur "Baldur\'s Gate 4" ------------')
            personnages = generer_personnages(2)

        action_principale = input("\n--------  MENU  --------\n"
                                  "1: Créer un personnage\n"
                                  "2: Choisir un personnage\n"
                                  "3: Combattre\n"
                                  "q: Quitter\n"
                                  "Votre choix : ").lower()

        if action_principale == 'q':
            print("\nÀ bientôt 👋")
            break

        elif action_principale == '1':  # Créer un personnage
            nouveau_personnage = creer_personnage(len(personnages))
            if nouveau_personnage:
                personnages.append(nouveau_personnage)
                # afficher_personnages(personnages)
                print('\nVotre personnage a bien été ajouté à la liste des personnages !')

        elif action_principale == '2':  # Choisir un personnage
            personnage_en_jeu = choisir_personnage(personnages)
            if isinstance(personnage_en_jeu, dict):  # Vérifie que c'est bien un personnage (dictionnaire)
                print(f"\nVous avez choisi : {personnage_en_jeu['avatar']} {personnage_en_jeu['nom']}")

        elif action_principale == '3':  # Combattre
            if not isinstance(personnage_en_jeu, dict):
                print("\nVeuillez d'abord choisir un personnage !")
            else:
                lancer_phase_de_combat(personnage_en_jeu)


# Lancement du jeu
lancer_jeu()
