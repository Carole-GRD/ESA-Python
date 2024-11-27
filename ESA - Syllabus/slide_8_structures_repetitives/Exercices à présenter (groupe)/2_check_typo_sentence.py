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

is_valid = False

while not is_valid:
    text = input("Entrez une phrase : ")

    # Vérifier que la phrase commence par une majuscule
    if not text[0].isupper():
        print("La phrase doit commencer par une majuscule.")
        continue

    # Vérifier que la phrase se termine par un point
    if text[-1] != ".":
        print("La phrase doit se terminer par un point.")
        continue

    # Vérifier qu'il n'y a pas de doubles espaces
    if "  " in text:
        print("Les mots doivent être séparés par un seul espace.")
        continue

    # Vérifier la typographie des ponctuations
    i = 0
    error_found = False
    while i < len(text):
        char = text[i]

        # Vérification pour la virgule et le point
        if char in ",.":
            if i > 0 and text[i - 1] == " ":
                print(f"Le caractère '{char}' doit être collé au mot qui le précède.")
                error_found = True
                break
            if char == "." and i == len(text) - 1:
                pass  # Dernier point : pas d'espace requis
            elif i < len(text) - 1 and text[i + 1] != " ":
                print(f"Le caractère '{char}' doit être suivi d'un espace.")
                error_found = True
                break

        # Vérification pour le point-virgule, les deux points, et le point d'interrogation
        elif char in ";:?":
            if (i > 0 and text[i - 1] != " ") or (i < len(text) - 1 and text[i + 1] != " "):
                print(f"Le caractère '{char}' doit être entouré d'espaces.")
                error_found = True
                break

        i += 1

    if error_found:
        continue  # Recommence la saisie si une erreur a été trouvée

    # Si aucune erreur n'est trouvée, la phrase est validée
    print("La phrase respecte les règles typographiques.")
    is_valid = True


# =========================================================================
# =========================================================================
# =========================================================================

# # phrase = input("Entre une phrase : ")
# phrase = "Entrez une phrase. Bonjour : comment, ça va ? Ma 2e phrase."
# phrase_split = phrase.split(" ")
# virgule_split = phrase.split(",")
#
# if phrase[0] != phrase[0].upper():  # vérifie que la pharse commence bien par une majuscule
#     print("Erreur: la pharse doit commencer par une majuscule!")
# if phrase[len(phrase)-1] != ".":  # vérifie si la phrase se termine bien par un point
#     print("Erreur: la pharse doit se terminer par un point! ")
# for i in phrase_split:  # vérifie s'il y a bien que un seul espace
#     if i == '':
#         exit("Erreur: la pharse ne peut comporter que un seul espace entre deux mots!")
# compteur = 0
# while compteur < len(virgule_split):
#     if virgule_split[compteur][-1] == " ":  # verifie s'il n'y a pas d'espace avant la vigule
#         exit("Erreur : il ne faut pas d'espace avant une virgule!")
#     if compteur + 1 < len(virgule_split):  # vérifie s'il y a bien un espace apres une virgule
#         if virgule_split[compteur + 1][0] != " ":
#             exit("Erreur : il faut un espace après une virgule!")
#     compteur += 1
# compteur = 0
# while compteur < len(phrase):  # vérifie les l'esapce avant et apres du ":", ";" et "?"
#     if (phrase[compteur] == ";" and phrase[compteur-1] != " ") or (
#             phrase[compteur] == ";" and phrase[compteur+1] != " ") or (
#             phrase[compteur] == ";" and phrase[compteur-1] != " " and phrase[compteur] == ";" and phrase[
#             compteur+1] != " "):
#         exit("Erreur: il faut un espace des deux coté du ; ")
#     if (phrase[compteur] == "?" and phrase[compteur - 1] != " ") or (
#             phrase[compteur] == "?" and phrase[compteur + 1] != " ") or (
#             phrase[compteur] == "?" and phrase[compteur - 1] != " " and phrase[compteur] == ";" and phrase[
#             compteur + 1] != " "):
#         exit("Erreur: il faut un espace des deux coté du ? ")
#     if (phrase[compteur] == ":" and phrase[compteur - 1] != " ") or (
#             phrase[compteur] == ":" and phrase[compteur + 1] != " ") or (
#             phrase[compteur] == ":" and phrase[compteur - 1] != " " and phrase[compteur] == ";" and phrase[
#             compteur + 1] != " "):
#         exit("Erreur: il faut un espace des deux coté du :  ")
#
#     compteur += 1
