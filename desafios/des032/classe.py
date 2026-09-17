

class ContaBancaria:
    def __init__(self, id, nome, saldo=0):
        self._id = id
        self._titular = nome
        self.__saldo = saldo

    @property
    def nome(self):
        return self._titular

    @nome.setter
    def nome(self, nome):
        self._titular = nome

    def sacar(self, valor):
        if valor <= self.__saldo and valor > 0:
            self.__saldo -= valor
            print(f'Saque de R${valor:.2f}. Autorizado na conta {self._id}')
        else:
            raise ValueError('Não pode fazer saques com valores negativos ou maiores que o saldo!')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f'Depósito de R${valor:.2f}. Autorizado na conta {self._id}')
        else:
            raise ValueError('Não pode fazer saques com valores negativos ou maiores que o saldo!')
