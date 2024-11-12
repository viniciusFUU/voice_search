import requests
from bs4 import BeautifulSoup
import lxml
import os

class Searching:
    @classmethod
    def wikipedia_search(cls, arquivo):
        caminho_textos = os.path.join('Backend', 'textos', arquivo)
        
        with open(caminho_textos, 'r') as busca:
            texto = busca.read().strip()
            
        caminho_pesquisa = os.path.join('Backend', 'Pesquisas')
        print(f"esse é o caminho: {caminho_pesquisa}")
        
        url = f"https://pt.wikipedia.org/wiki/{texto.replace(' ', '_')}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml-xml')
        paragrafos = soup.find_all('p')

        resposta = [p.get_text() for p in paragrafos[:3]]

        cls.verificacao_pasta_pesquisa(caminho_pesquisa)

        with open(os.path.join('Backend', 'Pesquisas',f'{texto}.txt'), 'w', encoding="utf-8") as pesquisa:
            pesquisa.write("\n".join(resposta))

        return resposta

    @classmethod
    def verificacao_pasta_pesquisa(cls, caminho_pesquisa):
        if not os.path.exists(caminho_pesquisa):
            print("Criando a pasta 'Pesquisas'")
            os.makedirs(caminho_pesquisa)