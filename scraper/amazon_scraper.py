import requests
from bs4 import BeautifulSoup
import random
import time

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54'
]

def scrape_amazon(query):
    search_url = f'https://www.amazon.com/s?k={query}'
    headers = {
        'User-Agent': random.choice(user_agents)
    }
    try:
        response = requests.get(search_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        products = []
        for item in soup.select('.s-main-slot .s-result-item'):
            name = item.select_one('h2 .a-link-normal').text.strip() if item.select_one('h2 .a-link-normal') else "Name not available"
            relative_url = item.select_one('h2 .a-link-normal')['href'] if item.select_one('h2 .a-link-normal') else "#"
            url = f'https://www.amazon.com{relative_url}'
            price_whole = item.select_one('.a-price-whole')
            price_fraction = item.select_one('.a-price-fraction')
            price = f"{price_whole.text.strip()}.{price_fraction.text.strip()}" if price_whole and price_fraction else "Price not available"
            products.append({
                'name': name,
                'url': url,
                'price': price,
                'source': 'Amazon'
            })
        return products
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return []

# Example usage:
if __name__ == '__main__':
    products = scrape_amazon('iphone')
    for product in products:
        print(product)
         