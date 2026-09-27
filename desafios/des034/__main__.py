from classes import *

def main():
    funcionarios = [
        Gerente('Claudio', 20000),
        Desenvolvedor('Guilherme', 15000),
        Designer('Manuela', 12000)
    ]

    for f in funcionarios:
        print(f)


if __name__ == '__main__':
    main()