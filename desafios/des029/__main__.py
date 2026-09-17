from classes import *

def main():
    d = Diario('gui')

    d.escrever('Meu nome é Guilherme')
    d.escrever('Eu gosto de chocolate')
    d.escrever('Eu sou o melhor programador python')

    d.ler('gui')    


if __name__ == '__main__':
    main()