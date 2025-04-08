"""
    Slide 19 : Les dates et les heures
"""

from datetime import date
from datetime import datetime as dt
from datetime import time
from datetime import timedelta
from calendar import calendar

print()

now = dt.now()
# print(now)

# print(now.strftime('%d/%m/%Y'))   # strftime => string formated time
# print(now.strftime('%Hh%M'))


mon_heure = time(17, 15, 0)  # il est 17h15
# print(mon_heure)  # Affiche l'heure au format 'heure:minute:seconde'


date_str = "2024-04-13"
date_dt = dt.strptime(date_str, "%Y-%m-%d")  # strptime() construit la chaîne en datetime
# print(date_dt)  # 2024-04-13 00:00:00

formatted_date = date_dt.strftime("%A, %d %B %Y")
# print(formatted_date)  # Saturday, 13 April 2024


today = date.today()
print(today)

date_de_naissance = date(year=1978, month=3, day=16)
# print(date_de_naissance)


def calculate_age(born):
    """
    :param born: (date) la date de naissance
    :return: (int) l'âge
    """
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


# print(calculate_age(date_de_naissance))

age = (date.today() - date_de_naissance) // timedelta(days=365.2425)   # // est l'opérateur de la division entière
# print(age)

# print(timedelta.__doc__)
# help(timedelta)
