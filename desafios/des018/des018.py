from rich import print
from rich.panel import Panel

class Churrasco:
    
    consumo_pad:float = 0.400
    custo_pad:float = 82.40

    def __init__(self, titulo, quantidade):
        self.titulo = titulo
        self.quantidade = quantidade

    def __str__(self) -> str:
        return f'Esse é o {self.titulo} com {self.quantidade} convidados'

    def calc_consumo_total(self) -> float:
        return Churrasco.consumo_pad * self.quantidade

    def calc_custo_total(self) -> float:
        return self.calc_consumo_total() * Churrasco.custo_pad

    def calc_custo_dividido(self) -> float:
        return self.calc_custo_total() / self.quantidade

    def analisar(self):
        conteudo = f'Analisando [green]{self.titulo}[/] com [blue1]{self.quantidade} convidados[/]\n'
        conteudo += f'Cada participante comerá {Churrasco.consumo_pad}Kg e cada Kg custa R${Churrasco.custo_pad:,.2f}\n'
        conteudo += f'Recomendo [blue1]comprar {self.calc_consumo_total():.2f}Kg[/] de carne\n'
        conteudo += f'O custo total será de [green]R${self.calc_custo_total():,.2f}[/]\n'
        conteudo += f'Cada pessoa pagará [yellow]R${self.calc_custo_dividido():,.2f}[/] para participar.'

        painel = Panel(conteudo,title=self.titulo, width=70)
        return painel


c1 = Churrasco('Churras dos Amigos', 15)
print(c1.analisar())

# 400g por pessoa
# R$82,40/Kg