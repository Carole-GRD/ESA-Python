"""
    Exercice 3 :

    Écrivez un programme qui prend une liste de durées (par exemple, ['2:30', '1:45', '3:10'])
    et calcule la durée totale en heures et minutes.
"""
from datetime import timedelta


def additionner_durees(liste_durees):
    """
    :param liste_durees: (list) Une liste de durées sous forme de chaînes de caractères,
                                chaque chaîne étant au format 'HH:MM'.
    :return: (tuple) Un tuple contenant le total en heures et minutes (int, int).
    """
    total = timedelta()

    for duree in liste_durees:
        try:
            heures, minutes = map(int, duree.split(':'))
            total += timedelta(hours=heures, minutes=minutes)
        except ValueError:
            print(f"Erreur : la durée '{duree}' n'est pas au format 'HH:MM'.")
            continue  # Ignore cette durée et passe à la suivante

    # Extraire heures et minutes de l'objet timedelta
    heures, reste = divmod(total.total_seconds(), 3600)
    minutes = reste // 60

    return int(heures), int(minutes)


# Utilisation
durees = ['2:30', '1:45', '3:10', 'invalid']
heures, minutes = additionner_durees(durees)
print(f"Durée totale : {heures:02}h{minutes:02}")  # ➡️ Durée totale : 07h25
