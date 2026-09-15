from classes import *
from rich import print

def main():
    p1 = Guerreiro('Kratos', 3000)
    p2 = Mago('Alanzoka', 2000)

    p1.atacar(p2, 4000)
    p2.curar()
    p2.atacar(p1, 3000)
    p1.status()
    p2.status()


if __name__ == '__main__':
    main()
