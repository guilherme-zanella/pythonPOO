from rich import print
from rich.panel import Panel

class Churrasco:
    def __init__(self, titulo, quantidade):
        self.titulo = titulo
        self.quantidade = quantidade

    def analisar(self):
        consumo_pad = 0.4
        custo_pad = 82.40
        consumo_tot = consumo_pad * self.quantidade
        custo_tot = consumo_tot * custo_pad
        custo_div = custo_tot / self.quantidade

        txt_analise = f'Analisando [green]{self.titulo}[/] com [blue1]{self.quantidade} convidados[/]'
        txt_padrao = f'Cada participante comerá {consumo_pad}Kg e cada Kg custa R${custo_pad:,.2f}'
        txt_kg = f'Recomendo [blue1]comprar {consumo_tot:.2f}Kg[/] de carne'
        txt_custo_tot = f'O custo total será de [green]R${custo_tot:,.2f}[/]'
        txt_custo_div = f'Cada pessoa pagará [yellow]R${custo_div:,.2f}[/] para participar.'

        caixa = Panel(f'{txt_analise}\n{txt_padrao}\n{txt_kg}\n{txt_custo_tot}\n{txt_custo_div}',title=self.titulo, width=70)
        return caixa


c1 = Churrasco('Churras dos Amigos', 15)
print(c1.analisar())

# 400g por pessoa
# R$82,40/Kg