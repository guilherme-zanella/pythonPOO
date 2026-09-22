from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, valor=0):
        self._valor = valor

    @property
    def fvalor(self):
        return f'R${self._valor:,.2f}'

    @abstractmethod
    def pagar(self):
        pass


class PIX(Pagamento):
    def pagar(self):
        print(f'Pagamento CONFIRMADO de {self.fvalor} via PIX')


class CartaoCredito(Pagamento):
    def pagar(self):
        print(f'Pagamento CONFIRMADO de {self.fvalor} via Cartão de Crédito')


class Boleto(Pagamento):
    def pagar(self):
        print(f'Pagamento CONFIRMADO de {self.fvalor} via Boleto')


def finalizar_compra(self, valor):
    try:
        self._valor = valor
        self.pagar()
    except:
        print(f'Ocorreu um erro na hora de fazer o pagamento!')
