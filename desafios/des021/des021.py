from rich import print

class Caneta:
    def __init__(self, cor = 'azul'):
        match cor.lower().strip():
            case 'azul':
                escolha = 'blue1'
            case 'vermelho' | 'vermelha':
                escolha = 'red1'
            case 'verde':
                escolha = 'green'
            case 'preto' | 'preta':
                escolha = 'black'
            case 'branco' | 'branca':
                escolha = 'white'
            case 'amarelo' | 'amarela':
                escolha = 'yellow'
            case _:
                escolha = 'white'

        self.cor = escolha
        self.tampada = True

    def destampar(self):
        self.tampada = False

    def tampar(self):
        self.tampada = True

    def escrever(self, texto):
        if self.tampada:
            print(f':prohibited: A [{self.cor}]caneta [/] está tampada! ', end='')
        else:
            print(f'[{self.cor}]{texto}[/]', end=' ')

    def pular_linha(self, num=1):
        for n in range(num+1):
            print()


c1 = Caneta('azul')
c2 = Caneta('vermelha')
c3 = Caneta('verde')

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever('Olá, tudo bem?')
c1.pular_linha(2)
c2.escrever('Olá, gafanhoto!')
c3.escrever('Vamos exercitar!')
