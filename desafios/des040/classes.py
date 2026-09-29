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
        import json

        lista_pessoas = []
        for v in lista:
            lista_pessoas.append(v.__dict__)

        with open('desafios/des040/pessoas.json', 'w', encoding='utf-8') as arq:
            json.dump(lista_pessoas, arq, indent=4, ensure_ascii=False)

        with open('desafios/des040/pessoas.json', 'r', encoding='utf-8') as arq:
            dados = json.load(arq)
            return json.dumps(dados, indent=4, ensure_ascii=False)


class XML:

    def exportar(self, lista):
        import xml.etree.ElementTree as ET

        nome = lista[0].__class__.__name__.lower()
        pai = ET.Element('dados')

        for elemento in lista:
            filho = ET.SubElement(pai, nome)
            for c, v in elemento.__dict__.items():
                neto = ET.SubElement(filho, c)
                neto.text = str(v)

        ET.indent(pai, space='\t')
        txt = ET.tostring(pai, encoding='unicode', xml_declaration=True)
        return txt



def exportar_dados(formato, lista):
    print(formato.exportar(lista))