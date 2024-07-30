import requests
from bs4 import BeautifulSoup

def scrape_jiji(query):
    search_url = f'https://www.jiji.co.ke/search?query={query}'
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    products = []
    for item in soup.select('.masonry-item'):
        name = item.select_one('.b-list-advert-base__data__header').text.strip()
        relative_url = item.select_one('a')['href']
        url = f'https://www.jiji.co.ke{relative_url}'
        price = item.select_one('.qa-advert-price').text.strip()
        
        # Attempt to extract image URL
        img_tag = item.select_one('img')
        if img_tag:
            image_url = img_tag['src']
        else:
            image_url = 'default_image_url'  # Use a placeholder if image URL is not found
        
        products.append({
            'name': name,
            'url': url,
            'price': price,
            'image_url': image_url,
            'source': 'Jiji'
        })
    return products
