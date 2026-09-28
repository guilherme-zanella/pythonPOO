from classes import *
from rich import inspect, print

def main():
    p1 = Produto('Teclado', 480)
    p2 = Produto('Mouse', 95)
    p3 = Produto('Fone', 200)
    p4 = Produto('Controle', 356)

    c1 = Carrinho()
    c2 = Carrinho()

    c1 += p1
    c1 += p2

    c2 += c1
    c2 += p3

    print(c1)
    print(c2)


if __name__ == '__main__':
    main()