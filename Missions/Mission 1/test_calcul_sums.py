from calcul_sums import calculate_sums

# # Calcul de la somme attendue pour comparaison
# expected_sum = sum([i**2 for i in range(1, 11)])
#
# # Test 1 : Vérifier la valeur finale de sum_1
# sum_1, sum_2 = calculate_sums()
# if sum_1 == expected_sum:
#     print("Test 1 réussi : sum_1 est correct.")
# else:
#     print(f"Test 1 échoué : sum_1 est {sum_1}, attendu {expected_sum}.")
#
# # Test 2 : Vérifier la valeur finale de sum_2
# if sum_2 == expected_sum:
#     print("Test 2 réussi : sum_2 est correct.")
# else:
#     print(f"Test 2 échoué : sum_2 est {sum_2}, attendu {expected_sum}.")
#
# # Test 3 : Vérifier que sum_1 et sum_2 sont égaux
# if sum_1 == sum_2:
#     print("Test 3 réussi : sum_1 et sum_2 sont égaux.")
# else:
#     print(f"Test 3 échoué : sum_1 est {sum_1}, sum_2 est {sum_2}.")



def test_calculate_sums():
    # Test 1: Basic Functionality
    expected_sum_1, expected_sum_2 = 385, 385
    actual_sum_1, actual_sum_2 = calculate_sums('A partir du fichier : "test_calcul_sums"')
    assert actual_sum_1 == expected_sum_1 and actual_sum_2 == expected_sum_2, "Basic functionality test failed"

    # # Test 2: Edge Case (Single Iteration)
    # # Modify the function to run only one iteration
    # def modified_calculate_sums():
    #     sum_1 = 0
    #     sum_2 = 0
    #     i = 1
    #
    #     while i <= 1:  # Modified condition
    #         i_squared = i**2
    #         sum_1 += i_squared
    #         sum_2 = i * (i + 1) * (2 * i + 1) // 6
    #         i += 1
    #
    #     return sum_1, sum_2
    #
    # expected_sum_1, expected_sum_2 = 1, 1
    # actual_sum_1, actual_sum_2 = modified_calculate_sums()
    # assert actual_sum_1 == expected_sum_1 and actual_sum_2 == expected_sum_2, "Edge case test failed"

# Run the tests
test_calculate_sums()