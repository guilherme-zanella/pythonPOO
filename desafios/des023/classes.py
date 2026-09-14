from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligono):
    def __init__(self, lado):
        super().__init__(qtd_lados=4)
        self.lado = lado

    def __str__(self):
        return f'Um quadrado de lado {self.lado} tem:'

    def perimetro(self):
        return f'[blue]{self.qtd_lados * self.lado:.1f}[/]'

    def area(self):
        return f'[blue]{self.lado ** 2:.1f}[/]'


class Circulo(Poligono):
    def __init__(self, raio):
        super().__init__(qtd_lados=1)
        self.raio = raio

    def __str__(self):
        return f'Um círculo de raio {self.raio} tem:'

    def perimetro(self):
        return f'[blue]{self.raio * 2 * 3.14:.1f}[/]'

    def area(self):
        return f'[blue]{self.raio ** 2 * 3.14:.1f}[/]'
