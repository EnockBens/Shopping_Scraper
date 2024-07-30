import requests
from bs4 import BeautifulSoup

def scrape_amazon(query):
    search_url = f'https://www.amazon.com/s?k={query}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    products = []
    for item in soup.select('.puisg-row'):
        name = item.select_one('h2 .a-link-normal').text.strip()
        url = 'https://www.amazon.com' + item.select_one('h2 .a-link-normal')['href']
        price = item.select_one('.a-price-whole')
        if price:
            price = price.text.strip()
        else:
            price = 'N/A'
        products.append({
            'name': name,
            'url': url,
            'price': price,
            'source': 'Amazon'
        })
    return products
