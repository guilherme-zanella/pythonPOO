
class ContaBancaria:
    """
        Cria uma conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, id, nome, saldo=0):
        self.id = id # publico (+)
        self._titular = nome # protegido (#)
        self.__saldo = saldo # privado (-)
        print(f'Conta {self.id} criada com sucesso. Saldo disponível: R${self.__saldo:,.2f}')

    def __str__(self):
        # return f'A conta {self.id} de {self._titular} tem o saldo de R${self.__saldo:,.2f}'
        return f'Estado atual da conta: {self.__dict__}'

    def sacar(self, valor):
        valor = abs(valor)
        if valor <= self.__saldo:
            self.__saldo -= valor
            print(f'R${valor:,.2f} sacado, Saldo disponível: R${self.__saldo:,.2f}')
        else:
            print(f'ERRO, Saldo insuficiente.')

    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f'Depósito de R${valor:,.2f} feito com sucesso.')

 
