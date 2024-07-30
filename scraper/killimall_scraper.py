import requests
from bs4 import BeautifulSoup

def scrape_killimall(query):
    search_url = f'https://www.killimall.co.ke/catalog/?q={query}'
    try:
        response = requests.get(search_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        products = []
        for item in soup.select('.wap-div'):
            name = item.select_one('product-title').text.strip()
            url = item.select_one('a')['href']
            price = item.select_one('.product-price').text.strip()
            products.append({
                'name': name,
                'url': url,
                'price': price,
                'source': 'Killimall'
            })
        return products
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return []
