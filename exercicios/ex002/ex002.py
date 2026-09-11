# Declaração da clase
class Gafanhoto:
    """ 
        Essa classe cria um gafanhoto, que é uma pessoa com nome e idade.

        Para criar um nova pessoa utilize:
        variavel = Gafanhoto(nome, idade)
    """ # Documentação
    def __init__(self, nome='', idade=0): # Método construtor
        # Atributos
        self.nome = nome
        self.idade = idade

    # Métodos
    def aniversario(self):
        self.idade += 1

    def __str__(self):
        return f'{self.nome} é gafanhoto(a) e tem {self.idade} anos de idade!'

    def __getstate__(self):
        return f'Estado: nome = {self.nome} e idade = {self.idade}'

# Declaração de objetos
g1 = Gafanhoto('Guilherme', 13)
g1.aniversario()
print(g1)

print(g1.__class__)

print(g1.__dict__)
print(g1.__getstate__())

print(g1.__doc__)
