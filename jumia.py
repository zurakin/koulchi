import requests
from bs4 import BeautifulSoup


def scrape(url):
    shoppingList = []
    r = requests.get(url)
    c = r.content
    soup = BeautifulSoup(c, 'html.parser')
    all = soup.find_all('div', {'class':"sku -gallery"})
    for item in all:
        # price = item.find('span', {'dir':'ltr'})['data-price']
        it = {'source':"jumia"}
        it['title'] = item.find('h2', {'class':'title'}).text.strip()
        it['location'] = 'Morocco'
        it['date'] = 'This product is New !'
        it['type'] = ''
        it['price'] = item.find('span', {'data-price':True})['data-price']
        # it['price'] = item.find('span', {'dir':'ltr'})['data-price']
        it['link'] = item.find('a', href=True)['href']
        shoppingList.append(it)
    return shoppingList

def get_url(item, min=0, max=1000000):
    url = "https://www.jumia.ma/"
    item = item.replace(' ', "_")
    url+=item+'/'
    url+=f'?price={min}-{max}'
    print(url)
    return url
