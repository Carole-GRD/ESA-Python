"""
Jeu de combat dans lequel un personnage affronte des boss de niveaux croissants.

Le programme permet de :
    1. Créer un ou deux personnages avec des caractéristiques variées.
    2. Sélectionner un personnage pour combattre le boss.
    3. Générer des boss avec des points de vie augmentant à chaque niveau.
    4. Simuler des combats au tour par tour jusqu'à la victoire ou la défaite.

Le joueur peut progresser à travers plusieurs niveaux en battant successivement des boss de plus en plus puissants.

Date : 10-02-2025
Auteurs : Gwenaël, Hyacinthe, Alfred, Edith, Franck, Boris, Carole, Christian
"""
import random


def creer_personnage(personnages):
    """
    Crée un personnage en demandant à l'utilisateur de saisir son nom, son genre, sa race
    et attribue une classe aléatoirement.
    :param personnages: (list) La liste actuelle des personnages.
    :return: (dict) Un dictionnaire contenant les informations du personnage.
    """

    numero = max([p['numero'] for p in personnages], default=-1) + 1  # Trouve le plus grand numéro existant et ajoute 1

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
        'numero': numero,
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
    :return: (dict) Un dictionnaire contenant les informations du boss.
    """

    boss_data = {
        1: ('Malakar', 1, '🤖'),
        2: ('Déméthius', 20, '👾'),
        3: ('Vortex 9', 40, '👻'),
        4: ('Dr. Vexenstein', 70, '🧌'),
        5: ('Azael\'Xoth, [L\'ombre-éternelle]', 100, '👺')
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
            'numero': i,
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
    Affiche les personnages sous forme de tableau.
    :param personnages: (list) Une liste de dictionnaires représentant les personnages.
    """

    # Définition des largeurs de colonnes
    col_widths = {
        "Numero": 3, "Nom": 10, "Genre": 10, "Race": 10, "Classe": 10, "DV": 4, "Avatar": 6
    }

    # Affichage de l'en-tête
    header = (f" {'N°'.ljust(col_widths['Numero'])}"
              f" | {'Nom'.ljust(col_widths['Nom'])}"
              f" | {'Genre'.ljust(col_widths['Genre'])}"
              f" | {'Race'.ljust(col_widths['Race'])}"
              f" | {'Classe'.ljust(col_widths['Classe'])}"
              f" | {'DV'.ljust(col_widths['DV'])}"
              f" | {'Avatar'.ljust(col_widths['Avatar'])}")
    print('\n' + header)
    print("-" * len(header))

    # Affichage des personnages
    for i, personnage in enumerate(personnages):
        row = (f" {str(i + 1).ljust(col_widths['Numero'])}"
               f" | {personnage['nom'].ljust(col_widths['Nom'])}"
               f" | {personnage['genre'].ljust(col_widths['Genre'])}"
               f" | {personnage['race'].ljust(col_widths['Race'])}"
               f" | {personnage['classe'].ljust(col_widths['Classe'])}"
               f" | {str(personnage['dv']).ljust(col_widths['DV'])}"
               f" | {personnage['avatar'].ljust(col_widths['Avatar'])}")
        print(row)


def choisir_personnage(personnages):
    """
    Permet à l'utilisateur de choisir un personnage existant.
    :param personnages: (list) Une liste de dictionnaires contenant les personnages.
    :return: (dict | int) Le dictionnaire contenant les caractéristiques du personnage sélectionné
             ou l'entier 0 si l'utilisateur choisit de revenir au menu.
    """

    print('\nVos personnages :')
    afficher_personnages(personnages)

    while True:
        try:
            choix = int(input('\nNuméro du personnage choisi ou (0) pour revenir au menu : '))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue  # Redemande une entrée

        # Sélection d'un personnage existant
        if 1 <= choix <= len(personnages):
            return personnages[choix - 1]
        elif choix == 0:
            return 0


