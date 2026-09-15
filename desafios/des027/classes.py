from rich import print
from random import randint, choice
from abc import ABC, abstractmethod

class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        golpes = []

    def rolar_dado(self, num):
        return randint(0, num)

    def atacar(self, alvo, forca = 100):
        if self.vida > 0 and alvo.vida > 0:
            golpe = choice(self.golpes)

            print(f'[blue]{self.nome}[/]({self.vida}) atacou [red]{alvo.nome}[/]({alvo.vida}) com [blue]{golpe}[/] de força {forca}')

            alvo.receber_dano(forca)
        else:
            print(f'O ataque não pode acontecer\n')

    def receber_dano(self, dano):
        forca_ataque = self.rolar_dado(dano)
        self.vida -= forca_ataque

        if self.vida < 0:
            self.vida = 0
            print('[red1]Alvo morto[/]!\n')
        else:
            print(f'[red]{self.nome}[/] recebeu [red1]dano de {forca_ataque:.0f}[/]!\n')

    def status(self):
        print(f'O personagem: [blue]{self.nome}[/] ([yellow]{self.__class__.__name__}[/]) tem:\n'
              f'A vida de [green]{self.vida}[/]\n'
              f'Os golpes: {self.golpes}\n')

    @abstractmethod
    def curar(self):
        pass


class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['arco e flecha', 'magia', 'transformação', 'bruxaria', 'poção mágica']

    def curar(self):
        cura = self.rolar_dado(100)

        if self.vida > 0:
            print(f'[green]{self.nome}[/] fez uma magia de cura e [green]recuperou {cura}[/] pontos de [green]vida[/].\n')
            self.vida += cura


class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['chute na cara', 'pulo giratório', 'soco', 'voadora', 'espada']

    def curar(self):
        cura = self.rolar_dado(100)

        if self.vida > 0:
            print(f'[green]{self.nome}[/] enrolou uma atadura e [green]recuperou {cura}[/] pontos de [green]vida[/].\n')
            self.vida += cura
