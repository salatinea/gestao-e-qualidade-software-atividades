import unittest
from par import is_par

class TestPar(unittest.TestCase):

    def test_numero_par(self):
        self.assertTrue(is_par(4))
        self.assertTrue(is_par(100))

    def test_numero_impar(self):
        self.assertFalse(is_par(3))
        self.assertFalse(is_par(99))

    def test_zero(self):
        self.assertTrue(is_par(0))

    def test_numero_negativo(self):
        self.assertTrue(is_par(-8)) 
        self.assertFalse(is_par(-7))  

if __name__ == "__main__":
    unittest.main()