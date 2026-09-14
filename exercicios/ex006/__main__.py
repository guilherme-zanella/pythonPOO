from rich import inspect
from classes.aluno import Aluno
from classes.professor import Professor
from classes.funcionario import Funcionario

def main():
    a1 = Aluno('Guilherme', 14, 'Desenvolvedor', '12b')
    a1.fazer_aniversario()
    a1.fazer_matricula()

    p1 = Professor('Cláudio', 46, 'Matemática', 'Doutorado')
    p1.fazer_aniversario()
    p1.dar_aula()

    f1 = Funcionario('Rafaela', 39, 'Diretora', 'Secretaria')
    f1.fazer_aniversario()
    f1.bater_ponto()

if __name__ == '__main__':
    main()
