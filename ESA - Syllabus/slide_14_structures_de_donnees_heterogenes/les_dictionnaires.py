"""
    Un enregistrement (ou article) est une structure hétérogène d’éléments pouvant être de types différents.
    Ces éléments sont appelés champs.
"""

# =====================================================================================
# ============================= Les dictionnaires =====================================
# =====================================================================================

mon_dico = {}  # initialisation d’un dico vide
# Le type “dictionnaire” étant un type “mutable”, il sera facile de rajouter des infos dedans :
mon_dico['first_name'] = 'André'  # Si la clé n'existe pas …
mon_dico['last_name'] = 'NUYENS'
mon_dico['age'] = 25

print(mon_dico)                   # {'first_name': 'André', 'last_name': 'NUYENS', 'age': 25}
print(mon_dico['first_name'])     # André
print(mon_dico.keys())            # dict_keys(['first_name', 'last_name', 'age'])
print(mon_dico.values())          # dict_values(['André', 'NUYENS', 25])
print(mon_dico.items())           # dict_items([('first_name', 'André'), ('last_name', 'NUYENS'), ('age', 25)])

# if 'first_name' in mon_dico:
#     del mon_dico['first_name']
# print(mon_dico['first_name'])     # KeyError: 'first_name'

for k in mon_dico.keys():
    print('La clé "{0}" à comme valeur "{1}"'.format(k, mon_dico[k]))


"""
    Un dictionnaire n'est pas mutable ???
    se renseigner sur le garbage collector
"""

# mon_dico2 = mon_dico         # les deux variables pointent vers la même adresse mémoire
mon_dico2 = mon_dico.copy()    # nous créons une vraie copie indépendante de la variable d'orignie

"""
    Parcours d’un dictionnaire
    Vous pouvez utiliser une boucle for pour traiter successivement tous les éléments contenus dans un dictionnaire, 
    mais attention :
        • au cours de l’itération, ce sont les clés qui seront utilisés ;
        • l’ordre des éléments qui sont traités est imprévisible.
"""
for k in mon_dico:
    print(k, mon_dico[k])
# Cette méthode n’est pas fort optimisée en termes de performances ou de lisibilité.
# Il est préférable de passer par la fonction items() :
for k, value in mon_dico.items():
    print(k, value)