def lancer_combat(personnage, niveau=1):
    """
    Lance un combat entre un personnage et un boss du niveau donné.
    :param personnage: (dict) Dictionnaire contenant les informations du personnage combattant.
    :param niveau: (int) Niveau du jeu (par défaut : 1).
    :return: (bool) True si le personnage gagne le combat, False sinon.
    """

    boss = creer_boss(niveau)

    # Calcul des points de vie du personnage en fonction du niveau
    pdv_personnage = personnage['dv'] * niveau

    # Affichage des adversaires
    avatar_nom_personnage = personnage['avatar'] + ' ' + personnage['nom']
    avatar_nom_boss = boss['avatar'] + ' ' + boss['nom']
    print(f"\n-------------  Niveau {niveau}  -------------")
    print(f'{avatar_nom_personnage} ({pdv_personnage} pdv)   🆚   {avatar_nom_boss} ({boss['pdv']} pdv)')
    print('--------------------------------------')

    # Booléen qui alterne entre joueur et boss à chaque tour
    joueur = False

    # Boucle de combat principal
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
            degats = attaque - defense

            if joueur:  # Attaque du joueur
                boss['pdv'] -= degats
                print(f'\n{'💥 COUP CRITIQUE ! ' if coup_critique else ''}{avatar_nom_personnage} attaque de {attaque}')
                print(f'{avatar_nom_boss} perd {degats} point{'s' if degats > 1 else ''} de vie,'
                      f' il lui reste {boss['pdv']}')
            else:  # Attaque du boss
                pdv_personnage -= degats
                print(f'\n{'💥 COUP CRITIQUE ! ' if coup_critique else ''}{avatar_nom_boss} attaque de {attaque}')
                print(f'{avatar_nom_personnage} perd {degats} point{'s' if degats > 1 else ''} de vie,'
                      f' il lui reste {pdv_personnage}')
        else:
            print(f'\n🛡️ BOUCLIER : {avatar_nom_personnage if joueur else avatar_nom_boss} attaque, '
                  f'mais la défense de {avatar_nom_boss if joueur else avatar_nom_personnage} est trop forte !')

    if boss['pdv'] <= 0:
        print(f'\n{avatar_nom_personnage} a gagné ! 🎉')
        return True
    elif pdv_personnage <= 0:
        print(f'\n{avatar_nom_personnage} a perdu ! 😢')
        return False


def lancer_phase_de_combat(personnage_en_jeu):
    """
    Gère la phase de combat.
    :param personnage_en_jeu: (dict) Dictionnaire contenant les informations du personnage combattant.
    """

    niveau = 1

    while niveau <= 5:
        if not lancer_combat(personnage_en_jeu, niveau):
            break  # Arrête la boucle si le combat est perdu

        niveau += 1  # Augmente le niveau seulement si le combat est gagné

        if niveau <= 5:  # Vérifie si un prochain combat est possible
            print(f"\nBravo, tu as atteint le niveau {niveau} !")
            if input("\nContinuer ? o/n : ").lower() == 'n':
                break

    print("\n--------  Fin du combat  --------")


def lancer_jeu():
    """
    Affiche le menu principal et gère les choix de l'utilisateur.
    """
    action_principale = ''
    personnages = []
    personnage_en_jeu = None
    premier_lancement = True

    while action_principale != 'q':
        if premier_lancement:
            premier_lancement = False
            print('\n------------ Bienvenue sur "Baldur\'s Gate 4" ------------')
            personnages = generer_personnages(2)  # Création de deux personnages aléatoirement

        action_principale = input(f"\n--------  MENU  --------\n"
                                  f"1: Créer un personnage\n"
                                  f"2: Choisir un personnage\n"
                                  f"3: Combattre{f' avec {personnage_en_jeu["nom"]}' if personnage_en_jeu else ''}\n"
                                  f"q: Quitter\n"
                                  f"Votre choix : ").lower()

        match action_principale:
            case 'q':
                print("\nÀ bientôt 👋")
                break

            case '1':  # Créer un personnage
                nouveau_personnage = creer_personnage(personnages)
                if nouveau_personnage:
                    personnages.append(nouveau_personnage)
                    print('\nVotre personnage a bien été ajouté à la liste des personnages !')

            case '2':  # Choisir un personnage
                personnage_en_jeu = choisir_personnage(personnages)
                # Vérifie qu'on reçoit un personnage (dictionnaire) et pas le nombre 0 qui permet de retourner au menu
                if isinstance(personnage_en_jeu, dict):
                    print(f"\n=>  Vous avez choisi : {personnage_en_jeu['avatar']} {personnage_en_jeu['nom']}")

            case '3':  # Combattre
                if not isinstance(personnage_en_jeu, dict):
                    print("\nVeuillez d'abord choisir un personnage !")
                else:
                    lancer_phase_de_combat(personnage_en_jeu)


# Lancement du jeu
lancer_jeu()
