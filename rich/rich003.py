from rich import print
from rich.table import Table

tabela = Table(title='Tabela de preços', style='black bold', title_style='red1 bold', title_justify='left')

tabela.add_column('Produto', justify='left', width=15, style='yellow bold')
tabela.add_column('Preço', justify='center', width=10, style='green1')

tabela.add_row('Banana', 'R$4.20')
tabela.add_row('Maçã', 'R$2.30')
tabela.add_row('Maracujá', 'R$12.50')
tabela.add_row('Pera', 'R$5.70')

print(tabela)