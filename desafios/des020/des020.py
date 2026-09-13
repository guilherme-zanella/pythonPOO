from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.jogos = []

    def add_favorite(self, jogo):
        self.jogos.append(jogo)

    def ficha(self):
        conteudo = (
            f'Nome real: [black on blue]{self.nome}[/]\n'
            f'Jogos favoritos:'
        )
        for j in self.jogos:
            conteudo += f'\n :video_game: [blue]{j}[/]'

        caixa = Panel(conteudo,
                    title=f'Jogador <{self.nick}>',
                    width=50
                    )
        print(caixa)



j1 = Gamer('Guilherme Zanella', 'guizim123')
j1.add_favorite('Fortnite')
j1.add_favorite('FIFA')
j1.add_favorite('Brawl stars')
j1.add_favorite('Rocket league')
j1.ficha()
