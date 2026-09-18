from classe import *
from rich import print, inspect

def main():
    r = Retangulo()

    try:
        # r.base = 10
        # r.altura = 12
        r.medidas = (2,4)

    except Exception as e:
        print(f'Ocorreu um {type(e).__name__}: {e}')

    print(r.medidas)


if __name__ == '__main__':
    main()