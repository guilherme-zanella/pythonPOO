from time import sleep
from rich import print

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.p_atual = 1
        print(f':book: [blue]Você acabou de abrir o livro [red1]"{self.titulo}"[/red1] que tem [green]{self.paginas} páginas[/green] no total. Agora você está na [yellow]página {self.p_atual}[/]')

    def next_page(self, numero):
        for n in range(numero):
            self.p_atual += 1
            print(f'Pág{self.p_atual} > ',end='')
            sleep(0.5)
            if n == numero-1 or self.p_atual == self.paginas:
                print(f'[blue]Você avançou {n+1} páginas e agora está na [yellow]página {self.p_atual}[/]')
            if self.p_atual == self.paginas:
                print(f':closed_book: [red1]Você chegou ao final do livro "{self.titulo}"[/]')
                break



l1 = Livro('Um estudo em vermelho', 20)
l1.next_page(5)
l1.next_page(10)
l1.next_page(30)
