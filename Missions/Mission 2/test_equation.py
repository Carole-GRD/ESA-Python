import unittest

from equation import find_power_solutions

class TestPowerEquations(unittest.TestCase):

    def test_simple_case(self):
        # Test avec l'équation x^2 + y^2 = z^2 (triangle pythagoricien) avec max_val = 5
        solutions, count = find_power_solutions(2, 2, 2, 5)
        self.assertEqual(count, 2)
        expected_solutions = [(3, 4, 5), (4, 3, 5)]
        self.assertEqual(set(solutions), set(expected_solutions))

    def test_no_solution(self):
        # Test avec une équation sans solution : x^3 + y^3 = z^2, max_val = 2
        solutions, count = find_power_solutions(3, 3, 2, 2)
        self.assertEqual(count, 0)
        self.assertEqual(solutions, [])

    def test_small_numbers(self):
        # Test avec l'équation x^1 + y^1 = z^1, max_val = 2
        solutions, count = find_power_solutions(1, 1, 1, 2)
        expected_solutions = [(1, 1, 2)]
        self.assertEqual(count, len(expected_solutions))
        self.assertEqual(set(solutions), set(expected_solutions))

    def test_max_value_boundary(self):
        # Test avec max_val = 1
        solutions, count\
            = find_power_solutions(1, 1, 1, 1)
        self.assertEqual(count, 0)  # Car 1 + 1 ≠ 1
        self.assertEqual(solutions, [])

    def test_different_powers(self):
        # Test avec des puissances différentes : x^2 + y^1 = z^1, max_val = 3
        solutions, count = find_power_solutions(2, 1, 1, 3)
        expected_solutions = [(1, 1, 2), (1, 2, 3)]
        self.assertEqual(count, len(expected_solutions))
        self.assertEqual(set(solutions), set(expected_solutions))

    def test_higher_powers(self):
        # Test avec des puissances plus élevées : x^3 + y^3 = z^3, max_val = 5
        solutions, count = find_power_solutions(3, 3, 3, 5)
        self.assertEqual(count, 0)  # Selon le théorème de Fermat pour n=3
        self.assertEqual(solutions, [])

    def test_zero_power(self):
        # Test avec une puissance nulle : x^0 + y^1 = z^1, max_val = 3
        solutions, count = find_power_solutions(0, 1, 1, 3)
        # x^0 = 1 pour tout x, donc l'équation devient 1 + y = z
        expected_solutions = [(1, 1, 2), (1, 2, 3), (2, 1, 2), (2, 2, 3), (3, 1, 2), (3, 2, 3)]
        self.assertEqual(count, len(expected_solutions))
        self.assertEqual(set(solutions), set(expected_solutions))


if __name__ == '__main__':
    unittest.main()