import os

class Pesquisas_controller:
    lista_de_pesquisas = []
    caminho_pesquisa = os.path.join('Backend', 'Pesquisas')

    @classmethod
    def listar_arquivos(cls):
        for pesquisa in os.listdir(cls.caminho_pesquisa):
            if pesquisa.endswith('.txt'):
                cls.lista_de_pesquisas.append(pesquisa)
        
        return cls.lista_de_pesquisas

    @classmethod
    def busca_pesquisa(cls, texto):
        for pesquisa in os.listdir(cls.caminho_pesquisa):
            if pesquisa == texto:
                caminho_arquivo = os.path.join(cls.caminho_pesquisa, pesquisa)
                with open(caminho_arquivo, 'r') as p:
                    conteudo = p.read()
                return conteudo