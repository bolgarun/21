import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import pandas

url = "https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%96%D0%B2%D0%B0%D0%BD%D0%BE-%D1%84%D1%80%D0%B0%D0%BD%D0%BA%D1%96%D0%B2%D1%81%D1%8C%D0%BA"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
title = soup.find_all(class_='main')
title_10 = title


cells_1 = [title.find(class_='date').get_text() for title in title_10]

cells_2 = [title.find(class_='day-link').get_text() for title in title_10]

cells_3 = [title.find(class_='month').get_text() for title in title_10]

cells_4 = [title.find(class_='min').get_text() for title in title_10]

cells_5 = [title.find(class_='max').get_text() for title in title_10]

wather = pandas.DataFrame(
    {
        'first': cells_2,
        'second': cells_1,
        'third': cells_3,
        'fourth': cells_4,
        'fifth': cells_5    
    })

print(wather)
