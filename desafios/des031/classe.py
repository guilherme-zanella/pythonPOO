class Retangulo:
    def __init__(self, base=1, altura=1):
        self._base = base
        self._altura = altura
        self._area = None

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, a):
        if a < 0:
            raise ValueError('Valor para altura inválido!')
        else:
            self._altura = a

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, b):
        if b < 0:
            raise ValueError('Valor para base inválido!')
        else:
            self._base = b

    @property
    def area(self):
        self._area = self.base * self.altura
        return self._area

    @property
    def medidas(self):
        return f'Base = {self.base}\nAltura = {self.altura}\nÁrea = {self.area}'

    @medidas.setter
    def medidas(self, med):
        for i, n in enumerate(med):
            if n < 0:
                raise ValueError('Medidas inválidas!')
            elif i == 0:
                self.base = n
            elif i == 1:
                self.altura = n
            else:
                raise ValueError('Capotemo o corsa!')
