class Retangulo:
    def __init__(self, base=1, altura=1):
        self._base = None
        self._altura = None
        self._area = None
        self.base = base
        self.altura = altura

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        if isinstance(valor, float) or isinstance(valor, int):
            if valor < 1:
                raise ValueError('Valor para altura inválido!')
            else:
                self._altura = valor
        else:
            raise ValueError('O valor da altura deve ser um número')

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, valor):
        if isinstance(valor, float) or isinstance(valor, int):
            if valor < 1:
                raise ValueError('Valor para base inválido!')
            else:
                self._base = valor
        else:
            raise ValueError('O valor da base deve ser um número')

    @property
    def area(self):
        self._area = self.base * self.altura
        return self._area

    @area.setter
    def area(self):
        raise PermissionError('Você não pode mexer na área.')

    @property
    def medidas(self):
        return f'Base = {self.base}\nAltura = {self.altura}\nÁrea = {self.area}'

    @medidas.setter
    def medidas(self, med):
        if not isinstance(med, tuple):
            raise ValueError('Os valores de medida devem ser informados dentro de uma tupla!')
        elif len(med) != 2:
            raise ValueError('A tupla deve conter apenas duas medidas (base, altura)')
        else:
            for i, n in enumerate(med):
                if n < 0 or isinstance(n, str):
                    raise ValueError('Medidas inválidas!')
                elif i == 0:
                    self.base = n
                elif i == 1:
                    self.altura = n
                else:
                    raise ValueError('Capotemo o corsa!')

