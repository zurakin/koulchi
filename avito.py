import requests
from bs4 import BeautifulSoup


def scrape(url, min=0, max=float('inf')):
    shoppingList = []
    r = requests.get(url)
    c = r.content
    soup = BeautifulSoup(c, 'html.parser')
    all = soup.find_all('div', {'class':"item li-hover"})
    for item in all:
        price = item.find('span', {'class':'price_value'}).text.strip().replace(' ', '')
        try:
            price = int(price)
            if price<min or price>max:
                continue
        except:
            continue
        it = {'source':"avito"}
        it['title'] = item.find('h2', {'class':'fs14 d-inline-block text-truncate'}).text.strip()
        it['location'] = item.find('div', {'class':'re-text'}).text.strip()
        it['date'] = item.find('span', {'class':'age-text'}).text.strip().replace('\n', ' ')
        it['type'] = item.find('div', {'class':'cg-text'}).text.strip()
        it['price'] = price
        it['link'] = item.find('a', href=True)['href']
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
