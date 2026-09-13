from rich import print

class Caneta:
    def __init__(self, cor):
        traducao = {
            'verde': 'green',
            'vermelha': 'red1',
            'azul': 'blue1',
            'preta': 'black',
            'branca': 'white',
            'amarela': 'yellow1'
        }
        self.cor = traducao[cor]
        self.tampada = True

    def destampar(self):
        self.tampada = False

    def tampar(self):
        self.tampada = True

    def escrever(self, texto):
        if self.tampada:
            print(f':prohibited: A [{self.cor}]caneta[/] está tampada! ', end='')
        else:
            print(f'[{self.cor}]{texto}[/]', end='')

    def pular_linha(self, num=1):
        for n in range(num+1):
            print()


c1 = Caneta('azul')
c2 = Caneta('vermelha')
c3 = Caneta('verde')

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever('Olá, tudo bem? ')
c1.pular_linha(2)
c2.escrever('Olá, gafanhoto! ')
c3.escrever('Vamos exercitar! ')
