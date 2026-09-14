from rich import inspect
from classes import Aluno, Professor, Funcionario, Pessoa


def main():
    a1 = Aluno('Guilherme', 14, 'Desenvolvedor', '12b')
    a1.fazer_aniversario()
    a1.fazer_matricula()
    a1.estudar()

    p1 = Professor('Cláudio', 46, 'Matemática', 'Doutorado')
    p1.fazer_aniversario()
    p1.dar_aula()
    p1.estudar()

    f1 = Funcionario('Rafaela', 39, 'Diretora', 'Secretaria')
    f1.fazer_aniversario()
    f1.bater_ponto()
    p1.estudar()

if __name__ == '__main__':
    main()
