# from modules.guia_de_ti_testes import Buscar
from modules.atualiza_guia import Pesquisa


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
    ''')


banner()

# O intuito dessa função era ver a disponibilidade de Web Scraping em cima desse site.
# Buscar.pesquisa_plataforma()
## Esta função retornou 176 links de plataformas disponiveis para web scraping

Pesquisa.pesquisa()