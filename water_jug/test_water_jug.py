# water_jug/test_water_jug.py
import unittest
from .simulation import solve_water_jug
from .diophantine import solve_diophantine

class TestWaterJug(unittest.TestCase):
    def test_simple_cases(self):
        self.assertEqual(len(solve_water_jug(3, 5, 4)), 6)
        self.assertEqual(solve_diophantine(3, 5, 4), 6)

    def test_impossible_cases(self):
        self.assertEqual(solve_water_jug(2, 4, 5), "No solution exists")
        self.assertIsNone(solve_diophantine(2, 4, 5))

    def test_large_numbers(self):
        self.assertIsInstance(solve_water_jug(999, 1000, 1), list)
        self.assertEqual(solve_diophantine(999, 1000, 1), 1000)

    def test_equal_jugs(self):
        self.assertEqual(solve_water_jug(5, 5, 5), ["Fill A"])
        self.assertEqual(solve_diophantine(5, 5, 5), 1)

    def test_prime_numbers(self):
        self.assertIsInstance(solve_water_jug(17, 23, 8), list)
        self.assertIsNotNone(solve_diophantine(17, 23, 8))

    def test_large_target(self):
        self.assertIsInstance(solve_water_jug(7, 11, 66), list)
        self.assertIsNotNone(solve_diophantine(7, 11, 66))

    def test_coprime_jugs(self):
        self.assertIsInstance(solve_water_jug(25, 36, 1), list)
        self.assertIsNotNone(solve_diophantine(25, 36, 1))

if __name__ == '__main__':
    unittest.main()