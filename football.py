import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import pandas
import schedule 
import time
import mysql.connector


print()
url = 'https://football.ua/club/42-chelsea.html'

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
footballClub = soup.find('h1').text

info = soup.find(class_='info-page-table').text.replace('\n', ' ')
infoClub = info.replace('\n', ' ')
print(' '*70 + footballClub + ' '*70)
print('-'*145)
print(infoClub)
print('-'*145)
print()
print(' '*20 + '*'*30 + ' Завершені матчі: ' + '*'*29)
print()
next_game = soup.find_all(class_='feed-table')

find_p = [x.find_all('p') for x in next_game]
over_game_date = [x.text.replace('\r\n', '') for x in find_p[0]]
next_game_date = [x.text.replace('\r\n', '') for x in find_p[1]]

find_a = [x.find_all('a') for x in next_game]
over_game_score = [x.text.replace('\r\n', '') for x in find_a[0]]
next_game_score = [x.text.replace('\r\n', '') for x in find_a[1]]

print(' '*20 + '-'*77)
for x in over_game_date:
    print(x)
    print(' '*20 + '-'*77)
    for i in over_game_score[0:3]:
        print(' '*54, i)
    del over_game_score[0:3]
    print(' '*20 + '-'*77)

print()
print(' '*20 + '*'*30 + ' Наступні матчі: ' + '*'*30)
print()
print(' '*20 + '-'*77)
for x in next_game_date:
    print(x)
    print(' '*20 + '-'*77)
    for i in next_game_score[0:3]:
        print(' '*54, i)
    del next_game_score[0:3]
    print(' '*20 + '-'*77)

findInTable = soup.find(class_='tournament-table')
inTable_club = [x.text for x in findInTable.find_all('a')]
inTable_games = [x.text for x in findInTable.find_all('td', class_='games')]
inTable_score = [x.text for x in findInTable.find_all('td', class_='score')]
index = (inTable_club.index(footballClub))
place = index + 1
print()
print('Місце: {}          Зіграно матчів: {}           Набрано очків: {}'.format(place, inTable_games[index], inTable_score[index]))
