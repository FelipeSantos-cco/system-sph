import requests 
from bs4 import BeautifulSoup

class Buscar():

    def pesquisa_palavra():
        url = 'https://guiadeti.com.br/'

        header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/51.0.2704.103 Safari/537.36'
        }

        resposta = requests.get(url, headers= header)

        if resposta.status_code >= 200 and resposta.status_code < 300:
            print("Requisição OK")
            site = BeautifulSoup(resposta.content, 'html.parser')
            tabelaCursos = site.find('div', attrs={'class': 'fusion-fullwidth fullwidth-box fusion-builder-row-4 fusion-flex-container nonhundred-percent-fullwidth non-hundred-percent-height-scrolling'})
            
            listaLinks = []

            for link in tabelaCursos.find_all('a'):
                if link.get('href') not in listaLinks:
                    listaLinks.append(link.get('href'))

            print(listaLinks)
