from classes import *
from rich import print, inspect

def main():
    c = Credencial()

    c.senha = 'teste1'

    c.validar('teste1')


if __name__ == '__main__':
    main()
