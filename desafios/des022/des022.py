from rich import print
from rich.panel import Panel

class ControleRemoto:
    def __init__(self):
        self.canal = 1
        self.volume = 2
        self.ligada = False

    def click(self, botao):
        if botao == '@':
            if self.ligada:
                self.ligada = False
            else:
                self.ligada = True

        if self.ligada:
            if botao == '-':
                if self.volume == 0:
                    pass
                else:
                    self.volume -= 1

            if botao == '+':
                if self.volume == 5:
                    pass
                else:
                    self.volume += 1

            if botao == '<':
                if self.canal == 1:
                    self.canal = 5
                else:
                    self.canal -= 1

            if botao == '>':
                if self.canal == 5:
                    self.canal = 1
                else:
                    self.canal += 1

    def tv(self):
        if self.ligada:
            conteudo = ('Canal  =')
            for c in range(1, 6):
                conteudo += f' {c} ' if self.canal != c else f' [white on yellow] {c} [/] '

            conteudo += '\nVolume = '
            for v in range(1, 6):
                conteudo += f'[white on blue1] [/]' if v <= self.volume else f'[white on black] [/]'  
        else:
            conteudo = ':prohibited: [red1]A TV está desligada[/]'

        tela = Panel(conteudo, title='[ TV ]', width=30)
        print(tela)

controle = ControleRemoto()
while True:
    controle.tv()
    botao = input(f'< CH{controle.canal} >  - VOL{controle.volume} + ')
    if botao == '0':
        break
    controle.click(botao)
    
        