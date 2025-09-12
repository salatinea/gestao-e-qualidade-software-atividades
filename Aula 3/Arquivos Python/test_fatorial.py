import unittest
from fatorial import fatorial

class TestFatorial(unittest.TestCase):

    def test_fatorial_zero(self):
        self.assertEqual(fatorial(0), 1)

    def test_fatorial_positivo(self):
        self.assertEqual(fatorial(5), 120)

    def test_fatorial_negativo(self):
        with self.assertRaises(ValueError):
            fatorial(-1)

if __name__ == "__main__":
    unittest.main()