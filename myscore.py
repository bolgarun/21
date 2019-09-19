import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import pandas
import re
from selenium import webdriver



url = 'https://www.myscore.ua/'
chromedriver = '/home/user/Downloads/chromedriver'
driver = webdriver.Chrome(chromedriver)
driver.get(url)

event = driver.find_element_by_class_name('event')

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')
events = soup.find_all(title='Подробиці матчу!')

list_home = []
for x in events:
    if x.find(class_='event__participant event__participant--home') != None:
        list_home.append(x.find(class_='event__participant event__participant--home').text)
    if x.find(class_='event__participant event__participant--home fontBold') != None:
        list_home.append(x.find(class_='event__participant event__participant--home fontBold').text)

list_goest = []
for x in events:
    if x.find(class_='event__participant event__participant--away') != None:
        list_goest.append(x.find(class_='event__participant event__participant--away').text)
    if x.find(class_='event__participant event__participant--away fontBold') != None:
        list_goest.append(x.find(class_='event__participant event__participant--away fontBold').text)

list_event_time = []
for x in events:
    if x.find(class_='event__time') != None:
        list_event_time.append(x.find(class_='event__time').text)
    if x.find(class_='event__stage') != None:
        list_event_time.append(x.find(class_='event__stage').text)

scoreList = []
for x in events:
    if x.find(class_='event__scores fontBold') != None:
        scoreList.append(x.find(class_='event__scores fontBold').text)
    else:
        scoreList.append('--')


title_event = pandas.DataFrame(
    {
        'event_time': list_event_time,
        'g_home_team': list_home,
        'h_score': scoreList,
        's_goest_team': list_goest,
    })

print(title_event)
