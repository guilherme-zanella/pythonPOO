class Termostato:
    def __init__(self):
        self.__temperatura = 24

    @property
    def temperatura(self):
        return f'{self.__temperatura}°C'

    @temperatura.setter
    def temperatura(self, valor):
        if valor <= 16:
            self.__temperatura = 16
        elif valor >= 30:
            self.__temperatura = 30
        else:
            n = 16
            while n <=30:
                if valor == n:
                    self.__temperatura = valor
                    break
                n += 0.5
            else:
                print(f'Temperatura de {valor}°C é inválida!')
