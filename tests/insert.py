# import requests

arquivo = open('../plataformas.txt', 'r')
links = arquivo.readlines()
arquivo.close()

for link in links:
    