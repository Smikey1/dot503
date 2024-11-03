import unittest
from operation import add, subtract, multiply, divide, power, sqrt

class TestOperations(unittest.TestCase):

    def test_add(self):
        # Test addition
        self.assertEqual(add(10, 5), 15)  # Should pass
        self.assertEqual(add(-1, 1), 0)   # Should pass

    def test_subtract(self):
        # Test subtraction
        self.assertEqual(subtract(10, 5), 5)  # Should pass
        self.assertEqual(subtract(-1, -1), 0)  # Should pass

    def test_multiply(self):
        # Test multiplication
        self.assertEqual(multiply(3, 7), 21)  # Should pass
        self.assertEqual(multiply(5, -3), -15)  # Should pass

    def test_divide(self):
        # Test division
        self.assertEqual(divide(10, 2), 5)  # Should pass
        self.assertEqual(divide(10, 0), 'ZERO DIVISION Error (divide by zero)')  # Edge case, should pass

    def test_power(self):
        # Test power
        self.assertEqual(power(2, 3), 8)  # Should pass
        self.assertEqual(power(2, -1), 0.5)  # Should pass

    def test_sqrt(self):
        # Test square root
        self.assertAlmostEqual(sqrt(4), 2.0)  # Should pass, square root of 4 is 2
        self.assertAlmostEqual(sqrt(9), 3.0)  # Should pass, square root of 9 is 3
        self.assertAlmostEqual(sqrt(2), 1.41421356237, places=5)  # Should pass, square root of 2
        self.assertEqual(sqrt(0), 0)  # Edge case, sqrt(0) is 0

    def test_failed_add(self):
        # Failing test case for add function (intentional failure)
        self.assertEqual(add(2, 2), 5)  # Expected fail

    def test_failed_multiply(self):
        # Failing test case for multiply function (intentional failure)
        self.assertEqual(multiply(2, 6), 8)  # Expected fail

    def test_failed_divide(self):
        # Failing test case for divide function (intentional failure)
        self.assertEqual(divide(10, 2), 3)  # Expected fail

if __name__ == '__main__':
    unittest.main()
