import requests
from bs4 import BeautifulSoup

def scrape_kilimall(query):
    search_url = f'https://www.kilimall.co.ke/listing/?q={query}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(search_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        products = []
        for item in soup.select('.wap-div'):
            name = item.select_one('.product-title').text.strip()
            relative_url = item.select_one('a')['href']
            url = f'https://www.kilimall.co.ke{relative_url}'
            price = item.select_one('.sale_price').text.strip()
            products.append({
                'name': name,
                'url': url,
                'price': price,
                'source': 'Kilimall'
            })
        return products
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return []

# # Example usage:
# products = scrape_kilimall('iphone')
# for product in products:
#     print(product)
