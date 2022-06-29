import pandas as pd
from urllib import response
import requests
from bs4 import BeautifulSoup

Namelist = []

produto = input('Digite abaixo o produto o qual deseja buscar\n')

url = 'https://www.amazon.com.br/s?k='

response = requests.get(url + produto)

content = response.content

amazon = BeautifulSoup(content, 'html.parser')

offers = amazon.find('div' , attrs={'class':'a-section a-spacing-none a-spacing-top-small s-title-instructions-style'})
#a-section a-spacing-none a-spacing-top-small s-title-instructions-style


for offer in offers:
    names = offer.find('span', attrs={'class':'a-size-base-plus a-color-base a-text-normal'})

    if(names):
        Namelist.append([names.text])

LinkedOffers = pd.DataFrame(Namelist,columns=['names'])

print(LinkedOffers)