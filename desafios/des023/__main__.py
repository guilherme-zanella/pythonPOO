from classes import Quadrado, Circulo
from rich import print

def main():
    p1 = Quadrado(5)
    print(p1)
    print(f'Perímetro = {p1.perimetro():.1f}')
    print(f'Área = {p1.area():.1f}')

    p2 = Circulo(20)
    print(p2)
    print(f'Perímetro = {p2.perimetro():.1f}')
    print(f'Área = {p2.area():.1f}')

if __name__ == '__main__':
    main()