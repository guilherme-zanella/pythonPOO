from abc import ABC, abstractmethod

class Validador(ABC):

    @abstractmethod
    def validar(self):
        pass


class Usuario(Validador):

    def validar(self, valor:str):

        caracteres = '!@#$%^&*()+-=[]{}|;:",./<>?`~'

        if 5 <= len(valor) <= 20:
            estado = True
            for l in valor:
                if l != l.lower():
                    estado = False
                if l in caracteres:
                    estado = False
                if l == ' ':
                    estado = False
        else:
            estado = False

        return estado


class Senha(Validador):

    def validar(self, valor):

        caracteres = '!@#$%^&*()+-=[]{}|;:",./<>?`~_'

        if len(valor) >= 8:
            estado = True
            maisculas = 0
            simbolos = 0

            for l in valor:
                if l != l.lower():
                    maisculas += 1
                if l in caracteres:
                    simbolos += 1
                if l == ' ':
                    estado = False
                         
            if maisculas == 0:
                estado = False  
            if simbolos == 0:
                estado = False    

        else:
            estado = False

        return estado


class Email(Validador):

    def validar(self, valor):
        estado = True

        caracteres = '!#$%^&*()=[]{}|;:",/<>?`~ '
        arrobas = 0
        pontos = 0

        for i, l in enumerate(valor):
            if l == '@':
                if i != 0:
                    arrobas += 1
            if l in caracteres:
                estado = False
            if l == '.':
                if arrobas != 0:
                    pontos += 1
            if l == ' ':
                estado = False

        if len(valor.split('.')[-1]) < 2:
            estado = False
        if arrobas != 1:
            estado = False
        if pontos == 0:
            estado = False

        return estado
            


def validar_dado(classe, valor):
    estado = classe.validar(valor)
    
    print(f'Valor: {valor} é valido? {'SIM' if estado else 'NÃO'}')

