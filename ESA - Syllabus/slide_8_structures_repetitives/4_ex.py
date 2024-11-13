"""
    Exercice 4 :

    Écrire un programme affichant un triangle rempli d’étoiles s’étendant sur 7 lignes comme
    indiqué ci-dessous :
    *
    **
    ***
    ****
    *****
    ******
    *******
"""

# lign = "*"
# for i in range(7):  # de 0 à 6 (car 7 exclu) -> 7 itérations
#     print(lign)
#     lign += "*"

# lign = "*"
# for i in range(7):     # de 0 à 6 (car 7 exclu) -> 7 itérations
#     print("*"*(i+1))   # on multiplie par (i+1) car on veut de 1 à 7 étoiles

# lign = "*"
# for i in range(1, 8):     # de 1 à 7 (car 8 exclu) -> 7 itérations
#     print("*"*i)          # on multiplie par i car on veut de 1 à 7 étoiles

stars = "*******"
lign = ""
for star in stars:
    lign += star
    print(lign)

