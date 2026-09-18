from hashlib import sha256

class ContaBancaria:
    def __init__(self, id, nome, saldo=0, chave=None):
        self._id = id
        self._titular = nome
        self.__saldo = saldo

        if not chave:
            chave = self.pede_senha()
        else:
            chave = sha256(chave.encode('utf-8')).hexdigest()
        self.__hash = chave

        print(f'Conta {self._id} criada com sucesso. Saldo atual de R${self.__saldo:,.2f}')

    def __str__(self):
        return f'A conta {self._id} de {self.nome} tem saldo atual de R${self.__saldo:,.2f}'

    def validar(self, chave):
        if chave == self.__hash:
            return True
        else:
            return False

    def pede_senha(self):
        senha = str(input('Senha: '))
        hash = sha256(senha.encode('utf-8')).hexdigest()
        return hash

    @property
    def nome(self):
        return self._titular

    @nome.setter
    def nome(self, nome):
        senha = self.pede_senha()
        if self.validar(senha):
            self._titular = nome
            print(f'Nome da conta {self._id} trocado para {self._titular}')
        else:
            print(f'Senha inválida. Não foi possivel mudar o nome da conta {self._id}')

    def sacar(self, valor, chave=None):
        if not chave:
            hash = self.pede_senha()
        else:
            hash = sha256(chave.encode('utf-8')).hexdigest()

        if valor <= self.__saldo and valor > 0:
            if self.validar(hash):
                self.__saldo -= valor
                print(f'Saque de R${valor:.2f}. Autorizado na conta {self._id}')
            else:
                print(f'Senha inválida! Não foi possível realizar o saque na conta {self._id}')
        else:
            raise ValueError('Não pode fazer saques com valores negativos ou maiores que o saldo!')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f'Depósito de R${valor:.2f}. Autorizado na conta {self._id}')
        else:
            raise ValueError('Não pode fazer saques com valores negativos ou maiores que o saldo!')
