import requests
from bs4 import BeautifulSoup

def scrape_jumia(query):
    search_url = f'https://www.jumia.co.ke/catalog/?q={query}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(search_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        products = []
        for item in soup.select('.sku.-gallery'):
            name = item.select_one('.name').text.strip()
            relative_url = item.select_one('a.link')['href']
            url = f'https://www.jumia.co.ke{relative_url}'
            price = item.select_one('.price').text.strip()
            products.append({
                'name': name,
                'url': url,
                'price': price,
                'source': 'Jumia'
            })
        return products
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return []

# Example usage:
# if __name__ == '__main__':
#     products = scrape_jumia('iphone')
#     for product in products:
#         print(product)
