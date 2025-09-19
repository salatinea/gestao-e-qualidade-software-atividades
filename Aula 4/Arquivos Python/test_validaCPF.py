import unittest
from validaCPF import validaCPF

class test_validaCPF(unittest.TestCase):
    def test_cpf_valido(self):
        self.assertTrue(validaCPF("12345678901"))

    def test_cpf_curto(self):
        self.assertFalse(validaCPF("12345"))

    def test_cpf_com_letras(self):
        self.assertFalse(validaCPF("12345abc901"))

    def test_cpf_vazio(self):
        self.assertFalse(validaCPF(""))