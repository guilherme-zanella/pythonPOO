from rich import print
from rich.panel import Panel

class ControleRemoto:
    max_canal = 5
    min_canal = 1
    max_volume = 5
    min_volume = 0
    def __init__(self, canal=1, volume=2):
        self.canal:int = canal
        self.volume:int = volume
        self.ligada:bool = False   

    def liga_desliga(self) -> bool:
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def avancar_canal(self) -> int:
        if self.ligada:
            if self.canal == ControleRemoto.max_canal:
                self.canal = ControleRemoto.min_canal
            else:
                self.canal += 1

    def voltar_canal(self) -> int:
        if self.ligada:
            if self.canal == ControleRemoto.min_canal:
                self.canal = ControleRemoto.max_canal
            else:
                self.canal -= 1

    def aumentar_volume(self) -> int:
        if self.ligada:
            if self.volume != ControleRemoto.max_volume:
                self.volume += 1

    def diminuir_volume(self) -> int:
        if self.ligada:
            if self.volume != ControleRemoto.min_volume:
                self.volume -= 1

    def tv(self):
        if self.ligada:
            conteudo = ('Canal  =')
            for c in range(ControleRemoto.min_canal, ControleRemoto.max_canal+1):
                conteudo += f' {c} ' if self.canal != c else f' [white on yellow] {c} [/] '

            conteudo += '\nVolume = '
            for v in range(ControleRemoto.min_volume+1, ControleRemoto.max_volume+1):
                conteudo += f'[white on blue1] [/]' if v <= self.volume else f'[white on black] [/]'  
        else:
            conteudo = ':prohibited: [red1]A TV está desligada[/]'

        tela = Panel(conteudo, title='[ TV ]', width=30)
        print(tela)


controle = ControleRemoto()
while True:
    controle.tv()
    comando =input(f'< CH{controle.canal} >  - VOL{controle.volume} + ')
    match comando:
        case '0':
            break
        case '@':
            controle.liga_desliga()
        case '<':
            controle.voltar_canal()
        case '>':
            controle.avancar_canal()
        case '-':
            controle.diminuir_volume()
        case '+':
            controle.aumentar_volume()
    print('\n'*10)
        