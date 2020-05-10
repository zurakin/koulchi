import pandas as pd
from datetime import datetime
import avito

def get_file_name(item, city = None):
    name = item.replace(' ', '_')+' '
    if city !=None :
        name += city+' '
    else:
        name += 'maroc '
    now = datetime.now()
    name += now.strftime('%H.%M %d.%h.%y')
    name += '.csv'
    return name


def main():
    item = input('What are you looking for ?\n-->')
    city = input('What city to look for ?\n-->')
    if city == '':
        city = None
    url = avito.get_url(item, city)
    ShL = avito.scrape(url)
    df = pd.DataFrame(ShL)
    fileName = get_file_name(item, city)
    df.to_csv(fileName)


if __name__=="__main__":
    main()
