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

# =========================================================================
# ============================   TESTS  ==================================
# =========================================================================

# text = "Depuis quelque temps, j'ai envie de changer ma routine."
# text = "Peut-être as-tu une autre idée à me proposer ?"
# text = "Depuis quelque temps, j'ai envie de changer ma routine. Peut-être as-tu une autre idée à me proposer ? Troisème phrases."
# text = "Ce matin, j’ai hésité : devrais-je courir, lire un livre, ou simplement me reposer ; qu’en penses-tu ?"
# text = ("Hier, j'ai réfléchi à plusieurs options : "
#             "partir en voyage, rester chez moi, ou visiter des amis ; "
#             "laquelle préfères-tu ?")
# text = ("Depuis quelque temps, j'ai envie de changer ma routine. "
#         "Hier, j'ai réfléchi à plusieurs options : "
#         "partir en voyage, rester chez moi, ou visiter des amis ; laquelle préfères-tu ? "
#         "Peut-être as-tu une autre idée à me proposer.")
# text = "Entrez une phrase : Bonjour ; comment ça va ? Ma 2e phrase."

# =========================================================================
# =========================================================================
# =========================================================================


# def validate_sentence():
#     """
#     Valide une phrase selon les règles typographiques suivantes :
#
#     - La phrase doit commencer par une majuscule.
#     - La phrase doit se terminer par un point.
#     - Les mots doivent être séparés par un seul espace (pas de doubles espaces).
#     - Les ponctuations doivent respecter les règles suivantes :
#         - Les virgules (,) et points (.) doivent être collés au mot précédent.
#         - Les virgules (,) et points (.) doivent être suivies d'un espace, sauf en fin de phrase pour le point (.).
#         - Les caractères spéciaux (;, :, ?) doivent être entourés d'espaces.
#
#     La fonction demande à l'utilisateur de saisir une phrase et affiche des messages
#     d'erreur spécifiques pour chaque violation des règles.
#     Elle continue de demander une saisie jusqu'à ce que la phrase soit valide.
#
#     Une fois la phrase validée, elle affiche un message de confirmation.
#     """
#     is_valid = False
#
#     while not is_valid:
#         text = input("Entrez une phrase : ")   # Est-ce qu'il y a quelqu'un ? je suis arrivée.
#
#         # Vérifier que la phrase commence par une majuscule
#         if not text[0].isupper():
#             print("La phrase doit commencer par une majuscule.")
#             continue
#
#         # Vérifier que la phrase se termine par un point
#         if text[-1] != ".":
#             print("La phrase doit se terminer par un point.")
#             continue
#
#         # Vérifier qu'il n'y a pas de doubles espaces
#         if "  " in text:
#             print("Les mots doivent être séparés par un seul espace.")
#             continue
#
#         # Vérifier la typographie des ponctuations
#         i = 0
#         error_found = False
#         while i < len(text):
#             char = text[i]
#
#             # Vérification pour la virgule et le point
#             if char in ",.":
#                 if i > 0 and text[i - 1] == " ":
#                     print(f"Le caractère '{char}' doit être collé au mot qui le précède.")
#                     error_found = True
#                     break
#                 if char == "." and i == len(text) - 1:
#                     pass  # Dernier point : pas d'espace requis
#                 elif i < len(text) - 1 and text[i + 1] != " ":
#                     print(f"Le caractère '{char}' doit être suivi d'un espace.")
#                     error_found = True
#                     break
#
#             # Vérification pour le point-virgule, les deux points, et le point d'interrogation
#             elif char in ";:?":
#                 if (i > 0 and text[i - 1] != " ") or (i < len(text) - 1 and text[i + 1] != " "):
#                     print(f"Le caractère '{char}' doit être entouré d'espaces.")
#                     error_found = True
#                     break
#
#             i += 1
#
#         if error_found:
#             continue  # Recommence la saisie si une erreur a été trouvée
#
#         # Si aucune erreur n'est trouvée, la phrase est validée
#         print("La phrase respecte les règles typographiques.")
#         is_valid = True
#
#
# validate_sentence()


# =========================================================================
# =========================================================================
# =========================================================================


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
    Vérifie qu'une phrase respecte plusieurs règles grammaticales et typographiques.

    Cette fonction effectue plusieurs vérifications sur une phrase entrée par l'utilisateur :
    - La phrase doit commencer par une majuscule.
    - La phrase doit se terminer par un point final.
    - Il ne doit pas y avoir d'espace entre le dernier mot et le point final.
    - La phrase ne doit pas contenir plus d'un espace consécutif entre les mots.
    - Aucun espace ne doit apparaître avant une virgule.
    - Il doit y avoir exactement un espace après chaque virgule.
    - Les caractères de ponctuation spécifiques `:`, `;` et `?` doivent avoir un espace avant et après eux.

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


if __name__ == '__main__':
    check_typographie()
