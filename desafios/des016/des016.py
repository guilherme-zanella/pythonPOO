from rich import print

class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        return f':handshake: Olá, sou [blue1]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa Curso Em Vídeo'


f1 = Funcionario('Maria', 'Administração', 'Diretora')
f2 = Funcionario('Pedro', 'TI', 'Programador')

print(f1.apresentacao())
print(f2.apresentacao())
