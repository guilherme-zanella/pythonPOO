class Produto:

    def __init__(self, nome:str , preco: int|float):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f'{self.nome} (R${self.preco:,.2f})'


class Carrinho:

    def __init__(self):
        self.produtos = []
        self.total = 0

    def __str__(self):
        conteudo = '-'*30

        for p in self.produtos:
            conteudo += f'\n{p}'
        
        conteudo += '\n'    
        conteudo += '-'*30
        conteudo += f'\nTotal: R${self.total:,.2f}'

        return conteudo
        

    def __iadd__(self, produto):
        if produto.__class__.__name__ == 'Produto':
            self.produtos.append(produto)
            self.total += produto.preco
            return self
        elif produto.__class__.__name__:
            for i in produto.produtos:
                self.produtos.append(i)
