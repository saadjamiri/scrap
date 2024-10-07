import requests
from bs4 import BeautifulSoup

# URL de la page principale
url = 'https://quotes.toscrape.com/'

# Initialisation d'une variable pour le nombre total de pages
total_pages = 0

while url:  # Continue tant que 'url' n'est pas None
    # Envoyer une requête GET
    response = requests.get(url)

    # Vérifiez si la requête a réussi
    if response.ok:
        # Analyser le contenu HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Incrémenter le compteur de pages
        total_pages += 1

        # Trouver l'élément de pagination pour la prochaine page
        next_page = soup.find('li', class_='next')  # Rechercher le lien vers la page suivante

        if next_page:  # Si la page suivante existe
            url = next_page.find('a')['href']  # Obtenir le lien de la page suivante
            url = 'https://quotes.toscrape.com' + url  # Construire l'URL complète
        else:
            url = None  # Finir la boucle si aucune page suivante
    else:
        print("Échec de la requête.")
        break  # Sortir de la boucle en cas d'échec de la requête

print(f"Nombre total de pages : {total_pages}")
