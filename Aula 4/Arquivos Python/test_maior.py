import unittest
from maior import maior

class test_maior(unittest.TestCase):

    def test_maior_primeiro(self):
        self.assertEqual(maior(10, 5), 10)

    def test_maior_segundo(self):
        self.assertEqual(maior(3, 7), 7)

    def test_iguais(self):
        self.assertEqual(maior(4, 4), 4)