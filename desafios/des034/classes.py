from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome: str = 'Funcionário', salario: int|float = 1621):
        self.nome = nome
        self.__salario = 1621
        self.salario = salario

    def __str__(self):
        return f'{self.nome} ganha R${self.salario:,.2f} e por ser {self.__class__.__name__} o bônus será de R${self.calcular_bonus():,.2f}'

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self,valor):
        if valor > self.__salario:
            self.__salario = valor
        else:
            print(f'Você não pode abaixar o salario de um funcionário')

    @abstractmethod
    def calcular_bonus(self):
        pass


class Gerente(Funcionario):
    def calcular_bonus(self):
        return self.salario * 15 / 100


class Desenvolvedor(Funcionario):
    def calcular_bonus(self):
        return self.salario * 10 / 100


class Design(Funcionario):
    def calcular_bonus(self):
        return self.salario * 8 / 100
