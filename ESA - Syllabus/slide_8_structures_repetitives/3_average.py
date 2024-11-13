"""
    Exercice 3 :

    Écrire un programme qui demande le nombre de cote (sur 20) à introduire (maximum 5)
    et qui en calcul la moyenne de l’étudiant.

    Prévoyez la possibilité d’abandonner après chaque introduction de cote.
"""


def saisir_note(numero):
    """
    Fonction qui gère la saisie d'une note avec validation
    et possibilité d'abandon.
    """
    prompt = f"Entrez la {numero}e note sur 20 (ou 'q' pour quitter) : "

    while True:
        entry = input(prompt)

        # Vérification de l'abandon
        if entry.lower() == 'q':
            return None

        try:
            note = float(entry)
            if 0 <= note <= 20:
                return note
            else:
                prompt = "La note doit être comprise entre 0 et 20 : "
        except ValueError:
            prompt = "Veuillez entrer un nombre valide : "


def calculer_moyenne():
    """
    Programme principal qui gère la saisie des notes
    et le calcul de la moyenne.
    """
    # Demander le nombre de notes à saisir
    while True:
        try:
            nb_notes = int(input("Combien de notes voulez-vous entrer (max 5) ? "))
            if 1 <= nb_notes <= 5:
                break
            else:
                print("Le nombre de notes doit être entre 1 et 5.")
        except ValueError:
            print("Veuillez entrer un nombre entier.")

    # Liste pour stocker les notes
    notes = []

    # Saisie des notes
    for i in range(nb_notes):
        note = saisir_note(i + 1)

        # Vérifier si l'utilisateur veut abandonner
        if note is None:
            if not notes:
                print("Aucune note n'a été saisie.")
                return
            break

        notes.append(note)

    # Calcul et affichage de la moyenne
    average = sum(notes) / len(notes)
    print(f"\nNotes saisies : {', '.join(str(note) for note in notes)}")
    print(f"Moyenne : {average:.2f}/20")


if __name__ == "__main__":
    calculer_moyenne()
