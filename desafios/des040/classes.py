import json

class Aluno:

    def __init__(self, nome, curso, serie):
        self.nome = nome
        self.curso = curso
        self.serie = serie


class Usuario:

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


class JSON:
    
    def exportar(self, lista):
        lista_pessoas = []
        conteudo = {}
        for v in lista:
            conteudo = {}

            if v.__class__.__name__ == 'Usuario':
                conteudo.update({'nome': v.nome})
                conteudo.update({'email': v.email})

            if v.__class__.__name__ == 'Aluno':
                conteudo.update({'nome': v.nome})
                conteudo.update({'curso': v.curso})
                conteudo.update({'serie': v.serie})

            lista_pessoas.append(conteudo)

        with open('desafios/des040/pessoas.json', 'w', encoding='utf-8') as arq:
            json.dump(lista_pessoas, arq, indent=4, ensure_ascii=False)

        with open('desafios/des040/pessoas.json', 'r', encoding='utf-8') as arq:
            dados = json.load(arq)
            print(json.dumps(dados, indent=4, ensure_ascii=False))



def exportar_dados(objeto, lista):
    objeto.exportar(lista)