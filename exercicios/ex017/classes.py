class Numero:

    def __init__(self, valor: int|float = 0):
        self.numero = valor

    def dobrar(self):
        self.numero *= 2

    def __str__(self):
        return f'Tenho o valor {self.numero} dentro do Número'


class Texto:

    def __init__(self, texto: str = ''):
        self.texto = texto

    def dobrar(self):
        self.texto = f'{self.texto} {self.texto}'

    def __str__(self):
        return f'Tenho o texto "{self.texto}" dento da String'


class Lista:

    def __init__(self, lista: list = []):
        self.valores = lista

    def dobrar(self):
        self.valores = self.valores + self.valores

    def __str__(self):
        return f'Tenho a os valores {self.valores} dentro da Lista'


class Papel:

    def __init__(self):
        self.dobrado = False

    def dobrar(self):
        self.dobrado = True

    def __str__(self):
        return f'O papel está {'novo' if not self.dobrado else 'dobrado'}'


class Casa:

    def __init__(self):
        pass

    def __str__(self):
        return f'Era uma casa muito engraçada'


# duck typing

def tente_dobrar(objeto):
    try:
        objeto.dobrar()
    except:
        print(f'Tive dificuldades para dobrar {objeto.__class__.__name__}')
