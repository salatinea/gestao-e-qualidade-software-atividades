import unittest
from conta import Conta, InsufficientFunds

class TestConta(unittest.TestCase):

    def test_deposito_valido(self):
        conta = Conta()
        conta.depositar(100)
        self.assertEqual(conta.saldo, 100)

    def test_saque_com_sucesso(self):
        conta = Conta(200)
        conta.sacar(50)
        self.assertEqual(conta.saldo, 150)

    def test_saque_insuficiente(self):
        conta = Conta(100)
        with self.assertRaises(InsufficientFunds):
            conta.sacar(200)

    def test_deposito_invalido(self):
        conta = Conta()
        with self.assertRaises(ValueError):
            conta.depositar(-50)

    def test_saque_invalido(self):
        conta = Conta(100)
        with self.assertRaises(ValueError):
            conta.sacar(-20)

    def test_saldo_inicial_invalido(self):
        with self.assertRaises(ValueError):
            Conta(-100)

if __name__ == "__main__":
    unittest.main()
