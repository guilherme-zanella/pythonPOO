from abc import abstractmethod, ABC
from rich.panel import Panel
from rich import print

class Funcionario(ABC):
    sal_min = 1612
    inss = 7.5
    def __init__(self, nome):
        self.nome = nome
        self.salario = 0
        self.qtd_sal_min = 0

    @abstractmethod
    def calcular_salario(self):
        pass

    def analisar_salario(self):
        conteudo = f'O salário de [blue]{self.nome}[/] ([blue1]Funcionário: {self.__class__.__name__}[/]) é de [green]R${self.salario:.2f}[/] e corresponde a [yellow]{self.qtd_sal_min} salários mínimos[/].'
        painel = Panel(conteudo, title='Análise de funcionário', width=55)
        print(painel)


class Horista(Funcionario):
    def __init__(self, nome, valor_hora, horas_trab):
        super().__init__(nome)
        self.sal_bruto = valor_hora * horas_trab

    def calcular_salario(self):
        self.salario = self.sal_bruto - (self.sal_bruto * self.inss / 100)
        self.qtd_sal_min = self.salario / self.sal_min
        self.qtd_sal_min = round(self.qtd_sal_min, 1)


class Mensalista(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome)
        self.sal_bruto = salario

    def calcular_salario(self):
        self.salario = self.sal_bruto - (self.sal_bruto * self.inss / 100)
        self.qtd_sal_min = self.salario / self.sal_min
        self.qtd_sal_min = round(self.qtd_sal_min, 1)
    