"""
    Description:
        The objective of Duck, duck, goose is to walk in a circle,
        tapping on each player's head until one is chosen.

    Task:
        Given an array of Player objects and a position (first position is 1),
        return the name of the chosen Player.
        <name> is a property of <Player> objects, e.g <Player.name>

    Example:
        duck_duck_goose([a, b, c, d], 1) should return a.name
        duck_duck_goose([a, b, c, d], 5) should return a.name
        duck_duck_goose([a, b, c, d], 4) should return d.name

    Random input limits:
        6 ≤ Players ≤ 50
        5000 ≤ Position ≤ 50000
"""



# ===========
# Ma version
# ===========

# import random
#
# players = ['Jean', 'Jane', 'Alex', 'Lily', 'Tom', 'Joe']
# # players = ['Jean', 'Jane', 'Alex', 'Lily']
# # position = random.randrange(1, 17, 1)
# position = random.randrange(5000, 50000, 1)
#
# def duck_duck_goose(players_list, selected_position):
#     if selected_position % len(players_list) == 0:
#         index = len(players_list) - 1
#     else:
#         index = (selected_position % len(players_list)) - 1
#     print(f"player : {players_list[index]}")
#
#
# duck_duck_goose(players, position)





# ===========
# chatGPT
# ===========

def duck_duck_goose(players, position):
    # Calcul de l'indice réel dans la liste en tenant compte du décalage circulaire
    index = (position - 1) % len(players)
    # Retourne le nom du joueur à cet indice
    return players[index].name



# Exemple d'utilisation :
# -----------------------

class Player:
    def __init__(self, name):
        self.name = name


# Création de quelques objets joueur
a = Player("Alice")
b = Player("Bob")
c = Player("Charlie")
d = Player("Dana")

# Création d'une liste de joueurs
players = [a, b, c, d]

# Test du programme
print(duck_duck_goose(players, 1))  # Devrait retourner "Alice"
print(duck_duck_goose(players, 5))  # Devrait retourner "Alice"
print(duck_duck_goose(players, 4))  # Devrait retourner "Dana"


# import random
# print(duck_duck_goose(players, random.randrange(5000, 50000, 1)))
