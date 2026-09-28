from abc import ABC, abstractmethod
import locale

class Pagamento(ABC):
    def __init__(self):
        self._valor = None

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        if valor > 0:
            self._valor = valor
        else:
            raise ValueError('Não pode fazer pagamentos com valores negativos')

    @property
    def fvalor(self):
        # return f'R${self._valor:,.2f}'
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        return locale.currency(self.valor, grouping=True, symbol=True, international=False)

    @abstractmethod
    def pagar(self):
        pass


class PIX(Pagamento):
    def pagar(self, valor):
        self.valor = valor
        return f'Pagamento CONFIRMADO de {self.fvalor} via PIX'


class CartaoCredito(Pagamento):
    def pagar(self, valor):
        self.valor = valor
        return f'Pagamento CONFIRMADO de {self.fvalor} via Cartão de Crédito'


class Boleto(Pagamento):
    def pagar(self, valor):
        self.valor = valor
        return f'Pagamento CONFIRMADO de {self.fvalor} via Boleto'


def finalizar_pagamento(p, valor):
    try:
        print(p.pagar(valor))
    except:
        print(f'Ocorreu um erro na hora de fazer o pagamento!')
