class Produto:

    def __init__(self, nome:str , preco: int|float):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f'{self.nome} ({formatar_dinheiro(self.preco)})'


class Carrinho:

    def __init__(self, produtos: list = None):
        self.produtos = produtos if produtos else []

    @property
    def total(self):
        return sum(p.preco for p in self.produtos)

    def __str__(self):
        conteudo = '~'*30
        for p in self.produtos:
            conteudo += f'\n{p}'
        
        conteudo += '\n'    
        conteudo += '-'*30
        conteudo += f'\nTotal: {formatar_dinheiro(self.total)}'

        return conteudo
        
    def __iadd__(self, outro):
        if isinstance(outro, Produto):
            return Carrinho(self.produtos + [outro])
        elif isinstance(outro, Carrinho):
            return Carrinho(self.produtos + [p for p in outro.produtos])
        else:
            raise TypeError('Você tentou adicionar algo inválido no carrinho')


def formatar_dinheiro(valor):
    import locale

    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    formatado = locale.currency(valor, grouping=True)

    return formatado
    
