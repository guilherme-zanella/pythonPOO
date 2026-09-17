class Diario:
    def __init__(self, senha=123):
        self.__senha = senha
        self.__segredos = []

    def escrever(self, msg):
        self.__segredos.append(msg)

    def ler(self, senha):
        if senha == self.__senha:
            print('Meu Diário'.center(30,'-'))
            for m in self.__segredos:
                print(m)
        else:
            raise PermissionError('Senha inválida')
