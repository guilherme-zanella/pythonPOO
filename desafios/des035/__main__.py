from classes import *

def main():
    a1 = PDF('contrato', 250000)
    abrir_arquivo(a1)

    a2 = DOC('redação', 120000)
    abrir_arquivo(a2)


if __name__ == '__main__':
    main()
    