from classes import *
from rich import inspect, print

def main():
    a = Aluno('Guilherme', 2010, 'ADS')
    b = Aluno('Manuela', 2017, 'ENG')

    a.nascimento = 2012
    a.add_curso('MODA')
    a.curso = 'MODA'
    
    inspect(b, private=True)

if __name__ == '__main__':
    main()
