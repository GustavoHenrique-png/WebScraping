import re
from urllib import response
import requests
from bs4 import BeautifulSoup

# pegando site pela url
response = requests.get('https://g1.globo.com')

# colocando o site em uma variavel
content = response.content

# Dando ao bs4 a indicação de qu eé um html
site = BeautifulSoup(content, 'html.parser')

# Usando find para procurar uma div no site
news = site.find('div', attrs={'class': 'feed-post-body'})

#Buscando mais especificamente dentro da notici
titulo = news.find('a', attrs={'class': 'feed-post-link gui-color-primary gui-color-hover'})

# Pretify pra imprimir formatadinho
# print(site.prettify())

#noticia formatadinha
#print(news.pretify())

#titulo ad noticia
print(titulo.text)
