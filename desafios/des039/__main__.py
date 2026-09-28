from validadores import *

def main():
    validar_dado(Usuario(), 'guilherme_zanella')
    validar_dado(Email(), 'zanellag722@gmail.com')
    validar_dado(Senha(), 'aB@123456')


if __name__ == '__main__':
    main()