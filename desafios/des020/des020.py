from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.jogos = []

    def add_favorito(self, jogo):
        self.jogos.append(jogo)
        self.jogos = sorted(self.jogos)

    def ficha(self):
        conteudo = (
            f'Nome real: [black on blue] {self.nome} [/]\n'
            f'Jogos favoritos:'
        )
        for j in self.jogos:
            conteudo += f'\n :video_game: [blue]{j}[/]'

        painel = Panel(conteudo, title=f'Jogador <{self.nick}>', width=50)
        print(painel)


j1 = Gamer('Guilherme Zanella', 'guizim123')
j1.add_favorito('Fortnite')
j1.add_favorito('FIFA')
j1.add_favorito('Brawl stars')  
j1.add_favorito('Rocket league')
j1.ficha()
