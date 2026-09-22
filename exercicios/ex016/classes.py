class Porta:
    def abrir(self):
        print('Girar a maçaneta e empurrar/puxar a porta')

class Empresa:
    def abrir(self):
        print(f'Vá ao portal do empreendor com toda a documetação')

class Ovo:
    def abrir(self):
        print(f'Quebre a casca e reparta no meio sobre uma frigideira')

class Pedra:
    pass

# Metodo pythonico polimorfico "duck typing"

def tentar_abrir(objeto):
    try:
        objeto.abrir()
    except:
        print(f'Encontrei poblemas ao tentar abrir {objeto.__class__.__name__}')
