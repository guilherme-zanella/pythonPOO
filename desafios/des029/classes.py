from rich import print

class Diario:
    def __init__(self, senha='123'):
        self.__senha = senha.strip()
        self.__segredos = []

    def escrever(self, msg):
        if type(msg) == str and msg:
            self.__segredos.append(msg)
        else:
            raise ValueError('O segredo tem que ser uma string!')

    def ler(self, senha):
        if senha.strip() == self.__senha:
            print('[green] Diário Liberado [/]'.center(40,'-'))
            for m in self.__segredos:
                print(m)
        else:
            print('[red1] Diário Bloqueado [/]'.center(40,'-'))
            raise PermissionError('Senha inválida!')

    @property
    def senha(self):
        raise PermissionError('Nínguem tem a pemissão de ver a senha!')

    @senha.setter
    def senha(self, nova_senha):
        self.__senha = nova_senha
