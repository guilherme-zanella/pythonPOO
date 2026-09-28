from rich import print
from rich.panel import Panel

class Mensagem:

    def __init__(self, mensagem:str, tipo:str = 'mensagem', icone:str = ':speech_balloon:'):
        self._mensagem = mensagem
        self._tipo = tipo
        self._icone = icone

    def mostrar(self):

        self.painel = Panel(self._mensagem, title=f'{self._icone} {self._tipo.upper()} {self._icone}', style='white on black', width=50)

        print(self.painel)


class Alerta(Mensagem):
    def __init__(self, mensagem):
        super().__init__(mensagem, 'alerta', ':warning:')

    def mostrar(self):
    
        self.painel = Panel(self._mensagem, title=f'{self._icone} {self._tipo.upper()} {self._icone}', style='black on yellow1', width=50)

        print(self.painel)


class Erro(Mensagem):
    def __init__(self, mensagem):
        super().__init__(mensagem, 'erro', ':prohibited:')

    def mostrar(self):
    
        self.painel = Panel(self._mensagem, title=f'{self._icone} {self._tipo.upper()} {self._icone}', style='yellow on red1', width=50)

        print(self.painel)
        