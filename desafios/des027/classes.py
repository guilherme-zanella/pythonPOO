from rich import print
from random import randint, choice
from abc import ABC, abstractmethod

class Personagem(ABC):
    golpes = ['chute na cara', 'pulo giratório', 'soco', 'magia', 'voadora', 'arma', 'bola de fogo']
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def rolar_dado(self):
        return randint(0,101)

    def atacar(self, alvo, forca):
        forca_ataque = forca - (forca / 100 * self.rolar_dado())
        print(f'[green]{self.nome}[/]({self.vida}) atacou [red1]{alvo.nome}[/]({alvo.vida}) com [blue]{choice(self.golpes)}[/] de força {forca}')
        print(f'[red]{alvo.nome}[/] recebeu [red1]dano de {forca_ataque:.0f}[/]!')

    @abstractmethod
    def curar(self):
        pass


class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)

    def curar(self):
        print(f'[green]{self.nome}[/] fez uma magia de cura e [green]recuperou {self.rolar_dado()*5}[/] pontos de [green]vida[/].')


class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)

    def curar(self):
            print(f'[green]{self.nome}[/] enrolou uma atadura e [green]recuperou {self.rolar_dado()*5}[/] pontos de [green]vida[/].')