import requests, json

class Pesquisa: 

    def pesquisa():
        # URL Disponibilizada pela equipe do Guia de TI: https://guiadeti.com.br/
        url = 'https://guiadeti.com.br/wp-json/wp/v2/posts/'

        resposta = requests.get(url)
        # print(resposta.status_code)

        if resposta.status_code >= 200 and resposta.status_code < 300:
            # O que acontece?
            # essa url me retorna os ultimos 10 posts == um range de 0 a 9... já que dadosJSON é uma lista.....
            dadosJSON = resposta.json()

            for i in range(0, 9):
                post = dadosJSON[i]
                titulo = post['title']['rendered']
                link = post['link']

                print(f'Titulo: {titulo}\nLink: {link}\n\n')

        else:
            print(f"A conexão falhou\nResposta: {resposta.status_code}")