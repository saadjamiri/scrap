import requests as rq
from bs4 import BeautifulSoup
import re
url = 'https://books.toscrape.com/'
#envoyer une requête à la page web 
reponse=rq.get(url)
#parser le contenu de Html avec BeautifulSoup
contenu_page=reponse.text
html = BeautifulSoup(contenu_page,'html.parser')
#imprimer tout le html 
print(html.prettify())