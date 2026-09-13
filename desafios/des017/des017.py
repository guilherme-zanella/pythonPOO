from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        caixa = Panel(f'{self.nome:^30}\n{'—'*30}\n{f' R${self.preco:,.2f} '.center(30,'.')}', title='Produto', width=34)
        return caixa

p1 = Produto('Iphone 17 Pro Max', 25000.80)
p2 = Produto('Notebook Games', 8000)

print(p1.etiqueta())
print(p2.etiqueta())