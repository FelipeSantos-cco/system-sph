from modules.guia_de_ti_testes import Buscar
from modules.atualiza_guia import Pesquisa as noticia
import modules.insert as banco 

def banner():
    print(''' 
  /$$$$$$  /$$$$$$$  /$$   /$$                     /$$      
 /$$__  $$| $$__  $$| $$  | $$                    | $$      
| $$  \__/| $$  \ $$| $$  | $$  /$$$$$$   /$$$$$$$| $$   /$$
|  $$$$$$ | $$$$$$$/| $$$$$$$$ |____  $$ /$$_____/| $$  /$$/
 \____  $$| $$____/ | $$__  $$  /$$$$$$$| $$      | $$$$$$/ 
 /$$  \ $$| $$      | $$  | $$ /$$__  $$| $$      | $$_  $$ 
|  $$$$$$/| $$      | $$  | $$|  $$$$$$$|  $$$$$$$| $$ \  $$
 \______/ |__/      |__/  |__/ \_______/ \_______/|__/  \__/

\t\t[+] Felipe Santos de Almeida :)
\t\t[+] Projeto pessoal SPHack para a faculdade SPTech
\t\t[!] Apoio: Guia de TI
''')

# O intuito dessa função era ver a disponibilidade de Web Scraping em cima desse site.
# Buscar.pesquisa_plataforma()
## Esta função retornou 176 links de plataformas disponiveis para web scraping

banner()
info = int(input('''Escolha uma opção:\n
[0] - Ver noticias sobre cursos
[1] - Criação de Baanco - EM DESENVOLVIMENTO
[2] - Busca de Plataformas - Web Scraping
[3] - Inserção de Plataformas no Banco de Dados - Web Scraping

>->-> '''))

print('\n')

escolha = info

if escolha == 0:
	noticia.pesquisa()
        
elif escolha == 1:
  banco.criaBanco()

elif escolha == 2:
  Buscar.pesquisa_plataforma()

elif escolha == 3:
  banco.buscaLink()

else:
  print("[!] Escolha uma função válida!!!")

