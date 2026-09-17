from ex010 import *
from rich import inspect, print

def main():
    a1 = Avaliacao('Pedro', 'Matemática')
    a1.nota = 9
    print(f'{a1.nome} tirou {a1.nota} na prova de {a1.disciplina}')
    inspect(a1, private=True)


if __name__ == '__main__':
    main()