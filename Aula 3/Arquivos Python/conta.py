class InsufficientFunds(Exception):
       pass

class Conta:
    def __init__(self, saldo_inicial: float = 0.0):
        if saldo_inicial < 0:
            raise ValueError("Saldo inicial não pode ser negativo.")
        self.saldo = saldo_inicial

    def depositar(self, amount: float):
        if amount <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self.saldo += amount

    def sacar(self, amount: float):
        if amount <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if amount > self.saldo:
            raise InsufficientFunds("Saldo insuficiente para o saque.")
        self.saldo -= amount
