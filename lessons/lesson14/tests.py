import unittest

from .funk import quadratic


class TestQuadratic(unittest.TestCase):

    def test_two_real_roots(self):
        actual = quadratic(1, -3, 2)

        self.assertEqual(actual, (2, 1))

    def test_one_real_root(self):
        actual = quadratic(1, -2, 1)
        self.assertEqual(actual, 1)

    # def test_no_real_roots(self):
    #     actual = quadratic(1, 0, 1)
    #     self.assertIsNone(actual)
    #     self.assertEqual(actual, None)
    # def test_not_valid_real_roots(self):
    #     actual = quadratic(1, 0, 2)
    #     self.assertIsNone(actual)
    #     self.assertEqual(actual, 1, "No real roots")


if __name__ == "__main__":
    unittest.main()
