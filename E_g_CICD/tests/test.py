# test_nom_de_votre_script.py

import unittest
from code import mul

class TestMulFunction(unittest.TestCase):

    def test_mul_positive_numbers(self):
        result = mul(3, 4)
        self.assertEqual(result, 12)

    def test_mul_negative_numbers(self):
        result = mul(-2, 5)
        self.assertEqual(result, -10)

    def test_mul_zero(self):
        result = mul(7, 0)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
