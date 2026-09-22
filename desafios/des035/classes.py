from abc import ABC, abstractmethod

class Arquivo(ABC):
    def __init__(self, nome: str = '', tamanho: int|float = 0 ):
        self.nome = nome
        self._tamanho = tamanho
        self.extensao = self.__class__.__name__

    @property
    def nome_completo(self):
        return f'"{self.nome}.{self.extensao.lower()}"({self._tamanho / 1e+6}MB)'


    def abrir(self):
        print(f'Abrindo o arquivo {self.nome_completo} no Google docs')

class PDF(Arquivo):
    def abrir(self):
        print(f'Abrindo o arquivo {self.nome_completo} no Adobe Reader')


class DOC(Arquivo):
    def abrir(self):
        print(f'Abrindo o arquivo {self.nome_completo} no Microsoft Word')


class PY(Arquivo):
    def abrir(self):
        print(f'Abrindo o arquivo {self.nome_completo} ({self._tamanho}MB) no Visual Studio Code')


class HTML(Arquivo):
    def abrir(self):
        print(f'Abrindo o arquivo {self.nome_completo} ({self._tamanho}MB) no Google Chrome')

