import requests
from bs4 import BeautifulSoup
import lxml
import os

class Searching:
    def wikipedia_search(arquivo):
        caminho_textos = os.path.join('Backend', 'textos', arquivo)
        # print(f"caminho do texto: {caminho_textos}")
        with open(caminho_textos, 'r') as busca:
            texto = busca.read().strip()
            print(f"texto: {texto}")
        url = f"https://pt.wikipedia.org/wiki/{texto.replace(' ', '_')}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml-xml')
        paragrafos = soup.find_all('p')
        return [p.get_text() for p in paragrafos[:3]]