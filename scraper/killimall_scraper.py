import requests
from bs4 import BeautifulSoup

def scrape_killimall(query):
    search_url = f'https://www.killimall.co.ke/catalog/?q={query}'
    try:
        response = requests.get(search_url)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    products = []

    for item in soup.select('.product'):
        name = item.select_one('.product-name').text.strip()
        url = item.select_one('a')['href']
        price = item.select_one('.price').text.strip()
        products.append({
            'name': name,
            'url': url,
            'price': price,
            'source': 'Killimall'
        })

    return products
