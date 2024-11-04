
from median_calculator import numbers_list, sorted_list, median

# Test 1 : Vérifier le contenu initial de `numbers_list`
expected_numbers_list = [10, 2, 4, 8, 6]
# expected_numbers_list = [10, 2, 4, 8, 6, 7, 12]
if numbers_list == expected_numbers_list:
    print("Test 1 réussi : numbers_list est correct.")
else:
    print(f"Test 1 échoué : numbers_list est {numbers_list}, attendu {expected_numbers_list}.")

# Test 2 : Vérifier que `sorted_list` est bien triée
expected_sorted_list = sorted(expected_numbers_list)
if sorted_list == expected_sorted_list:
    print("Test 2 réussi : sorted_list est correcte.")
else:
    print(f"Test 2 échoué : sorted_list est {sorted_list}, attendu {expected_sorted_list}.")

# Test 3 : Vérifier que la médiane est correcte
# Pour une liste triée [2, 4, 6, 8, 10], la médiane est le 3e élément, soit 6
expected_median = 6
# Pour une liste triée [2, 4, 6, 7, 8, 10, 12], la médiane est le 4e élément, soit 7
# expected_median = 7
if median == expected_median:
    print("Test 3 réussi : La médiane est correcte.")
else:
    print(f"Test 3 échoué : median est {median}, attendu {expected_median}.")