from classes import *
from rich import inspect, print

def main():
    a = Aluno('Guilherme', 2010, 'ADS')

    a.nascimento = 2012
    a.add_curso('moda')
    a.curso = 'MODA'
    
    inspect(a, private=True)

if __name__ == '__main__':
    main()
