from abc import ABC, abstractmethod
from math import pi

class Poligono(ABC):
    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self) -> float:
        pass

    @abstractmethod
    def area(self) -> float:
        pass


class Quadrado(Poligono):
    def __init__(self, lado=1):
        super().__init__(qtd_lados=4)
        self.lado = lado

    def __str__(self):
        return f'Um quadrado de lado {self.lado} tem:'

    def perimetro(self):
        return self.lado * 4

    def area(self):
        return self.lado ** 2


class Circulo(Poligono):
    def __init__(self, raio=1):
        super().__init__(1)
        self.raio = raio

    def __str__(self):
        return f'Um círculo de raio {self.raio} tem:'

    def perimetro(self):
        return self.raio * 2 * pi

    def area(self):
        return self.raio ** 2 * pi
