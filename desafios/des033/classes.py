from datetime import datetime
from abc import ABC

ano_atual = datetime.now().year

class Pessoa(ABC):
    def __init__(self, nome, nasc):
        self._nome = nome
        self._nascimento = nasc
        self._idade = ano_atual - self._nascimento

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, ano):
        if ano_atual - 100 < ano < ano_atual:
            self._nascimento = ano
            self._idade = ano_atual - self._nascimento
        else:
            raise ValueError('Ano de nascimento inválido!')

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor=''):
        raise ValueError('Não é possível alterar a idade! Altere o ano de nascimento.')


class Aluno(Pessoa):
    def __init__(self, nome, nacs, curso):
        super().__init__(nome, nacs)
        self.cursos_oficiais = ['ADM', 'ADS', 'ENG', 'CONT']
        self._curso = curso

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self,curso):
        if curso in self.cursos_oficiais:
            self._curso = curso
        else:
            raise ValueError(f'O curso {curso} não é oficial!')

    def add_curso(self, c):
        self.cursos_oficiais.append(c.upper())
