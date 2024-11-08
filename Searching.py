import requests
from bs4 import BeautifulSoup
import lxml

class Searching:
    def wikipedia_search(arquivo):
        with open(arquivo, 'r') as busca:
            texto = busca.read().strip()
        url = f"https://pt.wikipedia.org/wiki/{texto.replace(' ', '_')}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml-xml')
        paragrafos = soup.find_all('p')
        return [p.get_text() for p in paragrafos[:3]]