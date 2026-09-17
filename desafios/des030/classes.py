import hashlib
import os

class Credencial:
    def __init__(self):
        self._senha = ''
        self.__hash = ''

    @property
    def senha(self):
        pass

    @senha.setter
    def senha(self,s):
        salt = os.urandom(64)
        self.__hash = hashlib.pbkdf2_hmac(
        'sha256',
        s.encode('utf-8'),
        salt
    )

    def verificar_senha(self, senha):
        pass