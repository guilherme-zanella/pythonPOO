from classes import *
from rich import inspect, print

def main():
    p1 = Produto('Teclado', 480)
    p2 = Produto('Mouse', 95)
    p3 = Produto('Gabinete', 200)
    p4 = Produto('Controle', 356)

    c1 = Carrinho()

    c1 = c1 + p1


    print(c1)


if __name__ == '__main__':
    main()