from classes import *

def main():
    c1 = Carteira(100)
    c2 = Carteira(200)

    c1 += 100 
    c2 -= 100

    if c1 == c2:
        print(f'As duas carteiras tem os mesmos valores')
    elif c1 >= c2:
        print('A primeira carteira tem mais dinheiro')
    elif c1 <= c2:
        print('A segunda carteira tem mais dinheiro')
    else:
        print(f'As carteiras tem valores diferentes')


if __name__ == '__main__':
    main()