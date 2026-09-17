from classe import *
from rich import print, inspect

def main():
    r = Retangulo()

    r.base = 10
    r.altura = 12

    # r.medidas = (2,4)

    print(r.medidas)


if __name__ == '__main__':
    main()