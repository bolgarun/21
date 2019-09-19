import time
import csv
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


f = open('instagram_followers.csv', 'w')
writer = csv.writer(f)

chromedriver = '/home/user/Downloads/chromedriver'
driver = webdriver.Chrome(chromedriver)
driver.get('https://www.instagram.com/')
time.sleep(2)
driver.maximize_window()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys('bolgarun21@gmail.com')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys('test2232601')
time.sleep(3)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[1]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/a/span').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
time.sleep(2)


fBody  = driver.find_element_by_xpath("//div[@class='isgrP']")
scroll = 0
while scroll < 7:
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
    time.sleep(3)
    scroll += 1

time.sleep(10)
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')
list_follower = soup.find(class_='PZuss')
list_a = list_follower.find_all('a', 'FPmhX notranslate _0imsa')
follower = []
for x in list_a:
    follower.append(x.text)
for i in range(len(follower)):
    writer.writerow([follower[i]])
    print(i+1, follower[i])
f.close()