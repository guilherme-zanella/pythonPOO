from classes import *
from rich import print, inspect

def main():
    s = Credencial()
    s.senha = 'abc'
    inspect(s, private=True)
    s.verificar_senha()

if __name__ == '__main__':
    main()
