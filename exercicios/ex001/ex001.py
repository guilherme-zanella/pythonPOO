# Declaração da clase
class Gafanhoto:
    def __init__(self): # Método construtor
        # Atributos
        self.nome = ''
        self.idade = 0

    # Métodos
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f'{self.nome} é gafanhoto(a) e tem {self.idade} anos de idade!'

# Declaração de objetos
g1 = Gafanhoto()
g1.nome = 'Guilherme'
g1.idade = 13
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = 'Manuela'
g2.idade = 9
print(g2.mensagem())
