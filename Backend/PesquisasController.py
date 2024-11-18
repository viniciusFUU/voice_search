import os
import FolderVerification

lista_de_pesquisas = []
caminho_pesquisa = os.path.join('Backend', 'Pesquisas')

def listar_arquivos():
    FolderVerification.varificacao_pastas(caminho_pesquisa)
    
    for pesquisa in os.listdir(caminho_pesquisa):
        if pesquisa.endswith('.txt'):
            lista_de_pesquisas.append(pesquisa)
    
    return lista_de_pesquisas

def busca_pesquisa(texto):
    for pesquisa in os.listdir(caminho_pesquisa):
        if pesquisa == texto:
            caminho_arquivo = os.path.join(caminho_pesquisa, pesquisa)
            with open(caminho_arquivo, 'r', encoding='utf-8') as p:
                conteudo = p.read()
            return conteudo