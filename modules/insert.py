import requests #, os
import mysql.connector
from bs4 import BeautifulSoup

def database(nomePlat, descPlat, urlPlat, urlImg):
    meubd = mysql.connector.connect(
        host="localhost",
        user="aluno",
        password="sptech",
        database="bdSPHack"
    )

    mycursor = meubd.cursor()

    sql = "INSERT INTO bdSPHack.tbPlataforma (nomePlataforma, descPlataforma, urlPlataforma, urlImgPlataforma) VALUES(%s, %s, %s, %s);"
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

# Teste
def criaBanco():
    conexao = mysql.connector.connect(
        host="localhost",
        user="aluno",
        password="sptech",
    )
    cursor = conexao.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS bdSPHack;")
    cursor.execute("USE bdSPHack;")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tbUser(
        idUser INT PRIMARY KEY AUTO_INCREMENT
        , nomeUser VARCHAR(120) COMMENT 'Nome do usuário'
        , emailUser VARCHAR(120) COMMENT 'E-mail do usuário'
        , senhaUser VARCHAR(32) COMMENT 'Senha do usuário'
    ) COMMENT 'Dados do usuário' ;
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tbPlataforma(
        idPlataforma INT PRIMARY KEY AUTO_INCREMENT
        , nomePlataforma VARCHAR(120) COMMENT 'Nome da Plataforma'
        , descPlataforma TEXT COMMENT 'Descrição da plataforma'
        , urlPlataforma TEXT COMMENT 'URL da Plataforma'
        , urlImgPlataforma TEXT COMMENT 'URL da imagem dessa Plataforma'
    ) COMMENT 'Dados das plataformas';
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tbCurso(
        idCurso INT PRIMARY KEY AUTO_INCREMENT
        , fkPlataforma INT COMMENT 'id da tbPlataforma'
        , FOREIGN KEY (fkPlataforma) REFERENCES tbPlataforma(idPlataforma)
        , nomeCurso VARCHAR(120) COMMENT 'Nome do curso'
        , descCurso TEXT COMMENT 'Descrição do curso'
        , tipoValor VARCHAR(20) CHECK (tipoValor IN ('gratuito', 'pago') ) COMMENT 'Verifica se o curso é pago ou não'
        , urlCurso TEXT COMMENT 'URL da Curso'
        , urlImgCurso TEXT COMMENT 'URL da imagem desse Curso'
    ) COMMENT 'Dados dos cursos';
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tbFavoritos(
        fkUser INT COMMENT 'Id do usuário'
        , fkCurso INT COMMENT 'Id do curso'
        , FOREIGN KEY (fkUser) REFERENCES tbUser(idUser)
        , FOREIGN KEY (fkCurso) REFERENCES tbCurso(idCurso)
        , dataHoraAdd DATETIME COMMENT 'Data e hora de quando foi adicionado aos favoritos do usuário'
        , PRIMARY KEY (fkUser, fkCurso)
    ) COMMENT 'Junção da tabela de cursos e usuário para selecionar os favoritos de cada user';
    """)

    # cursor.execute("""
    # INSERT INTO bdSPHack.tbUser (nomeUser, emailUser, senhaUser)
    # VALUES ('Felipe Santos', 'felipe.almeida@sptech.school', '12345678')
    #     , ('Bruna Santana', 'Brubs@gmail.com', '12345678')
    #     , ('Thiago Mendonça', 'Thigos@gmail.com', '12345678')
    #     , ('João Bezerra', 'JB@gmail.com', '12345678');
    # """)

    print('[INFO] Todas as tabelas foram criadas')
    
    conexao.commit()

def insertCurso():
    print("Xamblada")