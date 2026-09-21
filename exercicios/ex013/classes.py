class Mae:
    def __init__(self, nome='mamãe'):
        self.nome = nome

    def fazer_pudim(self):
        print(f'{self.nome} faz PUDIM com leite condensado')

    def fritar_coxinha(self):
        print(f'{self.nome} frita a COXINHA no óleo')


class Filha(Mae):
    def fazer_pudim(self):
        print(f'{self.nome} faz PUDIM com creme de leite')

class Filho(Mae):
    def fritar_coxinha(self):
        print(f'{self.nome} frita a COXINHA na Air Fryer')