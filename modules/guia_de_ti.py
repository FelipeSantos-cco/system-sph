import requests 
from bs4 import BeautifulSoup

class Buscar():

    def pesquisa_plataforma():

        url = 'https://guiadeti.com.br/'

        header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/51.0.2704.103 Safari/537.36'
        }

        listaLinks = []
        listaPlatLink = []

        resposta = requests.get(url, headers= header)

        if resposta.status_code >= 200 and resposta.status_code < 300:
            # print("Requisição OK")
            print("Buscando plataformas...")
            
            site = BeautifulSoup(resposta.content, 'html.parser')
            divLinks = site.find('div', attrs={'class': 'fusion-fullwidth fullwidth-box fusion-builder-row-4 fusion-flex-container nonhundred-percent-fullwidth non-hundred-percent-height-scrolling'})

            for link in divLinks.find_all('a'):

                if link.get('href') not in listaLinks: # Não pegar links repetidos
                    listaLinks.append(link.get('href'))

            #print(listaLinks)
            for i in range(0, len(listaLinks)):
                resposta = requests.get(listaLinks[i], headers= header)
                
                if resposta.status_code >= 200 and resposta.status_code < 300:
                    print(f"Entrando no Link: {listaLinks[i]}")

                    site = BeautifulSoup(resposta.content, 'html.parser')
                    divPlataformas = site.find('div', attrs={'class': 'fusion-portfolio-wrapper'})

                    for link in divPlataformas.find_all('a'):

                        if link.get('href') not in listaPlatLink:
                            listaPlatLink.append(link.get('href'))


            for i in range(0, len(listaPlatLink)):
                print(f"Plataforma: {listaPlatLink[i]}")
                            
                            
                         

        else:
            print(f"Erro na conexão\nResposta: {resposta.status_code}")
