import requests
from bs4 import BeautifulSoup

def scrape_jiji(query):
    search_url = f'https://www.jiji.co.ke/search?query={query}'
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    products = []
    for item in soup.select('.product-item'):
        name = item.select_one('.product-title').text.strip()
        url = item.select_one('a')['href']
        price = item.select_one('.product-price').text.strip()
        products.append({
            'name': name,
            'url': url,
            'price': price,
            'source': 'Jiji'
        })
    return products
