from classes import Quadrado, Circulo
from rich import print

def main():
    p1 = Quadrado(5)
    print(p1)
    print(f'Perímetro = {p1.perimetro()}')
    print(f'Área = {p1.area()}')

    p2 = Circulo(20)
    print(p2)
    print(f'Perímetro = {p2.perimetro()}')
    print(f'Área = {p2.area()}')

if __name__ == '__main__':
    main()