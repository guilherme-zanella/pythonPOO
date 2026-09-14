from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia

    @abstractmethod
    def calcular_frete(self):
        pass


class Moto(Transporte):
    fator = 0.50
    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        return f'R${self.distancia * self.fator:,.2f}'.replace('.', ',')


class Caminhao(Transporte):
    fator = 1.20
    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        if self.distancia < 50:
            return 'Raio mínimo de 50Km'
        else:
            return f'R${self.distancia * self.fator:,.2f}'.replace('.', ',')


class Drone(Transporte):
    fator = 9.50
    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        if self.distancia > 10:
            return 'Raio máximo de 10Km'
        else:
            return f'R${self.distancia * self.fator:.2f}'.replace('.', ',')
        