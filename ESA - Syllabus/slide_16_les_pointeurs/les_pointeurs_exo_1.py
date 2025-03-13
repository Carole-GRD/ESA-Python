"""
    Exercice 1 :

    Reprenez les dias précédentes en utilisant, cette fois-ci, un frozenset
        ● à votre avis, quelle est la principale différence entre les deux ?
        ● faites un schéma expliquant comment cela se déroule.
"""

# a = set()
# a.add(9)
# b = a
# b.add(2)
# c = b
# print(f'a : {a}')
# print(f'b : {b}')
# print(f'c : {c}')
#
# a = set()
# a.update([9, 2, 4])
# print(f'a : {a}')
# print(f'b : {b}')
# print(f'c : {c}')

# a = frozenset()
# a.add(9)   # AttributeError: 'frozenset' object has no attribute 'add'


# Les tuples sont immutables !

# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)
# tuple1 = ({'nom': 'Carole', 'numero': 6}, {'nom': 'Jesse', 'numero': 19})
# tuple2 = ({'nom': 'Andy', 'numero': 16}, {'nom': 'Geoffrey', 'numero': 3})

tuple1 = ({'nom': 'Carole', 'numero': 6},)
tuple2 = ({'nom': 'Jesse', 'numero': 19},)
tuple3 = ({'nom': 'Andy', 'numero': 16},)
tuple4 = ({'nom': 'Geoffrey', 'numero': 3},)

tuple5 = tuple1 + tuple2 + tuple3 + tuple4
print(tuple5)

index = tuple5.index({'nom': 'Andy', 'numero': 16})
print(index)
tuple5 = tuple5[:index] + tuple5[index+1:]
print(tuple5)

# tuple5 = tuple(dico for dico in tuple5 if dico != {'nom': 'Andy', 'numero': 16})
# print(tuple5)
