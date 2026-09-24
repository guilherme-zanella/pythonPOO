from rich import print
from rich.panel import Panel

class Mensagem:

    def __init__(self, mensagem:str):
        self.mensagem = mensagem
        self.tipo = 'mensagem'
        self.icone = '💬'

    def mostrar(self):

        self.painel = Panel(self.mensagem, title=f'{self.icone} AVISO {self.icone}', style='white on black', width=40)

        print(self.painel)


class Alerta(Mensagem):
    def __init__(self, mensagem):
        super().__init__(mensagem)
        self.tipo = 'alerta'
        self.icone = '🔺'

    def mostrar(self):
    
        self.painel = Panel(self.mensagem, title=f'{self.icone} AVISO {self.icone}', style='black on yellow1', width=40)

        print(self.painel)


class Erro(Mensagem):
    def __init__(self, mensagem):
        super().__init__(mensagem)
        self.tipo = 'alerta'
        self.icone = ':prohibited:'

    def mostrar(self):
    
        self.painel = Panel(self.mensagem, title=f'{self.icone} AVISO {self.icone}', style='yellow on red1', width=40)

        print(self.painel)
        