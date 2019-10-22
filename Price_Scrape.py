from bs4 import BeautifulSoup
import requests

url = 'https://loaf.com/products/squishmeister-chaise-sofa'  

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

price_box = soup.find('span', attrs={'class':'js-chosen_price'})['data-prices']

price = price_box

print (price)
