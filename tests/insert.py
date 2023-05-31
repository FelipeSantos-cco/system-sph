import requests #, os
import mysql.connector
from bs4 import BeautifulSoup

def database(nomePlat, descPlat, urlPlat, urlImg):
    meubd = mysql.connector.connect(
        host="localhost",
        user="aluno",
        password="sptech",
        database="bdsphack"
    )

    mycursor = meubd.cursor()

    sql = "INSERT INTO bdsphack.tbplataforma (nomePlataforma, descPlataforma, urlPlataforma, urlImgPlataforma) VALUES(%s, %s, %s, %s);"
    val = (nomePlat, descPlat, urlPlat, urlImg)

    mycursor.execute(sql, val)
    meubd.commit()

    return print(f'Inseriu: {nomePlat}\n') 


def buscaLink():

    arquivo = open('../plataformas.txt')
    links = arquivo.readlines()
    arquivo.close()

    for link in links:
        resposta = requests.get(link)

        if resposta.status_code >= 200 and resposta.status_code < 300:
            site = BeautifulSoup(resposta.content, 'html.parser')

            titulo = site.find('h1', attrs={'class': 'entry-title'}).contents[0]

            descricao = site.find('div', attrs={'class': 'fusion-text fusion-text-1 fusion-text-no-margin'}).get_text()

            urlImg = site.find('img', attrs={'decoding': 'async'}).get('data-src')
            urlImg = 'https://guiadeti.com.br'+urlImg

            urlPlataforma = site.find('div', attrs={'class': 'project-info'}).find('a', attrs={'target' : '_blank'}).get('href')

            # print(f'{titulo}\n{descricao}\n{urlPlataforma}\n{urlImg}')
            database(titulo, descricao, urlPlataforma, urlImg)



buscaLink()