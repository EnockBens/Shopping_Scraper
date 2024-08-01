import requests
from bs4 import BeautifulSoup

def scrape_jiji(query):
    search_url = f'https://www.jiji.co.ke/search?query={query}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    products = []
    for item in soup.select('.masonry-item'):
        name = item.select_one('.b-list-advert-base__data__header').text.strip()
        relative_url = item.select_one('a')['href']
        url = f'https://www.jiji.co.ke{relative_url}'
        price = item.select_one('.qa-advert-price').text.strip()
        
        # Attempt to extract image URL
        img_tag = item.select_one('img')
        if (img_tag and 'src' in img_tag.attrs):
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
