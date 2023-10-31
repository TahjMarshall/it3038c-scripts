import requests
from bs4 import BeautifulSoup
import re

def get_amazon_product_details(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        title = soup.find(id='productTitle').get_text().strip()

        price = None
        price_span = soup.find(id='priceblock_ourprice')
        if price_span:
            price = price_span.get_text().strip()
        else:
            pass
        
        return title, price
    else:
        print("Failed to retrieve the webpage. Status code:", response.status_code)
        return None, None

url = "https://www.amazon.com/TAOCOCO-Sectional-Furniture-Slipcovers-Pillowcases/dp/B07ZR6WV41/ref=asc_df_B07ZR6WV41/?tag=&linkCode=df0&hvadid=416790558681&hvpos=&hvnetw=g&hvrand=10269593383446226389&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9015705&hvtargid=pla-872502767463&ref=&adgrpid=90729934461&th=1"
title, price = get_amazon_product_details(url)
if title and price:
    print(f"{title} - {price}")
else:
    print("Failed to extract product details.")

