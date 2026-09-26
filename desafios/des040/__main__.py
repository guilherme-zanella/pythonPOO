from classes import *

def main():
    l = [
        Usuario('Guilherme', 'guilherme@gmail.com'),
        Usuario('Manuela', 'Manuzinha@gmail.com'),
        Aluno('Marcos', 'CNC', '192')
    ]

    exportar_dados(JSON(), l)


if __name__ == '__main__':
    main()