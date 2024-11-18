import requests
from bs4 import BeautifulSoup
import FolderVerification
import lxml
import os

def wikipedia_search(arquivo):
    caminho_pesquisa = os.path.join('Backend', 'Pesquisas')
    
    FolderVerification.varificacao_pastas(caminho_pesquisa)
    caminho_textos = os.path.join('Backend', 'textos', arquivo)
    
    with open(caminho_textos, 'r', encoding='utf-8') as busca:
        texto = busca.read().strip()

    url = f"https://pt.wikipedia.org/wiki/{texto.replace(' ', '_')}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml-xml')
    paragrafos = soup.find_all('p')

    resposta = [p.get_text() for p in paragrafos[:3]]


    with open(os.path.join('Backend', 'Pesquisas',f'{texto}.txt'), 'w', encoding="utf-8") as pesquisa:
        pesquisa.write("\n".join(resposta))

    return resposta