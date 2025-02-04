mon_ensemble_0 = set([1, 3, 5, 9, 2, 1])          # {1, 2, 3, 5, 9}
print(f"mon_ensemble_0 : {mon_ensemble_0}")

mon_ensemble_1 = set([5, 2, 4, 9, 8])
print(f"mon_ensemble_1 : {mon_ensemble_1}")       # {2, 4, 5, 8, 9}

mon_ensemble_2 = set(['b', 'e', 'a'])
print(f"mon_ensemble_2 : {mon_ensemble_2}")       # {'e', 'a', 'b'}

a = set([1, 3, 5, 9, 2, 1])
b = set([4, 1, 9, 5])

# Réunion
print(f"a | b : {a | b}")                      # {1, 2, 3, 4, 5, 9}

# Différence
print(f"a - b : {a - b}")                      # {2, 3}

# Intersection
print(f"a & b : {a & b}")                      # {1, 5, 9}

print(f"a == b : {a == b}")                    # False
print(f"a <= b : {a <= b}")                    # False
print(f"a >= b : {a >= b}")                    # False

c = set([0, 5, 10])
d = set([10, 0, 5])
print(f"c == d : {c == d}")                    # True
print(f"c <= d : {c <= d}")                    # True
print(f"c >= d : {c >= d}")                    # True

e = set([1, 5, 3, 4])
print(f"e : {e}")                              # {1, 3, 4, 5}g
# e.remove(7)                                    # KeyError: 7
if 7 in e:
    e.remove(7)
print(f"e : {e}")                              # {1, 3, 4, 5}
e.discard(7)
print(f"e : {e}")                              # {1, 3, 4, 5}
e.remove(5)
print(f"e : {e}")                              # {1, 3, 4}

# Les ensembles sont mutables, donc si on fait "f = e", ils pointent vers la même référence mémoire !
# Pour les copies, utiliser la méthode copy()
f = e.copy()
