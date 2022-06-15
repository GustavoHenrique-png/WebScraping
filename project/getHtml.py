import re
from urllib import response
import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.supermercadoriodaspedras.com.br')

content = response.content

site = BeautifulSoup(content,'html.parser')

#news = site.find('div', attrs={'class': 'feed-post-body'})

print(site.prettify)

class getHtml():

    response = requests.get('{site}')

rioDasPedras = getHtml()

rioDasPedras.response()