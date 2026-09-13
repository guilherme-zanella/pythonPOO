from rich import print
from rich import inspect

class Funcionario:
    # atributo de classe
    empresa = 'Curso em Vídeo'

    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo  

    def apresentacao(self) -> str: # indico que a função retorna uma string
        return f':handshake: Olá, sou [blue1]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {Funcionario.empresa}'


Funcionario.empresa = 'NETFLIX'

f1 = Funcionario('Maria', 'Administração', 'Diretora')
f2 = Funcionario('Pedro', 'TI', 'Programador')

print(f1.apresentacao())
print(f2.apresentacao())
# inspect(f1, methods=True)
# inspect(Funcionario)
