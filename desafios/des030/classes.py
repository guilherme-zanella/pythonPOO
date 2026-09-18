from hashlib import sha256
from rich import print

class Credencial:
    def __init__(self):
        self.__hash = None

    @property
    def senha(self):
        return self.__hash

    @senha.setter
    def senha(self,chave):
        if len(chave) >= 6 and len(chave) <= 12:
            self.__hash = sha256(chave.encode('utf-8')).hexdigest()
        else:
            raise ValueError('A senha precisa ter no mínimo 6 caracteres e 12 no máximo')

    def validar(self, chave):
        usuario = sha256(chave.encode('utf-8')).hexdigest()
        if usuario == self.__hash:
            print('[green]Senha Confere![/]')
        else:
            print('[red1]Senha não confere![/]')
            