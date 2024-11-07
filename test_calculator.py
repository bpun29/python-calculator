import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add1(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:

    def test_add2(self):
        self.assertEqual(self.calc.add(1, 7), 8)
    
    def test_subtract1(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)
    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)

    def test_multiply1(self):
        self.assertEqual(self.calc.multiply(1, 2), 2)
    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(6, 3), 18)

    def test_divide1(self):
        self.assertEqual(self.calc.divide(8, 2), 4)
    def test_divide2(self):
        self.assertEqual(self.calc.divide(12, 4), 3)

    def test_modulo1(self):
        self.assertEqual(self.calc.modulo(6, 2), 0)
    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(9, 4), 1)

if __name__ == '__main__':
    unittest.main()

