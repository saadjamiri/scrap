import requests as rq
from bs4 import BeautifulSoup

# URL du site web
url = 'https://books.toscrape.com/'

# Envoyer une requête à la page web
reponse = rq.get(url)

# Parser le contenu HTML avec BeautifulSoup
contenu_page = reponse.text
res = BeautifulSoup(contenu_page, 'html.parser')

# Extraire tous les livres (chaque livre est contenu dans une balise article avec la classe "product_pod")
books = res.find_all("article", class_="product_pod")

# Extraire le titre, le prix et la disponibilité pour chaque livre
for book in books:
    # Titre du livre
    titre = book.h3.a["title"]
    
    # Prix du livre (le prix est dans un paragraphe avec la classe "price_color")
    prix = book.find("p", class_="price_color").text
    
    # Disponibilité du livre (dans un paragraphe avec la classe "instock availability")
    disponibilite = book.find("p", class_="instock availability").text.strip()
    
    # Afficher les informations extraites
    print(f"Titre: {titre}")
    print(f"Prix: {prix}")
    print(f"Disponibilité: {disponibilite}")
    print('-' * 40)
