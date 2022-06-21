import re
from urllib import response
import requests
import pandas as pd
from bs4 import BeautifulSoup

Newslist = []

# pegando site pela url
response = requests.get('https://g1.globo.com')

# colocando o site em uma variavel
content = response.content

# Dando ao bs4 a indicação de qu eé um html
site = BeautifulSoup(content, 'html.parser')

# Usando find para procurar uma div no site(metodo findAll para buscar todas as tags que possuem as mesmas especificações do parametros)
news = site.findAll('div', attrs={'class': 'feed-post-body'})

#laço percorrendo as noticias do site
for new in news:

    #busca do titulo da noticia oqual contem o link
    titulo = new.find('a', attrs={'class':'feed-post-link gui-color-primary gui-color-hover'})
    
    #Adicionando as noticias que tem titulo dentro de uma lista
    if(titulo):
        #lista de listas com titulo da materia e link da mesma
        Newslist.append([titulo.text,titulo['href']])



    #print(titulo.text,'\n')

#colocando as listas numa tabela com o pandas
Linkednews = pd.DataFrame(Newslist,columns=['titulo', 'link'])

#criando arquivo csv com a tabela do pandas
Linkednews.to_csv('noticiasGlobo.csv',index=False)

#imprimindo a tabela do pandas
print(Linkednews)

#print(news)

#Buscando mais especificamente dentro da noticia
#titulo = news.find('a', attrs={'class': 'feed-post-link gui-color-primary gui-color-hover'})

# Pretify pra imprimir formatadinho
# print(site.prettify())

#noticia formatadinha
#print(news.pretify())

#titulo ad noticia
#print(titulo.text)

