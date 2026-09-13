from time import sleep
from rich import print

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.pagina_atual = 1
        print(f':book: [blue]Você acabou de abrir o livro [red1]"{self.titulo}"[/red1] que tem [green]{self.paginas} páginas[/green] no total. Agora você está na [yellow]página {self.pagina_atual}[/]')

    def __str__(self):
        return f'Você está lendo o livro {self.titulo}.'

    def fim_livro(self) -> bool:
        return True if self.pagina_atual == self.paginas or self.pagina_atual > self.paginas else False

    def avancar_pagina(self, numero=1):
        for n in range(numero):
            if not self.fim_livro():
                self.pagina_atual += 1
                print(f'Pág{self.pagina_atual} :arrow_forward: ',end='')
                sleep(0.3)
                if n == numero-1 or self.fim_livro():
                    print(f'[blue]Você avançou {n+1} páginas e agora está na [yellow]página {self.pagina_atual}[/]')

            if self.fim_livro():
                print(f':closed_book: [red1]Você chegou ao final do livro "{self.titulo}"[/]')
                break


l1 = Livro('Um estudo em vermelho', 20)
l1.avancar_pagina(5)
l1.avancar_pagina(10)
l1.avancar_pagina(30)
l1.avancar_pagina(4)
