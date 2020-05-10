import requests
from bs4 import BeautifulSoup


def scrape(url):
    shoppingList = []
    r = requests.get(url)
    c = r.content
    soup = BeautifulSoup(c, 'html.parser')
    all = soup.find_all('div', {'class':"item li-hover"})
    for item in all:
        it = {'source':"avito.ma"}
        it['title'] = item.find('h2', {'class':'fs14 d-inline-block text-truncate'}).text
        it['location'] = item.find('div', {'class':'re-text'}).text
        it['date'] = item.find('span', {'class':'age-text'}).text
        it['type'] = item.find('div', {'class':'cg-text'}).text
        it['price'] = item.find('span', {'class':'price_value'}).text
        shoppingList.append(it)
    return shoppingList

def get_url(item, city = None):
    url = "https://www.avito.ma/fr/"
    if city!= None:
        url+=city.replace(' ', '_')+'/'
    else:
        url+='maroc/'
    item = item.replace(' ', "_")
    url+=item
    url+="--à_vendre"
    return url
