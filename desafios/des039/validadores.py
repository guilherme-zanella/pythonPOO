from abc import ABC, abstractmethod
import re

class Validador(ABC):

    @abstractmethod
    def validar(self):
        pass


class Usuario(Validador):

    def validar(self, valor:str):
        regex = r'^[a-z0-9_]{5,20}$'
        if re.fullmatch(regex, valor):
            return True
        else:
            return False


class Senha(Validador):

    def validar(self, valor):
        regex = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@!#$%&?/|\=+-_,.]).{8,}$'
        if re.fullmatch(regex, valor):
            return True
        else:
            return False


class Email(Validador):

    def validar(self, valor):
        regex = r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z0-9]{2,}$'
        if re.fullmatch(regex, valor):
            return True
        else:
            return False


            
def validar_dado(classe, valor):
    resultado = classe.validar(valor)
    
    print(f'Valor: {valor} é valido? {'SIM' if resultado else 'NÃO'}')

