from classe import *
from rich import inspect, print

def main():
    c = ContaBancaria(22, 'Guilherme', 5000, '123')

    print('Mudando o nome')
    c.nome = 'Manuela'

    print('Vou depositar')
    c.depositar(100)

    print('Vou sacar')
    c.sacar(300)

    print(c)


if __name__ == '__main__':
    main()
