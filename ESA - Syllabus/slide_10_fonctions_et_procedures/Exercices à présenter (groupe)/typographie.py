"""
    Écrire un programme qui renvoie une erreur si une phrase encodée
    par l'utilisateur ne vérifie pas les règles élémentaires de typographie :
        ● La phrase commence par une Majuscule.
        ● La phrase se termine par un point.
        ● Les mots sont séparés par un et un seul espace, excepté en cas
          de symbole de ponctuation (dans ce cas, on respecte les règles ci-après) :
                ● La virgule et le point sont collés au mot qui les précède et sont suivi par un espace.
                ● Le point-virgule, les deux points et le point d'interrogation sont entourés d'un espace.
"""


def check_espaces_autour(phrase, compteur, ponctuation):
    """
    Vérifie la présence d'un espace avant et après les caractères donnés (ponctuation)
    : pre : phrase es la chaîne de caractère (str) à vérifier
    : pre : compteur est un nombre (int) qui représente la position du caractère dans la phrase
    : pre : ponctuation est le caractère (str) pour lequel il faut vérifier les espaces avant et après
    : post : ne retourne rien
    """
    if phrase[compteur] == ponctuation:
        if phrase[compteur - 1] != " " or phrase[compteur + 1] != " ":
            exit(f"Erreur : il faut un espace des deux côtés du {ponctuation}")


def check_typographie():
    """
    Cette fonction effectue plusieurs vérifications sur une phrase entrée par l'utilisateur.

    Conditions de validité :
        * La phrase doit commencer par une majuscule.
        * La phrase doit se terminer par un point final.
        * Il ne doit pas y avoir d'espace entre le dernier mot et le point final.
        * La phrase ne doit pas contenir plus d'un espace consécutif entre les mots.
        * Aucun espace ne doit apparaître avant une virgule.
        * Il doit y avoir exactement un espace après chaque virgule.
        * Les caractères de ponctuation spécifiques `:`, `;` et `?` doivent avoir un espace avant et après eux.

    :returns : Si une des règles n'est pas respectée, le programme affiche un message d'erreur
                spécifique et termine l'exécution.
    """
    phrase = input("Entrez une phrase : ")     # Est-ce qu'il y a quelqu'un ? Je suis arrivée.

    if not phrase[0].isupper():
        print("Erreur : la phrase doit commencer par une majuscule!")

    if phrase[len(phrase) - 1] != ".":
        print("Erreur : la phrase doit se terminer par un point ! ")

    if phrase[len(phrase) - 2] == " ":
        print("Erreur : le point doit être collé au mot qui le précède ! ")

    phrase_split = phrase.split(" ")
    for i in phrase_split:  # Vérifie s'il n'y a bien qu'un seul espace
        if i == '':
            exit("Erreur : la phrase ne peut comporter qu'un seul espace entre deux mots!")

    virgule_split = phrase.split(",")
    compteur = 0
    while compteur < len(virgule_split):
        if virgule_split[compteur][-1] == " ":  # Vérifie s'il n'y a pas d'espace avant la virgule
            exit("Erreur : il ne faut pas d'espace avant une virgule!")
        if compteur + 1 < len(virgule_split):  # Vérifie s'il y a bien un espace après une virgule
            if virgule_split[compteur + 1][0] != " ":
                exit("Erreur : il faut un espace après une virgule!")
        compteur += 1

    compteur = 0
    while compteur < len(phrase):  # Vérifie les espaces avant et après les caractères ":", ";" et "?"
        check_espaces_autour(phrase, compteur, ";")
        check_espaces_autour(phrase, compteur, "?")
        check_espaces_autour(phrase, compteur, ":")
        compteur += 1


check_typographie()
