from classe import *
from rich import inspect, print

def main():
    c = ContaBancaria(22, 'Guilherme', 5000, '123')

    c.depositar(100)
    
    c.sacar(300)
    
    print(c)


if __name__ == '__main__':
    main()
