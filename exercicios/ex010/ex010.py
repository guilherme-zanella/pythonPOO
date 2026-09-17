class Avaliacao:
    def __init__(self, nome, disciplina, nota=0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota

    @property
    def nota(self): #getter
        return self._nota
    
    @nota.setter # setter
    def nota(self, valor):
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            print('Nota inválida!')

    @nota.deleter
    def nota(self):
        pass
    