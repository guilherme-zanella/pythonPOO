from rich import print
from rich.table import Table
from classes import *

def main():
    dist = 10

    viangens = [Moto(dist), Caminhao(dist), Drone(dist)]

    tabela = Table(title='Tabela de Fretes')

    tabela.add_column('Distância')
    tabela.add_column('Tipo')
    tabela.add_column('Frete')

    for v in viangens:
        tabela.add_row(f'{dist}Km', f'{type(v).__name__}', f'{v.calcular_frete()}')
    
    print(tabela)

if __name__ == '__main__':
    main()
