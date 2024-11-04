
import unittest

from equation_simple import find_linear_solutions


class TestFindLinearSolutions(unittest.TestCase):

    def test_simple_solution(self):
        # Test avec une équation simple : x + y = 5, max = 5
        solutions, count = find_linear_solutions(1, 1, 5, 5)
        self.assertEqual(count, 4)
        # self.assertIn((1, 4), solutions)
        # self.assertIn((2, 3), solutions)
        # self.assertIn((3, 2), solutions)
        # self.assertIn((4, 1), solutions)
        self.assertEqual(solutions, [(1, 4), (2, 3), (3, 2), (4, 1)])
        # expected_solutions = [(1, 4), (2, 3), (3, 2), (4, 1)]
        # self.assertEqual(count, len(expected_solutions))
        # for sol in expected_solutions:
        #     self.assertIn(sol, solutions)

    def test_no_solution(self):
        # Test avec une équation sans solution : 2x + 2y = 3, max = 5
        # ----------------
        # solutions, count = find_linear_solutions(2, 2, 3, 5)
        # self.assertEqual(count, 0)
        # self.assertEqual(solutions, [])
        # ----------------
        # OU BIEN, en une seule ligne !
        self.assertEqual(find_linear_solutions(2, 2, 3, 5), ([], 0))


    def test_single_solution(self):
        # Test avec une équation ayant une seule solution : 2x + 2y = 4, max = 5
        solutions, count = find_linear_solutions(2, 2, 4, 5)
        self.assertEqual(count, 1)
        # self.assertIn((1, 1), solutions)
        self.assertEqual(solutions, [(1, 1)])

    def test_max_value_boundary(self):
        # Test avec max_v = 1 pour x + y = 2
        solutions, count = find_linear_solutions(1, 1, 2, 1)
        self.assertEqual(count, 1)  # Il y a une solution (1,1)
        self.assertIn((1, 1), solutions)

    def test_negative_coefficients(self):
        # Test avec des coefficients négatifs : -x + y = 1, max = 3
        # solutions, count = find_linear_solutions(-1, 1, 1, 3)
        # expected_solutions = [(1, 2), (2, 3)]
        # self.assertEqual(count, len(expected_solutions))
        # for sol in expected_solutions:
        #     self.assertIn(sol, solutions)
        # ----------------
        # OU BIEN
        # self.assertEqual(find_linear_solutions(1, -1, 0, 10), ([(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], 10))
        self.assertEqual(find_linear_solutions(1, -1, 0, 10), ([(i, i) for i in range(1, 11)], 10))

    def test_zero_coefficient(self):
        # Test avec un coefficient nul : 0x + y = 2, max = 3
        solutions, count = find_linear_solutions(0, 1, 2, 3)
        self.assertEqual(count, 3)  # Une solution pour chaque x de 1 à 3, avec y=2
        expected_solutions = [(1, 2), (2, 2), (3, 2)]
        self.assertEqual(set(solutions), set(expected_solutions))
        #  set() compare les listes en tant qu'ensembles, donc sans tenir compte de l'ordre

    # # Test pour s'assurer qu'une ValueError est levée pour des types incorrects
    # def test_error_handling_type(self):
    #     with self.assertRaises(ValueError):
    #         find_linear_solutions("a", 1, 2, 3)
    #
    # # Test pour s'assurer qu'une ValueError est levée si max_v est négatif
    # def test_error_handling_negative_max_v(self):
    #     with self.assertRaises(ValueError):
    #         find_linear_solutions(1, 1, 5, -5)

if __name__ == '__main__':
    unittest.main()