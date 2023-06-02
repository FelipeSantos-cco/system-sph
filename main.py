# from modules.guia_de_ti_testes import Buscar
from modules.atualiza_guia import Pesquisa as noticia
import modules.insert as banco 

def banner():
  escolha = input(''' 
  /$$$$$$  /$$$$$$$  /$$   /$$                     /$$      
 /$$__  $$| $$__  $$| $$  | $$                    | $$      
| $$  \__/| $$  \ $$| $$  | $$  /$$$$$$   /$$$$$$$| $$   /$$
|  $$$$$$ | $$$$$$$/| $$$$$$$$ |____  $$ /$$_____/| $$  /$$/
 \____  $$| $$____/ | $$__  $$  /$$$$$$$| $$      | $$$$$$/ 
 /$$  \ $$| $$      | $$  | $$ /$$__  $$| $$      | $$_  $$ 
|  $$$$$$/| $$      | $$  | $$|  $$$$$$$|  $$$$$$$| $$ \  $$
 \______/ |__/      |__/  |__/ \_______/ \_______/|__/  \__/

\t\t[+] Felipe Santos de Almeida :)
\n> Opções:
\t0 - Noticias teste
\t1 - Criação do banco
\t2 - Insert Plataformas [!SCRAPING!]
\t3 - Insert Cursos
\n>>>> ''')
  
  return escolha

# O intuito dessa função era ver a disponibilidade de Web Scraping em cima desse site.
# Buscar.pesquisa_plataforma()
## Esta função retornou 176 links de plataformas disponiveis para web scraping

escolha = banner()

if escolha == 0:
	noticia.pesquisa()
        
elif escolha == 1:
  banco.criaBanco()

elif escolha == 2:
  banco.buscaLink()

elif escolha == 3:
  banco.insertCurso()
