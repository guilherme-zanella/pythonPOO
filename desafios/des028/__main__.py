from classes import *
from rich import print, inspect

def main():
    t = Termostato()
    try:
        t.temperatura = 25.3
    except Exception as e:
        print(f'Houve um problema: {e}')

    print(f'A temperatura do termostato é de {t.ftemperatura}')

    
if __name__ == '__main__':
    main()