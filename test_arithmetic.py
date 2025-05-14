import unittest
import arithmetic

class TestArithmetic(unittest.TestCase):
    def test_add(self):
        self.assertEqual(arithmetic.add(2, 3), 5)
        self.assertEqual(arithmetic.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(arithmetic.subtract(5, 2), 3)
        self.assertEqual(arithmetic.subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(arithmetic.multiply(3, 4), 12)
        self.assertEqual(arithmetic.multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(arithmetic.divide(10, 2), 5)
        with self.assertRaises(ZeroDivisionError):
            arithmetic.divide(1, 0)

if __name__ == "__main__":
    unittest.main()
