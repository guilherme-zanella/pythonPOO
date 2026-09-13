from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
         return f'{self.nome} custa R${self.preco:,.2f}'

    def etiqueta(self):
        conteudo = f'{self.nome:^30}'
        conteudo += f'{'—'*30}'
        conteudo += f'R${self.preco:,.2f} '.center(30, '.')

        caixa = Panel(conteudo, title='Produto', width=34)
        return caixa

p1 = Produto('Iphone 17 Pro Max', 25_000.80)
p2 = Produto('Notebook Games', 8_000)

print(p1.etiqueta())
print(p2.etiqueta())