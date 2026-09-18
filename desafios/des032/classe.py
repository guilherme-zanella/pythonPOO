from hashlib import sha256

class ContaBancaria:
    def __init__(self, id:int, nome:str, saldo:float=0, chave:str=None):
        self._id = id
        self._titular = nome
        self.__saldo = saldo

        if not chave:
            chave = self.pede_senha()
        self.__hash = sha256(chave.encode('utf-8')).hexdigest()

        print(f'Conta {self._id} criada com sucesso. Saldo atual de R${self.__saldo:,.2f}')

    def __str__(self) -> str:
        return f'A conta {self._id} de {self.nome} tem saldo atual de R${self.__saldo:,.2f}'

    def validar_senha(self, chave) -> bool:
        senha = sha256(chave.encode('utf-8')).hexdigest()

        if senha == self.__hash:
            return True
        else:
            return False

    def pede_senha(self) -> str:
        from pwinput import pwinput

        senha = str(pwinput('Senha: ','🔒')).strip()
        return senha

    @property
    def nome(self) -> str:
        return self._titular

    @nome.setter
    def nome(self, nome):
        senha = self.pede_senha()

        if self.validar_senha(senha):
            if len(nome) > 1:
                self._titular = nome
                print(f'Nome da conta {self._id} trocado para {self._titular}')
        else:
            print(f'Senha inválida. Não foi possivel mudar o nome da conta {self._id}')

    def sacar(self, valor, chave=None):
        if not chave:
            chave = self.pede_senha()

        if valor <= self.__saldo and valor > 0:

            if self.validar_senha(chave):
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
