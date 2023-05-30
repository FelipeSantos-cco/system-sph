import requests #, os
from bs4 import BeautifulSoup

# print(os.getcwd())

arquivo = open('../plataformas.txt')
links = arquivo.readlines()
arquivo.close()

for link in links:
    resposta = requests.get(link)

    if resposta.status_code >= 200 and resposta.status_code < 300:
        site = BeautifulSoup(resposta.content, 'html.parser')

        titulo = site.find('h1', attrs={'class': 'entry-title'}).contents[0]

        descricao = 0#site.find()
        
        urlImg = site.find('img', attrs={'decoding': 'async'})

        urlPlataforma = site.find('div', attrs={'class': 'project-info'}).find('a', attrs={'target' : '_blank'}).get('href')

        print(f'{titulo}\n{descricao}\n{urlPlataforma}\n{urlImg}')

    if True:
        break