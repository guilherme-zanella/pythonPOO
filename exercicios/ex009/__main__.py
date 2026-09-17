from ex009 import *
from rich import inspect

def main():
    a1 = Avaliacao('Pedro', 'Matemática')
    a1.set_nota(9)
    print(f'{a1.nome} tirou {a1.get_nota()} na prova de {a1.disciplina}')
    inspect(a1, private=True)


if __name__ == '__main__':
    main()