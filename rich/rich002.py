from rich import print
from rich.panel import Panel

caixa = Panel('[white]Esse aqui é um painel de exemplo[/] :+1:', title='Mensagem', style='red1', title_align='left', width=35)

print(caixa)