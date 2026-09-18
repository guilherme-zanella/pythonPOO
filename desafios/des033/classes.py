from datetime import datetime
from abc import ABC

ano_atual = datetime.now().year

class Pessoa(ABC):
    def __init__(self, nome, nasc):
        self._nome = nome
        self._nascimento = None
        self.nascimento = nasc
        self._idade = ano_atual - self._nascimento

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, ano):
        if ano_atual - 110 < ano <= ano_atual:
            self._nascimento = ano
            self._idade = ano_atual - self._nascimento
        else:
            raise ValueError('Ano de nascimento inválido!')

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        raise PermissionError('Não é possível alterar a idade! Altere o ano de nascimento.')


class Aluno(Pessoa):
    cursos_oficiais = ['ADM', 'ADS', 'ENG', 'CONT']

    def __init__(self, nome, nacs, curso):
        super().__init__(nome, nacs)
        self._curso = None
        self.curso = curso

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self,curso):
        if curso in Aluno.cursos_oficiais:
            self._curso = curso
        else:
            raise ValueError(f'O curso {curso} não é oficial!')

    def add_curso(self, c:str):
        c = c.strip().upper()

        if c not in Aluno.cursos_oficiais:
            if 3 <= len(c) <= 5:
                Aluno.cursos_oficiais.append(c.upper())
            else:
                raise ValueError(f'Nome {c} está fora do padrão para cursos')
        else:
            raise ValueError(f'Curso {c} já está na lista de cursos oficiais')
