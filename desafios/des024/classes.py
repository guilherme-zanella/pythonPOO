from abc import ABC, abstractmethod

class Bebida(ABC):
    def preparar(self):
        print(f' Iniciando o Preparo '.center(30, '-'))
        print(f'1. {self.ferver_agua()}')
        print(f'2. {self.misturar()}')
        print(f'3. {self.servir()}')
        print(f' Bebida Pronta '.center(30, '-'))

    def ferver_agua(self):
        return f'Fervendo a água a 100 graus Celsius.'

    @abstractmethod
    def misturar(self):
        pass

    def servir(self):
        pass


class Cafe(Bebida):
    def misturar(self):
        return f'Passando água pelo pó de café moído.'

    def servir(self):
        return f'Servindo em uma xícara pequena.'


class Cha(Bebida):
    def misturar(self):
        return f'Mergulhando o sachê de ervas na água.'

    def servir(self):
        return f'Servindo na caneca de porcelana com açúcar.'


class Leite(Bebida):
    def misturar(self):
        return f'Passando o vapor pelo bico do leite.'

    def servir(self):
        return f'Servindo na caneca grande, já com café.'
        