from classes import *
from rich import print, inspect

def main():
    t = Termostato()
    t.temperatura = 25.5
    print(f'A temperatura do termostato é de {t.temperatura}')

if __name__ == '__main__':
    main()