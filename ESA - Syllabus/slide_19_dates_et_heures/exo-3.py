"""
    Exercice 3 :

    Écrivez un programme qui prend une liste de durées (par exemple, ['2:30', '1:45', '3:10'])
    et calcule la durée totale en heures et minutes.
"""
from datetime import datetime as dt, timedelta

durees = ['2:30', '1:45', '3:10']

total = timedelta()

for duree in durees:
    duree_dt = dt.strptime(duree, "%H:%M")  # 1900-01-01 02:30:00
    duree_timedelta = timedelta(hours=duree_dt.hour, minutes=duree_dt.minute)  # 2:30:00
    total += duree_timedelta  # 7:25:00


# SOIT..
# Convertir le timedelta en datetime, comme ça on peut utiliser strftime pour l'affichage des heures et minutes

# Initialiser un datetime "fictif" de base
dt_de_base = dt(1, 1, 1)  # 0001-01-01 00:00:00

# Ajouter la durée au datetime "fictif" de base 0001-01-01 07:25:00
print(f"La durée totale est {(dt_de_base + total).strftime("%Hh%M")} !")      # La durée totale est 07h25 !

# ====================================================================

# OU BIEN...
# Calculer les heures et les minutes

# Convertir en secondes
total_seconds = int(total.total_seconds())

# Calculer heures et minutes
heures = total_seconds // 3600
minutes = (total_seconds % 3600) // 60

# Formater le texte
print(f"La durée totale est {heures:02}h{minutes:02} !")

# ====================================================================

# OU BIEN...

heures, reste = divmod(total, timedelta(hours=1))
minutes, secondes = divmod(reste, timedelta(minutes=1))
print(f"La durée totale est {heures:02}h{minutes:02} !")      # La durée totale est 07h25 !
