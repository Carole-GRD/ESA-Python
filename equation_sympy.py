from sympy import symbols, Eq, solve

# Définir les variables
x1, x2, x3 = symbols('x1 x2 x3')

# Équations basées sur les données du problème
eq1 = Eq(0.15*x1 + 0.75*x2 + 0.25*x3, 35.6)  # Volume total
eq2 = Eq(9*x1 + 24*x2 + 15*x3, 1590)         # Masse totale (kg)
eq3 = Eq(x1 + x2 + x3, 108)                  # Nombre total de télévisions

# Résoudre le système d'équations
sol = solve((eq1, eq2, eq3), (x1, x2, x3))

# Calculer la valeur marchande totale
valeur_totale = 402*sol[x1] + 1462*sol[x2] + 749*sol[x3]




# # Arrondir les résultats
# sol_rounded = {key: round(value.evalf()) for key, value in sol.items()}
# valeur_totale_rounded = round(valeur_totale.evalf())

# Arrondir les résultats à 2 décimales
sol_rounded = {key: "{:.2f}".format(value.evalf()) for key, value in sol.items()}
valeur_totale_rounded = "{:.2f}".format(valeur_totale.evalf())



print(f'sol : {sol_rounded}')
print(f'valeur_totale = {valeur_totale_rounded}')



