from classes import *
from rich import print

def main():
    d = Diario('gui')

    try:
        d.escrever('Meu nome é Guilherme')
        d.escrever('Eu gosto de chocolate')
        d.escrever('Eu sou o melhor programador python')
    except Exception as e:
        print(f'Houve um erro: {e}')

    d.senha = 'teste'

    try:
        d.ler('teste')    
    except Exception as e:
        print(f'Ocorreu um erro: {e}')


if __name__ == '__main__':
    main()
