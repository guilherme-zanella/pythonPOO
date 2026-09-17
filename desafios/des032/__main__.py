from classe import *
from rich import inspect, print

def main():
    c = ContaBancaria(22, 'Guilherme', 5000)
    c.nome = 'guilherme'
    c.depositar(100)
    c.sacar(200)
    inspect(c, private=True)


if __name__ == '__main__':
    main()
