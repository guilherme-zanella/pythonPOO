from rich import print
from rich import inspect

class ContaBancaria:
    """
        Cria uma conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, id, nome, saldo=0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f'Conta {self.id} criada com sucesso. Saldo disponível: R${self.saldo:,.2f}')

    def __str__(self):
        return f'A conta {self.id} de {self.titular} tem o saldo de R${self.saldo:,.2f}'

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'R${valor:,.2f} sacado, Saldo disponível: R${self.saldo:,.2f}')
        else:
            print(f'ERRO, Saldo insuficiente.')

    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito de R${valor:,.2f} feito com sucesso.')


c = ContaBancaria('22', 'Guilherme', 5000)
inspect(c)
