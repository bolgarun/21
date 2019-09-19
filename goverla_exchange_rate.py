import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import pandas
import schedule 
import time
import mysql.connector


def goverla(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    exchange_rate = soup.find_all(class_='gvrl-table-row')
    list_exchange_rate = exchange_rate[1:12]

    title = [x.img['alt'] for x in list_exchange_rate]

    to_buy = [x.find(class_='gvrl-table-cell bid').get_text() for x in list_exchange_rate]
    to_buy_final = list(map(lambda x:x.strip(),to_buy))

    to_cell = [x.find(class_='gvrl-table-cell ask').get_text() for x in list_exchange_rate]
    to_cell_final = list(map(lambda x:x.strip(),to_cell))

    money = pandas.DataFrame(
        {
            'title': title,
            'to_buy': to_buy_final,
            'to_cell': to_cell_final
        })
    print(money)

    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='123',
        db='mysql',
        charset='utf8'
        )
    cur = conn.cursor()
    cur.execute("USE scrap")

    delete_form = "DELETE FROM goverla"
    cur.execute(delete_form)
    conn.commit()

    while title != []:
        sqlform = "Insert into goverla(title, to_buy, to_cell) values(%s, %s, %s)"
        data = [(title[0], to_buy_final[0], to_cell_final[0])]
        cur.executemany(sqlform, data)
        conn.commit()
        title.remove(title[0])
        to_buy_final.remove(to_buy_final[0])
        to_cell_final.remove(to_cell_final[0])

goverla('https://goverla.ua/')


schedule.every().hour.do(goverla)
x = 1
while True: 
    schedule.run_pending() 
    time.sleep(5)
    print(x)
    x+=1