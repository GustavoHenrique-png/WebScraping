from urllib import response
import requests
from bs4 import BeautifulSoup

produto = input('Digite abaixo o produto o qual deseja buscar\n')

url = 'https://www.amazon.com.br/s?k='

response = requests.get(url + produto)

content = response.content

amazon = BeautifulSoup(content, 'html.parser')

print(response.text)