from abc import ABC, abstractmethod

class Arquivo(ABC):
    def __init__(self, nome: str, ext: str, tamanho: int|float):
        self.nome = nome
        self._extensao = None
        self.tamanho = tamanho
        self.extensao = ext

    @property
    def nome_completo(self):
        return f'"{self.nome}.{self._extensao.lower()}" ({self.tamanho / 1_000_000}MB)'

    @property
    def extensao(self):
        return self._extensao

    @extensao.setter
    def extensao(self, ext: str):
        formatos = ['pdf', 'doc', 'docx', 'py', 'html']
        ext = ext.lower().strip()
        
        if ext in formatos:
            self._extensao = ext
        else:
            raise AttributeError('Formato do arquivo digitado não é suportado')

    @abstractmethod
    def abrir(self):
        pass

class PDF(Arquivo):
    def __init__(self, nome, tamanho):
        super().__init__(nome, 'pdf', tamanho)

    def abrir(self):
        print(f'Abrindo o arquivo {self.nome_completo} no Adobe Reader')


class DOC(Arquivo):
    def __init__(self, nome, tamanho):
        super().__init__(nome, 'docx', tamanho)

    def abrir(self):
        print(f'Abrindo o arquivo {self.nome_completo} no Microsoft Word')


class PY(Arquivo):
    def __init__(self, nome, tamanho):
        super().__init__(nome, 'py', tamanho)

    def abrir(self):
        print(f'Abrindo o arquivo {self.nome_completo} ({self._tamanho}MB) no Visual Studio Code')


class HTML(Arquivo):
    def __init__(self, nome, tamanho):
        super().__init__(nome, 'html', tamanho)

    def abrir(self):
        print(f'Abrindo o arquivo {self.nome_completo} ({self._tamanho}MB) no Google Chrome')


def abrir_arquivo(arquivo):
    arquivo.abrir()
